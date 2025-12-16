"""
YouTube Video to Markdown Summarizer
=====================================
This script downloads a YouTube video's audio, transcribes it, analyzes the content,
and generates a structured Markdown file based on the video type.

Required installations:
pip install pytubefix whisper openai-whisper nltk

Markdown is much more reliable than PDF and can be:
- Read directly in any text editor
- Converted to PDF using pandoc or online tools
- Viewed beautifully on GitHub
- Edited easily
"""

import os
import sys
import re
import warnings
from datetime import timedelta
from pathlib import Path

# Suppress warnings
warnings.filterwarnings("ignore")

# Import required libraries
try:
    from pytubefix import YouTube
    import whisper
    import nltk
    from nltk.tokenize import sent_tokenize, word_tokenize
    from collections import Counter
except ImportError as e:
    print(f"Error: Missing required library. {e}")
    print("\nPlease install required packages:")
    print("pip install pytubefix whisper openai-whisper nltk")
    sys.exit(1)

# Download required NLTK data
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt", quiet=True)

try:
    nltk.data.find("tokenizers/punkt_tab")
except LookupError:
    nltk.download("punkt_tab", quiet=True)


class VideoType:
    """Enum-like class for video types"""

    DIY_TUTORIAL = "diy_tutorial"
    LIST_IDEAS = "list_ideas"
    GENERAL_INFO = "general_info"


class YouTubeToMarkdown:
    """Main class for converting YouTube videos to structured Markdown"""

    def __init__(self, video_url):
        self.video_url = video_url
        self.yt = None
        self.audio_path = None
        self.transcript = None
        self.video_info = {}
        self.video_type = None
        self.structured_content = []

    def download_audio(self):
        """Download audio stream from YouTube video"""
        print("Fetching video information...")
        try:
            self.yt = YouTube(self.video_url)
            self.video_info = {
                "title": self.yt.title,
                "author": self.yt.author,
                "duration": str(timedelta(seconds=self.yt.length)),
                "views": self.yt.views,
                "url": self.video_url,
            }

            print(f"Title: {self.video_info['title']}")
            print(f"Duration: {self.video_info['duration']}")
            print("\nDownloading audio stream...")

            audio_stream = self.yt.streams.filter(only_audio=True).first()

            if not audio_stream:
                raise Exception("No audio stream available")

            output_path = audio_stream.download(filename="temp_audio.mp4")
            self.audio_path = output_path
            print(f"Audio downloaded successfully: {output_path}")
            return True

        except Exception as e:
            print(f"Error downloading audio: {e}")
            return False

    def transcribe_audio(self):
        """Transcribe audio using Whisper"""
        if not self.audio_path or not os.path.exists(self.audio_path):
            print("Error: Audio file not found")
            return False

        try:
            print("\nTranscribing audio (this may take a few minutes)...")
            model = whisper.load_model("base")
            result = model.transcribe(self.audio_path, verbose=False)

            self.transcript = {
                "text": result["text"],
                "segments": result.get("segments", []),
            }

            print("Transcription completed successfully!")
            print(f"Transcript length: {len(self.transcript['text'])} characters")
            return True

        except Exception as e:
            print(f"Error transcribing audio: {e}")
            return False

    def detect_video_type(self):
        """Detect video type based on title and transcript analysis"""
        text = (self.video_info["title"] + " " + self.transcript["text"]).lower()

        diy_keywords = [
            "how to",
            "tutorial",
            "build",
            "make",
            "create",
            "diy",
            "step by step",
            "instructions",
            "guide",
            "install",
            "setup",
            "first",
            "second",
            "third",
            "next step",
            "finally",
        ]

        list_keywords = [
            "top 10",
            "top 5",
            "ideas for",
            "suggestions",
            "list of",
            "best",
            "ways to",
            "things you",
            "number",
            "idea number",
            "tip number",
            "method",
            "technique",
        ]

        diy_score = sum(1 for keyword in diy_keywords if keyword in text)
        list_score = sum(1 for keyword in list_keywords if keyword in text)

        numbered_pattern = re.findall(
            r"\b(number \d+|tip \d+|idea \d+|step \d+|\d+\.)", text
        )
        if len(numbered_pattern) > 3:
            list_score += 3

        if diy_score > list_score and diy_score >= 2:
            self.video_type = VideoType.DIY_TUTORIAL
            print("\nDetected video type: DIY Tutorial")
        elif list_score >= 3:
            self.video_type = VideoType.LIST_IDEAS
            print("\nDetected video type: List/Ideas")
        else:
            self.video_type = VideoType.GENERAL_INFO
            print("\nDetected video type: General Information")

        return self.video_type

    def structure_content(self):
        """Structure content based on video type"""
        print("Structuring content...")

        if self.video_type == VideoType.DIY_TUTORIAL:
            self.structured_content = self._structure_diy_tutorial()
        elif self.video_type == VideoType.LIST_IDEAS:
            self.structured_content = self._structure_list()
        else:
            self.structured_content = self._structure_general()

        print(f"Created {len(self.structured_content)} sections")
        return self.structured_content

    def _structure_diy_tutorial(self):
        """Structure content as step-by-step tutorial"""
        sections = []
        segments = self.transcript["segments"]

        step_patterns = [
            r"\b(step \d+)",
            r"\b(first|second|third|fourth|fifth|next|then|finally|lastly)",
            r"\b(number \d+)",
        ]

        current_step = 0
        current_content = []
        last_timestamp = 0

        for segment in segments:
            text = segment["text"].strip()
            timestamp = segment["start"]

            is_new_step = False
            for pattern in step_patterns:
                if re.search(pattern, text.lower()):
                    is_new_step = True
                    break

            if is_new_step and current_content:
                current_step += 1
                sections.append(
                    {
                        "title": f"Step {current_step}",
                        "content": " ".join(current_content),
                        "timestamp": self._format_timestamp(last_timestamp),
                    }
                )
                current_content = [text]
                last_timestamp = timestamp
            else:
                current_content.append(text)
                if not last_timestamp:
                    last_timestamp = timestamp

        if current_content:
            current_step += 1
            sections.append(
                {
                    "title": f"Step {current_step}",
                    "content": " ".join(current_content),
                    "timestamp": self._format_timestamp(last_timestamp),
                }
            )

        if len(sections) < 2:
            sections = self._create_time_based_sections()

        return sections

    def _structure_list(self):
        """Structure content as numbered list of ideas"""
        sections = []
        segments = self.transcript["segments"]

        list_patterns = [
            r"\b(number \d+)",
            r"\b(idea \d+)",
            r"\b(tip \d+)",
            r"\b(\d+\.)",
            r"\b(first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth)",
        ]

        current_item = 0
        current_content = []
        last_timestamp = 0

        for segment in segments:
            text = segment["text"].strip()
            timestamp = segment["start"]

            is_new_item = False
            for pattern in list_patterns:
                match = re.search(pattern, text.lower())
                if match:
                    is_new_item = True
                    break

            if is_new_item and current_content:
                current_item += 1
                sections.append(
                    {
                        "title": f"Idea #{current_item}",
                        "content": " ".join(current_content),
                        "timestamp": self._format_timestamp(last_timestamp),
                    }
                )
                current_content = [text]
                last_timestamp = timestamp
            else:
                current_content.append(text)
                if not last_timestamp:
                    last_timestamp = timestamp

        if current_content:
            current_item += 1
            sections.append(
                {
                    "title": f"Idea #{current_item}",
                    "content": " ".join(current_content),
                    "timestamp": self._format_timestamp(last_timestamp),
                }
            )

        if len(sections) < 2:
            sections = self._create_time_based_sections()
            for i, section in enumerate(sections):
                section["title"] = f"Idea #{i+1}"

        return sections

    def _structure_general(self):
        """Structure content as chronological sections"""
        return self._create_time_based_sections()

    def _create_time_based_sections(self):
        """Create sections based on time intervals"""
        sections = []
        segments = self.transcript["segments"]

        if not segments:
            return [
                {
                    "title": "Content",
                    "content": self.transcript["text"],
                    "timestamp": "00:00",
                }
            ]

        total_duration = segments[-1]["end"]
        target_sections = min(8, max(3, int(total_duration / 120)))
        section_duration = total_duration / target_sections

        current_section = []
        section_start = 0
        section_num = 1

        for segment in segments:
            current_section.append(segment["text"].strip())

            if segment["end"] >= section_start + section_duration:
                section_text = " ".join(current_section)
                topic = self._extract_topic(section_text)

                sections.append(
                    {
                        "title": f"Section {section_num}: {topic}",
                        "content": section_text,
                        "timestamp": self._format_timestamp(section_start),
                    }
                )

                current_section = []
                section_start = segment["end"]
                section_num += 1

        if current_section:
            section_text = " ".join(current_section)
            topic = self._extract_topic(section_text)
            sections.append(
                {
                    "title": f"Section {section_num}: {topic}",
                    "content": section_text,
                    "timestamp": self._format_timestamp(section_start),
                }
            )

        return sections

    def _extract_topic(self, text):
        """Extract main topic from text using simple NLP"""
        text = text[:500]
        words = word_tokenize(text.lower())

        stop_words = {
            "the",
            "a",
            "an",
            "and",
            "or",
            "but",
            "in",
            "on",
            "at",
            "to",
            "for",
            "of",
            "with",
            "by",
            "from",
            "as",
            "is",
            "was",
            "are",
            "were",
            "be",
            "been",
            "being",
            "have",
            "has",
            "had",
            "do",
            "does",
            "did",
            "will",
            "would",
            "could",
            "should",
            "may",
            "might",
            "can",
            "this",
            "that",
            "these",
            "those",
            "i",
            "you",
            "he",
            "she",
            "it",
            "we",
            "they",
        }

        meaningful_words = [
            w for w in words if w.isalnum() and w not in stop_words and len(w) > 3
        ]

        if meaningful_words:
            word_freq = Counter(meaningful_words)
            common_words = word_freq.most_common(3)
            topic = " ".join([word[0].title() for word in common_words])
            if topic:
                return topic

        words = text.split()[:5]
        return " ".join(words).title() + "..."

    def _format_timestamp(self, seconds):
        """Format seconds to MM:SS or HH:MM:SS"""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)

        if hours > 0:
            return f"{hours:02d}:{minutes:02d}:{secs:02d}"
        else:
            return f"{minutes:02d}:{secs:02d}"

    def generate_markdown(self, output_filename="output.md"):
        """Generate Markdown with structured content"""
        print(f"\nGenerating Markdown: {output_filename}")

        try:
            with open(output_filename, "w", encoding="utf-8") as f:
                # Title
                f.write(f"# {self.video_info['title']}\n\n")

                # Metadata
                f.write("## Video Information\n\n")
                f.write(f"- **Creator:** {self.video_info['author']}\n")
                f.write(f"- **Duration:** {self.video_info['duration']}\n")
                f.write(
                    f"- **URL:** [{self.video_info['url']}]({self.video_info['url']})\n\n"
                )

                # Summary
                f.write("## Summary\n\n")
                if self.video_type == VideoType.DIY_TUTORIAL:
                    f.write(
                        "This document provides a structured summary of the tutorial, organized as step-by-step instructions.\n\n"
                    )
                elif self.video_type == VideoType.LIST_IDEAS:
                    f.write(
                        "This document provides a structured summary of the video, organized as a list of ideas/suggestions.\n\n"
                    )
                else:
                    f.write(
                        "This document provides a structured summary of the video, organized into chronological sections.\n\n"
                    )

                f.write("---\n\n")

                # Structured content
                f.write("## Content\n\n")

                for i, section in enumerate(self.structured_content):
                    # Section title with timestamp
                    f.write(f"### {section['title']} `[{section['timestamp']}]`\n\n")

                    # Section content
                    content = section["content"].strip()
                    # Format into readable paragraphs
                    sentences = sent_tokenize(content)

                    # Group sentences into paragraphs (every 3-4 sentences)
                    paragraph_size = 3
                    for j in range(0, len(sentences), paragraph_size):
                        paragraph = " ".join(sentences[j : j + paragraph_size])
                        f.write(f"{paragraph}\n\n")

                    f.write("---\n\n")

                # Footer
                f.write("\n*Generated by YouTube to Markdown Summarizer*\n")

            print(f"Markdown generated successfully: {output_filename}")
            print(f"\nYou can:")
            print(f"  1. Read it in any text editor")
            print(f"  2. View it on GitHub (looks great!)")
            print(f"  3. Convert to PDF using: pandoc {output_filename} -o output.pdf")
            print(
                f"  4. Use online converters like dillinger.io or markdown-to-pdf.com"
            )
            return True

        except Exception as e:
            print(f"Error generating Markdown: {e}")
            import traceback

            traceback.print_exc()
            return False

    def cleanup(self):
        """Remove temporary audio file"""
        if self.audio_path and os.path.exists(self.audio_path):
            try:
                os.remove(self.audio_path)
                print("\nTemporary files cleaned up")
            except Exception as e:
                print(f"Warning: Could not remove temporary file: {e}")

    def process(self, output_filename="output.md"):
        """Main processing pipeline"""
        try:
            if not self.download_audio():
                return False

            if not self.transcribe_audio():
                return False

            self.detect_video_type()
            self.structure_content()

            if not self.generate_markdown(output_filename):
                return False

            return True

        finally:
            self.cleanup()


def main():
    """Main function"""
    print("=" * 60)
    print("YouTube Video to Markdown Summarizer")
    print("=" * 60)
    print()

    if len(sys.argv) > 1:
        video_url = sys.argv[1]
    else:
        video_url = input("Enter YouTube video URL: ").strip()

    if not video_url:
        print("Error: No URL provided")
        sys.exit(1)

    if not ("youtube.com" in video_url or "youtu.be" in video_url):
        print("Error: Invalid YouTube URL")
        sys.exit(1)

    if len(sys.argv) > 2:
        output_filename = sys.argv[2]
    else:
        output_filename = input(
            "Enter output filename (press Enter for 'output.md'): "
        ).strip()
        if not output_filename:
            output_filename = "output.md"

    if not output_filename.endswith(".md"):
        output_filename += ".md"

    processor = YouTubeToMarkdown(video_url)
    success = processor.process(output_filename)

    if success:
        print("\n" + "=" * 60)
        print("SUCCESS! Markdown generated successfully.")
        print(f"Output file: {output_filename}")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("FAILED: Could not complete processing")
        print("=" * 60)
        sys.exit(1)


if __name__ == "__main__":
    main()
