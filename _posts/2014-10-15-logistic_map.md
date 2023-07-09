---
title: "Logistic Map"
last_modified_at: 2014-10-15
categories:
  - Blog
tags:
  - "Old Blogger"
---
<link href="http://alexgorbatchev.com/pub/sh/current/styles/shCore.css" rel="stylesheet" type="text/css"></link> 
<link href="http://alexgorbatchev.com/pub/sh/current/styles/shThemeDefault.css" rel="stylesheet" type="text/css"></link> 
<script src="http://alexgorbatchev.com/pub/sh/current/scripts/shBrushPython.js" type="text/javascript"></script> 
<script language="javascript"> 
SyntaxHighlighter.config.bloggerMode = true;
SyntaxHighlighter.config.clipboardSwf = 'http://alexgorbatchev.com/pub/sh/current/scripts/clipboard.swf';
SyntaxHighlighter.all();
</script>
<br />
<div class="separator" style="clear: both; text-align: center;">
<object class="BLOG_video_class" contentid="8657c5108ff0b711" height="355" id="BLOG_video-8657c5108ff0b711" width="427"></object></div>
<br />
Been playing around with some of the math functions in Python. I think it's really cool how such a simple formula can create something so complicated. If you're interested, I've documented the code I used to make the video (apologies for the lack of syntax highlighting at the moment):
<br />
<br />
<br />
import numpy as np<br />
from matplotlib import pyplot as plt<br />
from matplotlib import animation<br />
<br />
# Set up the figure, the axis, and the plot element<br />
fig = plt.figure()<br />
ax = plt.axes(xlim=(0, 60), ylim=(0, 1))<br />
line, = ax.plot([], [], lw=1)<br />
<br />
# initialization function: plot the background of each frame<br />
def init():<br />
&nbsp; &nbsp; line.set_data([], [])<br />
&nbsp; &nbsp; return line,<br />
<br />
# animation function. This is called sequentially<br />
def animate(r):<br />
&nbsp; &nbsp; n = np.arange(0,60,1)<br />
&nbsp; &nbsp; x_n = .5 #initial value for x<br />
&nbsp; &nbsp; x_list = [] #initiate list<br />
<br />
&nbsp; &nbsp; for i in n:<br />
&nbsp; &nbsp; &nbsp; &nbsp; if i == 0:<br />
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; x_list.append(x_n) #initial value for x<br />
&nbsp; &nbsp; &nbsp; &nbsp; else:<br />
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; x_n1 = r*x_n*(1-x_n) #logisitic equation (the magic)<br />
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; x_list.append(x_n1) #add to x<br />
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; x_n = x_n1 #new x becomes old x<br />
&nbsp; &nbsp; x = np.array(x_list) #turn list into numpy array<br />
&nbsp; &nbsp; line.set_data(n, x)<br />
&nbsp; &nbsp; return line,<br />
<br />
# specify array of parameter values<br />
r = np.arange(2,4.5,.01)<br />
<br />
# animate, save, show plot<br />
anim = animation.FuncAnimation(fig, animate, init_func=init,<br />
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;frames=r, interval=60, blit=True)<br />
#anim.save('log_map2.mp4') #use default ffmpeg<br />
plt.show()