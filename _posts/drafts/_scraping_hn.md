---
title: "Personal Sites from Hacker News User Profiles"
last_modified_at: 2020-01-12
categories:
  - Blog
tags:
  - Projects
---

I was bemoaning the fact that I hadn't done any data science work recently, so I decided to scrape as many Hacker News user profiles as I could, and go from there.

## The project

When I first started my personal site, I was thinking about blogs in general. I've come across a lot of interesting sites on HN so when I also started to feel an itch for a data based project, I decided to combine the two ideas. I finally landed on a TODO step idea:

1. Get a list of all HN users
2. Get all urls from users "about" sections
3. Find all urls that are personal sites
4. Scrape all text from each personal site
5. Create a similarity network between sites
6. Visualize the graph

It's a cool idea, but it turns out step 3 is really hard. There's no full proof way to know if a url is a blog or not without either building an AI, or looking at each site individually.

## Get a list of all HN users

If it turns out the [HN API](https://github.com/HackerNews/API) _does_ have an endpoint that's a list of users, so be it. I missed it. That, obviously, made this step someone more difficult. Thankfully Google BigQuery has archived all of HN and made it [publicly available](https://console.cloud.google.com/marketplace/details/y-combinator/hacker-news?filter=solution-type:dataset&q=hacker%20news&id=5227103e-0eb9-4744-872b-325a8df50bee).

All it took was a single line of SQL to retrieve the data:

``` SQL
SELECT `by`,`timestamp` FROM `bigquery-public-data.hacker_news.full`
```

I added the `timestamp` column just because I wanted to see the date range for the data. Here are some quick stats:
* number of items: 22,472,356
* date of oldest item: 2006-10-09
* date of newest item: 2020-03-03
* number of unique users: 641408

Sadly, I'd forgotten about this dataset until _after_ I'd written a scraper to get users from comment data. Oh well.

## Get all urls from users "about" sections

Scraping all of the "about" sections was projected to take about 30 hours, so I needed a way to persist the data if something happened in the middle. I have minimal experience with databases in general, so I used this opportunity to see if I could set up something with minimal hassle. I happily landed on [dataset](https://dataset.readthedocs.io/en/latest/), which was super easy to stand up and made me feel like I was saving to something in memory (i.e. it was really easy).

Some more stats:
* Users who have a filled out "about" section: 89331
*

## Find all urls that are personal sites

This is a two-step process. First, I had to find all the urls. That part was fairly easy and just required some regex. A few more stats:


Then I had to find all the personal sites. This turned out to be ridiculously time consuming.

It's worth noting that I restricted selection of personal sites to only those written in English. This was done because of the text analysis steps later in the analysis.

## Scrape all text from each personal site
## Create a similarity network between sites
## Visualize the graph
