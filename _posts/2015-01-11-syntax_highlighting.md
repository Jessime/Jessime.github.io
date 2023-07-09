---
title: "Syntax Highlighting"
last_modified_at: 2015-01-11
categories:
  - Blog
tags:
  - "Old Blogger"
---
I had to follow a few different explanations on how to employ syntax highlighting on Blogger before I found a set of instructions that worked. In case anyone else is interested in posting some code onto their site, I would highly recommend checking out <a href="http://oneqonea.blogspot.com/2012/04/how-do-i-add-syntax-highlighting-to-my.html">this blog</a>, which has a nice visual walk through and the necessary code available. It only took me a few minutes to set up. Below are a couple of brief examples (including the one on the post) of what the highlighting looks like.

<pre class="brush:php;">&lt;?php
$example = range(0, 9);
foreach ($example as $value)
{
 echo $value;
}
</pre>
<pre class="brush:python;">#Here are some examples of syntax highlighting
"""This is a doc string."""
def Example(name):
    for i in range(4):
        print "Hello, %s!" %name

Example("Dan")
</pre>