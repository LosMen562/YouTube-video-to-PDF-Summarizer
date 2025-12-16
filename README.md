# YouTube to Markdown Summarizer

A Python tool that downloads YouTube videos, transcribes them using OpenAI Whisper, and generates organized Markdown summaries.

## Features

-   🎥 Downloads audio from YouTube videos
-   🎤 Transcribes audio using OpenAI Whisper
-   🤖 Auto-detects video type (DIY Tutorial, List/Ideas, General Info)
-   📝 Generates structured Markdown with timestamps
-   ⚡ Works with Python 3.11+

## Installation

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install pytubefix whisper openai-whisper nltk
```

## Usage

```bash
# Run interactively
python youtube_to_pdf.py

# Or with arguments
python youtube_to_pdf.py "https://www.youtube.com/watch?v=VIDEO_ID" "output.md"
```

## Requirements

-   Python 3.11 or higher
-   pytubefix
-   openai-whisper
-   nltk

## Output

Generates a Markdown file with:

-   Video metadata
-   Structured content based on video type
-   Timestamps for easy reference
-   Organized sections

## Converting to PDF

Use online tools or pandoc:

```bash
pandoc output.md -o output.pdf
```

## License

MIT

## Todo

-   [ ] Add more video type detection
-   [ ] Improve section splitting
-   [ ] Add export options (HTML, DOCX)
