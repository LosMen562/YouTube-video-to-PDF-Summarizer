# Raspberry Pi 5: Getting Started

## Video Information

- **Creator:** Jeff Geerling
- **Duration:** 0:24:42
- **URL:** [https://www.youtube.com/watch?v=UtLyX72-688](https://www.youtube.com/watch?v=UtLyX72-688)

## Summary

This document provides a structured summary of the tutorial, organized as step-by-step instructions.

---

## Content

### Step 1 `[00:04]`

In almost 500 videos, I've never made a guide for getting started with Raspberry Pi. So today, at this brand new microcenter in Charlotte, I thought I'd do that. And this location is special to me.

See, last year on the Mr. B set, I needed parts for button and LED controls, and there was nowhere in North Carolina I could get them the same day. They had almost everything in that Mr. B's building, except for the little electronics parts I needed. Yeah, just years of collecting stuff, little projects here and there, I just have everything that we would possibly need.

But you don't have a microcenter here. I don't have a microcenter. I just wish they had a greenville location because that really would have helped when I got on set.

Well, microcenter was listening. They just opened up here in Charlotte. It's not quite greenville, but that's a heck of a lot closer than Atlanta.

And I mean, other channels talk graphics cards, PC builds, and even Apple stuff. But when I come, I head straight to the Maker section. And Raspberry Pi is front and center.

For this video, I wanted to try out two projects perfect for getting started with the Raspberry Pi. Building a remote Pi camera and building an indoor air monitor. Everything I need should be inside this building.

And yes, microcenter sponsored this video. By the end of it, I'll build a great starter Pi rig and we'll give it away to some

---

### Step 2 `[01:10]`

lucky visitor here in Charlotte. The first thing you have to decide is which Pi to get. There are five generations of Raspberry Pi and there are also completely different form factors in each generation.

Like this tiny Pi Zero fits almost anywhere, but it doesn't have an Ethernet port or full-size USB. The Pi 4 and Pi 5 have that, but they're kind of naked boards. You have to buy a case, a power

---

### Step 3 `[01:30]`

supply, and all those things. Then there's the Pi 400. This kit that's 99 bucks comes with a Pi built into a keyboard, a mouse, a power supply, and it already has POS installed, so you can just plug an monitor and you're done.

But each Pi has its own merits. Like the Pi Zero isn't full featured, but it only costs 15 bucks and sits a tiny bit of power. Great for things like remote sensors or time lapse cameras.

The Pi 5 starts at 60 bucks, but it's about as fast as a basic cheap PC, but just tiny, and with tons of maker-friendly expansion options. The Pi 4 is like the Pi 5, but slower and you can get it at 35 bucks. All the pies are great for different projects, but today I'm going to stick with the latest version, the Pi 5.

It's the most flexible pie for anything from programming sensors to machine learning. I also need a keyboard and mouse. You could use any old set, but I'll grab the official Pi versions along with the Pi 5 case.

That's it for the basic kit, but for a camera project, I'll grab one of the Pi camera modules. This version has built-in auto focus, and it's about as good as a mid-range smartphone camera. The tiny size means I can put it almost anywhere, like this one watching my 3D printer.

To build an air monitoring station with a Pi, there are a lot of options. I could buy individual sensors, and Micro Center has tons of those, but one board I love is Pymoronis and Virou Plus air quality sensor. This thing comes in two versions that both use the Pi's GPIO, or General Purpose Input and Output Pins.

GPIO pins are one of the Pi's superpowers, and it really what makes a Pi a Pi. I'll grab the Plus version, but before we head over to build the Pi, I'll grab a couple other accessories in the style. When I'm hacking on a Pi project, I like to have the Pi mounted up on a tray instead of buried inside a case.

This acrylic case is perfect for that. I can run it without the top for easy access to everything. There are also tons of other hats, adapters, and other project boards.

I almost never leave this aisle empty-handed. That's the danger of living close to a Micro Center. There are also other cases, so many cases, and I'll be posting a video covering some of my favorite soon-so-subscribe.

I also grabbed an Ace or Monitor Micro Center head on sale for 99 bucks, and I like this one because it has built-in speakers, and I needed storage for the Pi, so I grabbed one of Micro Center's premium Micro SD cards. You can actually boot a Pi from a hard driver SSD too, but Micro SD is easy and cheap, as long as you get a decent card. And one last thing, the Pi camera doesn't have any way of mounting it to a tripod or anything, so I found a 3D printable case online, and I know Micro Center has 3D printers in the back, so I'm going to see if I can get a case printed.

I have the print file on here, and I'm going to try to get this to go. I've never used an A1 Mini before. Hey, whatcha doing over here?

Sorry, I need to print something for my video, and I was wondering, could I print it on one of these? Sure, what type of filming are you? I didn't think about that, but I saw that you guys have a really cool new way of getting filament in here.

Yeah, it's a mini machine. Can you show me how that works? Sure can.

What kind of color do you want? Well, I was thinking like a Raspberry Pi can red. Yeah, this is cool.

So these swatches show you how to print it. Okay, so like you just, this is actually that filament printer. These are actually printed, shows you how it prints all the bumps.

That is cool. All right, well, this says red, but it looks a little orange. I think this is a little more close to the Raspberry Pi red.

All right, so let's get one of these. How does this work? So we just take it over here, scan it into the machine,

---

### Step 4 `[04:54]`

and then it rotates around. Well, that one's out. Of course, that's the only one that's empty.

---

### Step 5 `[05:10]`

We've got like 20 of that one, so if you don't find it the first time,

---

### Step 6 `[05:16]`

it goes to the next one and we do have it there. Oh, right here. Yeah, so, well, thank you.

Can you, could you take care of that for me while I shoot the video? Sounds good, yeah. So unlike a desktop PC, this actually has everything on one board.

That's why it's called a single board computer. And that is the Raspberry Pi 5. If you have the ports over here, the GPIO pins and the processor, the memory, and the storage goes here.

And I got this micro center card. It's 256 gigabytes and it's super tiny. And it doesn't have an operating system on it.

So I'm going to put it into the pie, but we're not going to have an operating system yet. We're going to get that through the internet once we plug it in. To work with it, I'm going to use this pie keyboard.

So they didn't have the red and white one in stock. So we have the black and gray keyboard, which actually I think looks a little nicer, but it doesn't match the pie aesthetic. But it does have a matching black cable.

The pie keyboard also is nice because it has a built-in USB hub so you can plug multiple devices through it. One thing to keep in mind though, it doesn't have that much power. So you're not going to like charge your phone through here, but you can plug more USB devices.

The pie mouse is nothing to write home about, but it's a mouse. It has two buttons and a scroll wheel that clicks. On the pie 5, there's USB 2.0 ports, two of those, and USB 3.0 ports.

A keyboard doesn't need that much speed, so you should plug it in on this side. You could plug it on on either side, but if you're plugging in a hard drive or anything else that needs a lot of speed, plug it into the blue ports. And I can plug the mouse right into the pie, or I can also plug it into the back of the keyboard here.

And this mat is not ESD safe, but it's probably okay, but I do like to have the pie in a case or on something. So that's why I bought this acrylic stackable case. I'm going to use this without the fan on it for now.

That way I'll have easy access to all the ports on the pie. In this case comes with some heat sinks, which I can put on these. The pie runs okay without any heat sinks, but if you want the best performance, you want to run with the heat sink and it's nice that they include a fan here to get some air flow over it, just to keep it from overheating and thermal throttling and losing a little performance.

And it looks like this kit was actually made for the pie 4, which has the more squared off heat spreader on the top. But it still works. It's going to provide a little bit more area for the heat to come off.

You wouldn't really need a heat sink on the Wi-Fi module, but this one is a little big for that power module, which actually can get a little hot. So if you get a heat sink kit for the pie 5, it usually has a smaller one for that. But we can run it without it, it should be okay.

And once I deploy a pie, I'll put a fan on it, but for this testing that we're doing right now, we don't need a fan. It's not going to overheat, not in the open air like this. Although today it's 93 in Charlotte, so you'll see.

And I'm going to put these rubber feet on the bottom, so it doesn't slide around too much. One neat thing about this case in particular is it's stackable. You could actually put another case on top of this one, and have them stacked up to build your own little pie cluster

---

### Step 7 `[09:07]`

if you want. I have videos on that. Yes, be plugged in.

And then the pie 5, this is something I don't really like about all the pie 4 and pie 5 generation. They have micro HDMI, which means that you need an adapter cable if you want to plug in a standard HDMI monitor. They sell one, and it's like seven bucks, but it would be annoying like the monitor comes with a cable.

So you have to buy an extra cable just to plug it in. I would rather just have full size HDMI, so you didn't have to deal

---

### Step 8 `[09:40]`

with this. Plug this into the monitor. There it is.

And then I'll plug the pie's power supply into power. And if you're using a Raspberry Pi 5, it's good to get the official power supply, or another one that provides at least 25 to 30 watts, because the Pi 5 does need a little bit more power than the Pi 4 generation. But you can use other power supplies too.

It's just you might not be able to do things like plug an SSD or hard drive into it and have it be working. So now if I plug it in, it's going to turn on right away, but it doesn't have an operating system. And the easiest way to do this is to plug it into your network using an Ethernet cable.

And if you have internet access, you can hold down the shift key on the keyboard, and it will boot into the network installer.

---

### Step 9 `[10:29]`

If you don't have internet access, then you'll need another computer. And on the other computer,

---

### Step 10 `[10:33]`

you can plug the microSD card in and use Raspberry Pi's imager tool. And then you can flash the Raspberry Pi operating system onto it there. But in my case, I do have an Ethernet cable with internet.

So if I plug this in, hopefully it's actually plugged in somewhere. I didn't check that before yet. So we're changing course a little bit.

I found out that this Ethernet cable is plugged in, but it only works in certain scenarios and not with the Raspberry Pi. So I'm going to take the microSD card out of here. I'm also going to shut down the Pi by holding down the button on the front until the little LED turns red.

And I'm going to flash it using my Mac, using of course a dongle because Apple doesn't believe in having cards lots on their computers. So I'll plug this in

---

### Step 11 `[11:26]`

here. And then I'm going to use Raspberry Pi imager on my Mac. So this is a very similar process to what you'd get with the network boot.

You choose your device. So in this case, it's a Raspberry Pi 5. Choose your operating system.

99% of the time you're going to choose this, but you can actually choose other systems like you can choose Retro Pi for gaming or you can choose Octopi for 3D printing. There's a lot of different operating systems for Raspberry Pi. But this one is the nicest one

---

### Step 12 `[11:52]`

for getting started with all kinds of projects on the Pi. And then you choose your storage, which it's a 256GB microSD card. You can also change up some settings on the Pi in the imager or you can change them later on the Pi.

In my case, since I use imager for my own imagers sometimes, I'm going to change the settings on here so that I have my own password that I set already applied. And we could turn on the wireless LAN here, but we can also do that later. And you can also turn on things like remote SSH access and here, and other options too.

So I got this flashed on my MacBook and I'm going to plug it into the Pi again. And like I said, if you have Ethernet, that's a little bit easier, but otherwise you need another computer to flash the microSD card. So I plugged that in and I'm going to press the power button and the Pi turns on and we should see it boot up over here.

---

### Step 13 `[12:52]`

And the first time the Pi boots up on a fresh OS, it actually reboots a couple times because it has to expand to fill the file system. And sometimes I don't know why, but it reboots like three times. This time it looks like it's going to do it twice.

And this is POS. Now the desktop, this is running a version of Linux, but this is a kind of a custom skin of Linux that Raspberry Pi maintains. So it has a built-in menu bar with the little menu with all the options in it.

---

### Step 14 `[13:19]`

It has a built-in web browser, file manager, and terminal. And then over here there's WiFi settings, Bluetooth settings, sound settings. And so this monitor has speakers built in, so it

---

### Step 15 `[13:31]`

should also give a sound. And we'll test that. But the first thing I like to do when I set up a new Pi with a new microSD card is test to make sure that SD card is fast enough.

And Raspberry Pi actually includes this Raspberry Pi diagnostics tool to help with that. So the SD card speed test will check to make sure that this SD card is fast enough to run POS little. And it's always a good idea to check that because some microSD cards are made a lot better than others.

And if you have one that's really slow, it's going to make your whole experience using a Raspberry Pi not very fun. And it says it passed, which means that it meets Raspberry Pi standards. But you can look into the logs and see how fast it is.

This one is actually a pretty good card. Micro Center does a good job with their microSD cards. Good job to them.

The other thing that I want to make sure is working is the sound. So I'm going to close this and we'll connect to a WiFi network here.

---

### Step 16 `[14:26]`

The first time we do this, it's going to ask me what country I'm in. There it is, United States. It's like I have an IP address.

So I'm going to check and see if YouTube works. It's also a good test for the performance of a Raspberry Pi run. Other single-board computer.

Some of them can't really run YouTube at 1080p or at 720p. So we're going to go to YouTube. And I'll pick one of my videos and we'll see if the sound comes through.

The Pi hasn't updated its date in time yet. So the date was not setting because the WiFi here was a little bit interesting. I think they're blocking some of the servers that it was going to use.

---

### Step 17 `[15:06]`

So now we have the internet working finally. And I'm going to go to my YouTube channel and see if sound works. So it has sound.

The sound is nothing to write home about on this monitor. So if you're buying this monitor for its speakers, maybe buy some external speakers. But it does work.

So the the Pi has a few options for sound. You can go through HDMI. You can use USB audio device.

Some hats provide even better sound. But this video is not about seeing how good it is at

---

### Step 18 `[15:34]`

playing YouTube. It's about doing projects. So the next thing I'm going to do is plug this camera in.

To do that, I'm going to plug it into one of these slots here. However, you want to power off the Pi before you do that because you don't want to power off a camera while it's on or risk shorting something by putting the pin in the wrong place. So let me turn this off.

I'll plug it in and we'll see if we can get the camera up on here. So newer camera modules. Raspberry Pi started including the cable for it.

But if you have an older camera module or old stock, it has the wrong cable for this. So, Micro Center actually sells the right cable for it, which I have right here. And you'll have to do a cable swap on it.

And to do that, you pull very gently on this little black piece here. Slide this out. You can see the contacts are facing the same side as the camera.

And I'll put that in the same way with this orangeish cable and push down on the black part. Like so. And now these contacts go into one of these two ports facing towards the ports on this side.

So the contacts face this way. Plug it in. And we have the camera.

Now I actually got the 3D print back from the back. And here's part of it. Here's the other part.

And oh, when I did that, the Pi booted up. Maybe unplugged the Pi before you do this because you shouldn't really power it on while you're messing around with it too much. But I had them print this case in the back and we should fit right in like this.

That sound is... that doesn't sound wonderful. But it's good enough. So this is my little GoPro stand GoPro tripod.

And I'm going to face the camera

---

### Step 19 `[17:44]`

towards me right next to the Pi. And I'll screw this in. All right, the camera is all connected and it's pointed at me so I'm going to turn it on.

And when it comes up, there's a few different things you can do. You can just make sure the camera's working with RaspiCam. Or you can also download what I'm going to do a remote control web service that you can run on your Pi and you can actually access it from any other computer to see what's going on.

Now that the Pi's camera's plugged in, I want to make sure that it's actually working. So I'm going to say lib camera still

---

### Step 20 `[18:22]`

test T0. And that should open up a window with the camera on it and then it does. There I am.

Hello. And I think autofocus works too. Yeah, so there's my hand.

Now it's on me and we can focus on this. So the camera's working, autofocus is working and that's all good. And I'm going to close out of here by pressing Ctrl C in this window.

And so now we know the camera actually works. I'm going to set up a remote access service so I can access it from other computers on the network. And for that, I'm going to search for Pi camera to web UI.

And this is a project on GitHub made by Monkey Made Me. So thank you very much for making this an open source project that we can use. So I'm going to download the zip file that has the code for this in it.

Net downloads onto the system here. I can expand this and that creates a Python application that will run in the background and share this camera out over the network. So if I go back into the terminal and I follow the

---

### Step 21 `[19:30]`

instructions here, and then I'm going to type in Python app.py. And that loads in some configuration.

---

### Step 22 `[19:41]`

And then from any computer on the same network, I can go to the CRL and visit the Pi camera. And I can do that from here, of course, because I'm on the same network on this on this Pi. And this is the interface.

So you can see it's a little blotchy. That's because I think by default it's trying to do 4K, which 4K is a lot to stream. So I can change that in the setting to go to 1080p, which is a little easier to stream.

And it switches the camera mode. And now you can see, it's not quite real time because it's actually synchronizing the feed through the web UI. And I can access this from my iPad, from my iPhone, or another computer, and remote control it and do time lapses and things.

And this is just one of thousands of different projects you can do with a Pi camera. So the other part of this build is the Enviro Plus air quality monitor. And it uses the Pi's GPIO pins.

There's actually a lot of different ways you can interface with these pins. You can use little Dupont connectors where you plug them into each individual pin. Some people make breakout boards where you can plug things into breadboards on your Raspberry Pi.

A lot of these hats will plug straight into the top of the Pi. However, some hats also have things that stick out of the bottom. And that can also touch things that are on the Pi.

Like if you have a cooler or a big heat sink. And the other problem is that this has a temperature probe on it. And if you have the temperature probe right above the hot CPU, the temperature probe is going to be a little bit off.

So one thing that I do when I'm using these kind of hats is I have an adapter. I use a right angle adapter. And that will let me put this hat off to the side.

And it will still allow me to use another hat on top of the Pi if I want to. So I'm going to put this right here. And stab my finger while I do it because those are sharp.

Just plug it in on the side. Right there. And that lets me have the hat off to the side.

You can also get extension cables for this. There's a lot of different ways you can mount this up. This particular hat actually works a little bit better with the Raspberry Pi 0W or 0W2 because it's the footprints the same.

And that Pi gets a little bit cooler than the Pi 5.

---

### Step 23 `[22:01]`

Now but it will work with any Pi that has GPO. I'm going to do that. And then this hat also has the ability to use a particulate matter sensor.

So if you want to see PM 2.5 or PM 5 or PM 10 different particulate sizes in the air, this sensor lets you do that. And so if you're trying to measure your outdoor air quality or even indoor air quality. So I have this all plugged in.

I'm going to turn on the Pi and hopefully this is the right orientation. Otherwise we could see some magic smoke. So far it hasn't exploded so that's good.

And to get this to work you have to download software from Pymaroni which they provide on their website. And a lot of these projects will have you do things in the terminal. It's really a good skill to have on the Raspberry Pi to know how to use the terminal.

This video is not going to get too deep into that. For many things it gives you the commands to run so you can just run them and it should work. This is what I look like when I spend an hour debugging something on site that worked perfectly in the studio.

On the day of the shoot you ran into some networking issues and well it's just risky doing things live. Which is why I redid the setup back in the studio where I don't have any time pressures. I followed Pymaroni's instructions.

I installed the Enviro Plus software and this time I actually plugged the board in the right way and look at that it works. I can run the example Python scripts they include to do things like check on temperature, see the current light levels or even check on particulate matter after I plug in an external sensor. It was reading zero when I started it up but after I gave it a little persuasion with this Hacksmith mini lightsaber it started seeing the tiny particulates in my studio.

There's also an LCD you can control so I ran a few different tests to make sure that worked. All in all this little hat has a ton of features crammed in and since it's all managed through GPIO I can write my own custom software and do whatever I want with it. That is the power of a Raspberry Pi.

But back to North Carolina. It was cool to meet a couple of you there and Microcenter let me give away the whole setup monitor and I'll just sorry about the audio here. So Joshua came up here right as we were finishing up recording would you like to take this kit with the monitor the Raspberry Pi 5 the Enviro Plus camera?

Sure it would be amazing. Have you ever used a Raspberry Pi 4? I have I've got a 3 and I was able to get a 4 before the e-short.

So now we have a 5. Thanks for coming to my person. Thank you.

Right now I'm using a Pi at my studio to learn about radio with RTL SDR. At home I have unrunning Pi hole to make my home internet better. Raspberry Pi has a bunch of tutorials to get you started and of course subscribe here to see all my Pi adventures.

Thanks to Microcenter for sponsoring my trip and thanks especially to Blake from shooting star media for

---

### Step 24 `[24:38]`

helping me film everything today. Until next time I'm Jeff Girling.

---


*Generated by YouTube to Markdown Summarizer*
