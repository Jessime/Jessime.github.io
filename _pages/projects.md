---
title: "Projects"
layout: splash
permalink: /projects/
date: 2020-01-12T11:48:41-04:00
header:
  overlay_color: "#000"
  overlay_filter: "0"
  overlay_image: assets/images/projects_splash.jpg
  actions:
    - label: "Download"
      url: "https://github.com/mmistakes/minimal-mistakes/"
  caption: "Embarcadero Plaza"
excerpt: "The Menagerie"
intro:
  - excerpt: 'Nullam suscipit et nam, tellus velit pellentesque at malesuada, enim eaque. Quis nulla, netus tempor in diam gravida tincidunt, *proin faucibus* voluptate felis id sollicitudin. Centered with `type="center"`'
feature_row:
  - image_path: assets/images/projects_splash.jpg
    alt: "placeholder image 1"
    title: "Placeholder 1"
    excerpt: "This is some sample content that goes here with **Markdown** formatting."
  - image_path: assets/images/projects_splash.jpg
    image_caption: "Image courtesy of [Unsplash](https://unsplash.com/)"
    alt: "placeholder image 2"
    title: "Placeholder 2"
    excerpt: "This is some sample content that goes here with **Markdown** formatting."
    url: "#test-link"
    btn_label: "Read More"
    btn_class: "btn--primary"
  - image_path: assets/images/projects_splash.jpg
    title: "Placeholder 3"
    excerpt: "This is some sample content that goes here with **Markdown** formatting."
feature_row2:
  - image_path: assets/images/lunch_app.jpg
    alt: "LunchApp"
    title: "LunchApp"
    excerpt: 'A web app to help groups make decisions one where to go to lunch. My first web app. (Summer, 2017)'
    url: "#test-link"
    btn_label: "Read More"
    btn_class: "btn--primary"
feature_row1:
  - image_path: assets/images/revenge_start_screen.png
    alt: "The Revenge of Arius"
    title: "The Revenge of Arius"
    excerpt: 'A two player, turn based, tower defense game. My first independent coding project. (Summer, 2014)'
    url: "#test-link"
    btn_label: "Read More"
    btn_class: "btn--primary"
---

{% include feature_row id="intro" type="center" %}

{% include feature_row %}

{% include feature_row id="feature_row2" type="center" %}

{% include feature_row id="feature_row1" type="center" %}
