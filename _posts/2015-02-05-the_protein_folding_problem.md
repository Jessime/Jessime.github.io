---
title: "The Protein Folding Problem"
last_modified_at: 2015-02-05
categories:
  - Blog
tags:
  - "Old Blogger"
  - Genomics
---
First, if you've never had the opportunity to visit <a href="http://xkcd.com/">xkcd</a>, I highly suggest you do it. It's a wonderful website. My personal favorite is the <a href="http://what-if.xkcd.com/">What If?</a> feature. Read one of them; you'll like it. The comic relevant to this post is:<br />
<br />
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://3.bp.blogspot.com/-rqORugNMD2g/VNRCv43D_3I/AAAAAAAACdM/fxXGS7ii6Q8/s1600/xkcd_proteins.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://3.bp.blogspot.com/-rqORugNMD2g/VNRCv43D_3I/AAAAAAAACdM/fxXGS7ii6Q8/s1600/xkcd_proteins.png" height="110" width="320" /></a></div>
<br />
If you're unfamiliar with the protein folding problem, let me briefly set the stage. Imagine a protein made of 100 amino acids linked together in a chain. The protein has to figure out where to put each of these amino acids relative to each other, in order to work properly. (As an aside, proteins which fail to fold properly have implications to many horrible <a href="http://en.wikipedia.org/wiki/Proteopathy">diseases</a>.) For simplicity, let's also image that each of the amino acids can take one of 2 positions. This implies that the protein can take 2<sup>100</sup> positions. This may or may not seem like a lot of choices to you. Try putting&nbsp;2<sup>100</sup>&nbsp;into <a href="http://www.wolframalpha.com/">WolframAlpha</a>. It works out to be 1267650600228229401496703205376 different positions, and only one of them is right.<br />
<br />
To think about this number a different way, consider having 100 computers that will each check a trillion of these different possibilities a second. That's pretty good, right? Actually, it's not even close. It's going to take you approximately ~400,000,000 years to be able to look at all possibilities. It's absolutely impossible to fold a protein this way. It's not how nature does it, and it isn't how we attempt to do it either. Instead, the general hypothesis is that as the protein begins to fold into a favorable/proper state, it lowers it's energy, which basically crosses certain possibilities off the list without even having to check. The usual analogy is a <a href="http://www.snipview.com/q/Folding%20funnel">folding funnel</a>:<br />
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://4.bp.blogspot.com/-4GziUpAoLPw/VNRLMIYs_8I/AAAAAAAACdc/P8z2x2IlA08/s1600/blog_funnel.jpg" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://4.bp.blogspot.com/-4GziUpAoLPw/VNRLMIYs_8I/AAAAAAAACdc/P8z2x2IlA08/s1600/blog_funnel.jpg" height="336" width="400" /></a></div>
<br />
<br />
So, while all spaces on the funnel are technically possible, the protein is almost always just going to fall down the funnel. When scientist try to fold proteins, they use this funnel analogy as a method for only checking some of the possible conformations. But they check intelligently, mostly looking at the positions that have a high chance of being the natural shape of the protein.<br />
<br />
The specifics of how to implement such a search on a computer can get as technical as you like. But a teaching tool called <a href="http://www.pyrosetta.org/">PyRosetta</a>&nbsp;has been made that allows students like me (and you?) to get a pretty good idea of whats going on and what tools we have available to us. In my next post I'll show you a very simple script written for class that allows for the folding of a short peptide.<br />
<br />
Until next time, cheers.