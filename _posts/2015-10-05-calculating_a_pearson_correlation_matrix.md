---
title: "Calculating a Pearson Correlation Matrix"
last_modified_at: 2015-10-05
categories:
  - Blog
tags:
  - "Old Blogger"
---
&nbsp; &nbsp; &nbsp;One of the great things about graduate school is you get to constantly realize how ignorant you are about how things work. If the domain name weren't already taken, I would think about moving my stuff over to&nbsp;<a href="http://seriously.dontusethiscode.com/" target="_blank">seriously.dontusethiscode.com</a>. It can get a bit depressing thinking about all the stuff there is to know. But if you think about it a bit more, it's really just awesome how exciting our world is. I'm glad I've got this opportunity to learn and explore.<br />
<br />
&nbsp; &nbsp; &nbsp;Anyway, I found a question on&nbsp;<a href="https://www.reddit.com/r/Python/comments/3nbkxa/numpy_best_way_to_speed_up_iteration/" target="_blank">reddit</a>&nbsp;that reminded me of a post I did a while ago. One of the key points of '<a href="http://what-is-bioinformatics.blogspot.com/2015/01/simple-sequence-similarity_15.html" target="_blank">Simple Sequence Similarity</a>' was calculating a Pearson correlation matrix. While I realize that it isn't exactly the same as the problem on the reddit link, the nested iteration made me realize that I should probably show some improved code that I currently use to calculate the correlation matrix. By "improved", I mean ~500x faster.<br />
<br />
Here's a <a href="https://gist.github.com/Jessime/f9320f3e262ae31c1d92" target="_blank">link to the&nbsp;notebook</a>.<br />
<br />
As a fun bonus (which I won't dive into right now) there are at least four different examples of <a href="https://ipython.org/ipython-doc/dev/interactive/tutorial.html" target="_blank">Ipython magic</a>&nbsp;throughout the notebook.&nbsp;As always, I welcome any comments or suggestions!<br />
<br />
Cheers!