---
permalink: /fractal_tree_logo/
title: "Designing the Site's Logo"
header:
  video:
    id: NIOBqBq_tZg
    provider: youtube
---

[Open Graph](https://ogp.me/) is kinda cool, I guess. Open Graph is the technology behind link previews. You know how if you share a link on Facebook (or many other social media sites around the web) a thumbnail and short description of the site is automatically generated and included in your post? That's due to Open Graph.

One problem I've repeatedly run into is that level of zoom on the thumbnail doesn't make much sense. For example, I used to have this photo of myself as the logo:

{% include figure image_path="/assets/images/me_small_square.jpg" alt="A photo of me sitting in a chair" %}

It's a decent photo. When I would post a link, however, certain platforms would zoom in to the very center of the image, which wasn't particularly flattering. I made the joke that I should use a fractal-based image as a logo so that no matter what level of zoom happened it would still be interesting.

I didn't want to just copy something from the internet, though, so I took a few hours and made the image. The header video is the process I used to generate the final image.

The code was pretty simple. It's a combination of `turtle` and `seaborn`. The core fractal code is based on [this](https://codegolf.stackexchange.com/a/18786) code golf submission.

[And here's the jupyter notebook I used to make the artwork.](https://gist.github.com/Jessime/745585c6c478ec89a042f0998f037f14)

Then, I used screen capture to record the turtle animation and sped it up (while making the file size smaller) with:

```
ffmpeg -i Untitled.mov -filter:v "setpts=PTS/20" turtle_tree.mp4
```
