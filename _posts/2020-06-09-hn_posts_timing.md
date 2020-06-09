---
title: "When are HackerNews Stories Posted?"
last_modified_at: 2020-06-09
categories:
  - Blog
tags:
  - data analysis
  - Marketing
---

## All the time, but mostly at 1600 hours on Tuesdays.

I wanted to get a better sense of when people post stories to HN. Thankfully, the fact that every post ever submitted is available on BigQuery makes this really easy to figure out. My write up is just long enough to cover what I wanted to know. If you're interested in doing your own in-depth analysis, I've uploaded my notebook to this [GitHub Gist](https://gist.github.com/Jessime/ee3f29cc0b73bcc17ad15f38d8dcd270) to get you started.

### Time Series

More than 3.7M stories have been posted to HN since it began in... well, the official launch data was February 19, 2007, but posts go back to November 9, 2006. One other interesting tidbit is that while HN appears to have more or less hit its stride back in 2012, right now is the most active HN has ever been. It's easy to imagine Covid-19 is responsible.

(Click to enlarge)

<figure>
	<a href="https://i.imgur.com/3sFVBf6.png"><img src="https://i.imgur.com/3sFVBf6.png"></a>
</figure>

### Posts by Day of Week

Before looking at the results, I would have guess this graph to reveal the opposite of what it does. Saturday and Sunday seem like the main times to be posting on the internet to me. It makes me wonder what percentage of posts are corporate.

<figure>
	<a href="https://i.imgur.com/x35tCd5.png"><img src="https://i.imgur.com/x35tCd5.png"></a>
</figure>

Or, I wonder how many posts are made by people who are _supposed_ to be working...

### Posts by Hour

This is the meat of what I wanted to get to in this analysis. What time of day do most posts come in?

<figure>
	<a href="https://i.imgur.com/pr0uH1v.png"><img src="https://i.imgur.com/pr0uH1v.png"></a>
</figure>

I suppose the "results" of this graph are open for interpretation depending on your strategy. Do you want to submit when the firehose is strongest and the engagement is highest? Or, would you prefer waiting until those off-hours when things are a little more calm?

Either way, one conclusion that can definitely be drawn is: that curve is very pleasing.
