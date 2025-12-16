# E-Ink Weather Dashboard with a Raspberry Pi

## Video Information

- **Creator:** AKZ Dev
- **Duration:** 0:06:14
- **URL:** [https://www.youtube.com/watch?v=65sda565l9Y](https://www.youtube.com/watch?v=65sda565l9Y)

## Summary

This document provides a structured summary of the tutorial, organized as step-by-step instructions.

---

## Content

### Step 1 `[00:03]`

This is an ink weather dashboard powered by a Raspberry Pi. It displays your location and dates, current weather conditions with key metrics, an hourly weather graph, and a multi-day forecast. The ink display has crisp paper-like visuals, doesn't emit any distracting lights, and is easy to read from all angles.

This project also comes with a web UI to customize the dashboard and schedule automatic updates. If you're new here, this video is part of a series where I build new plugins and features for my ink display. In this video, I'm going to walk you through the design process of building the weather dashboard and how you can build it yourself.

This project uses a 7.3-inch in-key impression from PyMarony and a Raspberry Pi 02W along with an ikea picture frame. For a full tutorial of the hardware and software setup, you can check out my previous video. To pull weather data from the dashboard, I'm using Open Weather Map, which is a service that provides a fee weather API.

In this project, I'm using the one-call API, which has a pay-as-you-go price model, but is free for up to 1000 requests per day, which is way more than what we need. If you want to sign up, you'll need to generate an API key and store it in a .emv file in the project directory. In the code, I'm making three API calls to pull all the necessary data.

The one-call API endpoint accepts a latitude and longitude, a PI key and units of measurements as query parameters, and provides a current weather conditions along with hourly and daily forecasts. The air pollution API accepts the same parameters and

---

### Step 2 `[01:47]`

provides the air quality index. And finally, I'm calling the Geocoding API to get the name of the location from the latitude and longitude. With all the weather data collected, we can move on to building the dashboard.

To visualize the weather data, I define an HTML template and render it in a browser to generate an image. This approach allows for dynamic resizing to support different display sizes and orientations, as well as customizing the layout with CSS. To achieve this,

---

### Step 3 `[02:16]`

I first use the Ginger Templating Engine to populate HTML templates with real weather data at one time. For example, here's a simple Ginger Template that displays a weather icon, the current temperature, and units. The variables are substituted with data from Open Weather Map generating

---

### Step 4 `[02:32]`

the final HTML to render. Next, I use the Chromium browser in Headless Mode to render the HTML and take a screenshot. Chromium is an open-source version of Chrome that comes pre-installed on Raspberry Pi's.

It's lightweight, efficient, and can run without a graphical interface. Here's a sample CLI command that renders an HTML file and captures the screenshot.

---

### Step 5 `[02:55]`

The first argument specifies the HTML file to render and the Headless flag runs Chromium without a graphical interface. The screenshot flag instructs it to take a screenshot and store the image in the specified file. I also provide the window size which sets the dimensions of the rendered

---

### Step 6 `[03:09]`

output, matching the resolution of the ink display. And finally, I provide a few additional flags to optimize the performance and reduce overhead in the Raspberry Pi. When I run the command on our sample HTML file with some CSS styling, this is the resulting image.

With this process in place, we can now define a template for our weather dashboard and easily generate images to display. To build the weather dashboard, I started by updating the web UI with inputs needed for the weather API. Here, I added fields for latitude and longitude which can be set by selecting a location on the map model.

I also included a drop down to select the units of measurements for those of you outside the US who refused to embrace a superior imperial system.

---

### Step 7 `[03:56]`

Next, I built out the rest of the HTML template for the dashboard. For the weather chart, I'm using ChartJS which is a JavaScript library for data visualization. In the graph, I'm plotting the hourly weather forecast with the line chart and the probability

---

### Step 8 `[04:11]`

of precipitation with a bar graph. I then defined the CSS to style the dashboard and added icons for all the weather conditions and different metrics. The final result is a dashboard that dynamically resizes for different resolutions and orientations.

Now, I'm not an HTML or CSS wizard, so this took a while to get it right. But if you've made it this far, consider subscribing and liking the video to support the channel. With everything in place, we can now bring the weather dashboard to life on the ink display.

---

### Step 9 `[05:07]`

Next, I wanted to add some customization options to enhance the look. Back in the UI, I added options to toggle the metrics, weather graph and daily forecast along with the ability to choose a number of days to display. I also introduced style settings like different borders, the margin and pixels, a background color or image option and a text color selection.

With these settings, you can customize a design based on your preferences. You can also schedule automatic updates by adding the weather plugin to a playlist and defining a refresh interval, like every hour or daily at a set time. Overall, I'm really happy about how this weather display turned out.

Thanks for watching this far and if you have any suggestions or feedback, feel free to comment them down below.

---


*Generated by YouTube to Markdown Summarizer*
