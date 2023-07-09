---
title: "Using R in a Jupyter/Ipython Notebook with Ubuntu"
last_modified_at: 2016-01-22
categories:
  - Blog
tags:
  - "Old Blogger"
---
I may have mentioned it before, but I love the Jupyter Notebook. It's the only way I come close to keeping my code and analyses organized. I'm not a huge fan of R, mostly because I'm not great at it, but I have to use it sometimes. Today was my third attempt at integrating the R kernel into the Notebook, and it took several hours. I figured it would be worthwhile to chronicle what finally worked, in case I need it later.<br />
<br />
Here's my setup:<br />
<br />
Ubuntu 14.04 LTS<br />
CPython 2.7.11<br />
<div>
IPython 4.0.1</div>
<div>
R version 3.2.3 (2015-12-10)</div>
<div>
<br /></div>
<div>
I have no idea how well these steps would work with any variation in any of these versions. One thing I do know, using R 3.2.x is critical. I was previously using&nbsp;R 3.0.2, which turned out to be the difficulty. 3.0.2 continues to be the default download of R on Ubuntu, so a couple of extra steps are necessary to get 3.2.3 So, if you need to upgrade R:</div>
<div>
<ol>
<li>Open the 'Ubuntu Software Center'.</li>
<li>Edit -&gt; Software Sources.</li>
<li>Click the 'Other Software' tab.</li>
<li>Click the 'Add' button.</li>
<li>Fill in 'deb&nbsp;http://cran.fhcrc.org/bin/linux/ubuntu trusty/'</li>
<li>Click the '+ Add Source' button.&nbsp;</li>
</ol>
<div>
This will allow apt-get to properly upgrade R. You can then go to your terminal:<br />
<br /></div>
</div>
<pre class="brush:bash;">$sudo apt-get update
$sudo apt-get upgrade
$sudo apt-get install r-base r-base-dev
</pre>
<br />
At this point you should have a proper version of R. Next we can start working on kernel dependencies. Also from the terminal, run:<br />
<br />
<pre class="brush:bash;">$sudo apt-get install libzmq3-dev</pre>
<br />
We're almost done. From inside R (using either the terminal or an IDE like RStudio), run:<br />
<br />
<br />
<pre class="language-r"><code>install.packages(c('rzmq','repr','IRkernel','IRdisplay'),
                 repos = c('http://irkernel.github.io/', getOption('repos')),
                 type = 'source')
IRkernel::installspec()
</code></pre>
<br />
And there you go! Things should be up and running now, and you should have the option to create an R notebook:<br />
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://2.bp.blogspot.com/-VpRb5l9I_0k/VqLN1uUSF1I/AAAAAAAACso/JLSiwEeYQUU/s1600/Screenshot%2Bfrom%2B2016-01-22%2B19%253A46%253A24.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="225" src="http://2.bp.blogspot.com/-VpRb5l9I_0k/VqLN1uUSF1I/AAAAAAAACso/JLSiwEeYQUU/s400/Screenshot%2Bfrom%2B2016-01-22%2B19%253A46%253A24.png" width="400" /></a></div>
