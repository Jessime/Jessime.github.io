---
title: "Teach Your Fourth Grader Python (Installing Anaconda)"
last_modified_at: 2015-12-28
categories:
  - Blog
tags:
  - "Old Blogger"
  - Code
---
It's really never too early to start teaching your child to code. You may think, "What's the point of teaching my kid to code so long before they have any idea what they want to do with their life?" The topic is worth a post of its own, but here are a couple of articles by <a href="http://www.connectionsacademy.com/blog/posts/2014-12-04/Why-Learning-to-Code-Benefits-Kids-Regardless-of-Future-Career-Choice.aspx" target="_blank">Beth Werrell</a> and <a href="http://www.theguardian.com/technology/2014/feb/07/year-of-code-dan-crow-songkick" target="_blank">Dan Crow</a> that address how useful "computational thinking" is in a world where everything relies on software. Another possible issue that might come to mind is, "How do I teach my child to code when I don't even know how?" Thankfully, there are already some really great resources out there to help you learn and teach at the same time. One of my favorite books is&nbsp;<u><a href="http://inventwithpython.com/chapters/" target="_blank">Invent Your Own Computer Games with Python</a>&nbsp;</u>which is free online. Another resource, which I haven't used at all but generally gets good reviews is&nbsp;<a href="http://www.amazon.com/Teach-Your-Kids-Code-Parent-Friendly/dp/1593276141" style="text-decoration: underline;" target="_blank">Teach Your Kids to Code: A Parent-Friendly Guide to Python Programming</a>.<br />
<div>
<br /></div>
<div>
I had the opportunity earlier this semester to team up with a friend of mine to each a few hours worth of Python to her 4th grade class. Let me point out that this isn't nearly enough time to learn a programming language. It's enough time to see what coding is and complete a small project to get the students interested in coding. In 4th grade kids are still learning/perfecting their multiplication tables, so we decided to make a multiplication 2-player game.&nbsp;</div>
<div>
<br /></div>
<div>
We'll go over two things. First, I'll show you how to easily install Python (it can be a little bit of a challenge on your own). Then, in the next post, I'll present the code that I wrote for class, and describe the basics of what it does. Again, this isn't going to provide enough information for you to "learn how to code". It's a fun first project to show you why learning to code is worthwhile. I would suggest using one of the resources I linked above to figure out all of the details about how the code works.</div>
<div>
<br /></div>
<h2>
Installing Anaconda</h2>
<div>
Anaconda is a version of Python nicely bundled into a convenient package. Here are a list of steps to get up and running&nbsp;</div>
<div>
<br /></div>
<div>
1. Go to&nbsp;<a href="https://www.continuum.io/downloads">https://www.continuum.io/downloads</a>&nbsp;to download the program.&nbsp;</div>
<div>
2. You'll see options for Windows, OSX, and Linux. Choose the one that works for you.</div>
<div>
3. You'll also have the option between Python 2.7 and 3.5. You should choose 3.5 unless you have a very specific reason for choosing 2.7.</div>
<div>
<br /></div>
<div class="separator" style="clear: both; text-align: center;">
<a href="http://2.bp.blogspot.com/-TfGwNSTwwhQ/Vlodx3VT3yI/AAAAAAAACq0/rESKZ7TbpA4/s1600/1-1.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="223" src="http://2.bp.blogspot.com/-TfGwNSTwwhQ/Vlodx3VT3yI/AAAAAAAACq0/rESKZ7TbpA4/s400/1-1.png" width="400" /></a></div>
<div class="separator" style="clear: both; text-align: center;">
<br /></div>
<div class="separator" style="clear: both; text-align: left;">
4. Begin the download by clicking the 3.5 Graphical Installer I've highlighted in the red rectangle above.</div>
<div class="separator" style="clear: both; text-align: left;">
5. Once the download is complete, open the installer.</div>
<div class="separator" style="clear: both; text-align: left;">
<br /></div>
<div class="separator" style="clear: both; text-align: center;">
<a href="http://2.bp.blogspot.com/-VyJyQoOhQxk/VloeYFQENkI/AAAAAAAACq8/TITMn_TVBN4/s1600/2.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="179" src="http://2.bp.blogspot.com/-VyJyQoOhQxk/VloeYFQENkI/AAAAAAAACq8/TITMn_TVBN4/s320/2.png" width="320" /></a></div>
<div class="separator" style="clear: both; text-align: left;">
<br /></div>
<div class="separator" style="clear: both; text-align: left;">
6. Just follow the defaults and walk through the installer.&nbsp;</div>
<div class="separator" style="clear: both; text-align: left;">
7. Agree to the Terms of Service.&nbsp;</div>
<div class="separator" style="clear: both; text-align: left;">
8. Install for Just me.</div>
<div class="separator" style="clear: both; text-align: left;">
9. Accept the default 'Destination Folder'</div>
<div class="separator" style="clear: both; text-align: left;">
10. Click the 'Install' button.</div>
<div>
11. Once the install as been completely finished, search for 'Spyder' in your computer's search. Look for an icon similar to the one below:</div>
<div>
<br /></div>
<div class="separator" style="clear: both; text-align: center;">
<a href="http://2.bp.blogspot.com/-j19DzkSHg20/VlogLgmQIqI/AAAAAAAACrI/pq8nfHLLydw/s1600/spyder.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://2.bp.blogspot.com/-j19DzkSHg20/VlogLgmQIqI/AAAAAAAACrI/pq8nfHLLydw/s1600/spyder.png" /></a></div>
<div class="separator" style="clear: both; text-align: center;">
<br /></div>
<div class="separator" style="clear: both; text-align: left;">
12. Note: Ignore that my icon has Python 2.7, it's what I use because of legacy issues.</div>
<div class="separator" style="clear: both; text-align: left;">
13. Select the icon to launch Spyder. It will take a minute to launch.&nbsp;</div>
<div class="separator" style="clear: both; text-align: left;">
<br /></div>
<div class="separator" style="clear: both; text-align: center;">
<a href="http://2.bp.blogspot.com/-S6sbDrVtihQ/VlohNdiwLwI/AAAAAAAACrQ/un2vxEvzAWk/s1600/spyder2.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="225" src="http://2.bp.blogspot.com/-S6sbDrVtihQ/VlohNdiwLwI/AAAAAAAACrQ/un2vxEvzAWk/s400/spyder2.png" width="400" /></a></div>
<div class="separator" style="clear: both; text-align: center;">
<br /></div>
<div class="separator" style="clear: both; text-align: left;">
14. Congratulations! You're ready to start coding.&nbsp;</div>
<div class="separator" style="clear: both; text-align: left;">
<br /></div>
<div class="separator" style="clear: both; text-align: left;">
In case you're wondering Spyder is what's known as an <a href="https://en.wikipedia.org/wiki/Integrated_development_environment" target="_blank">IDE</a>. At its simplest, it is just a place to write and run your code. If yours doesn't look exactly the same as mine, don't worry. It's going to look different depending on whether you're using Windows, OSX or Linux.&nbsp;</div>
<div class="separator" style="clear: both; text-align: left;">
<br /></div>
<div class="separator" style="clear: both; text-align: left;">
<br /></div>
<div>
<br /></div>
