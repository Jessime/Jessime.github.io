---
title: "PhD Reflections II (The Middle)"
last_modified_at: 2020-01-12
categories:
  - Blog
tags:
  - Projects
---

## The large center chunk where things start to feel routine

Even though this post covers the largest period of time, it was the most difficult to write about. It's easy for days and weeks to all start to feel the same. Writing this helped me realize that's not really the case.

## 2nd year, Spring Semester (2016)

### Class

My last class for BCB was `STOR 893 Object Oriented Data Analysis`. I was _so excited_ for this class. I didn't know was OODA was, but it sounded rad. Turns out, the entire course was about [PCA](https://en.wikipedia.org/wiki/Principal_component_analysis). Until that class, I'd been under the impression that a downside of PCA was its lack of interpretability. This PI's entire career was built on telling stories about datasets on which he had applied PCA (or some slight variation). The first week or two of lectures were captivating. Past that, however, it lost its appeal for most people, including myself.

### Research

In some programs, classes remain a significant requirement for many years. This was certainly not the case for me. By my second year, and for the rest of my graduate school career, lab was 80-90% of my time. Here's what "research" meant for me.

We'd always start with a hypothesis. For example:

> lncRNAs with higher GC content are more likely to be found in the nucleus.

People say that "80% of data science is cleaning data." Those people are right. It's a lot of work.

This is a bit of a toy example, but we'd have to figure out:

* Which lncRNA transcripts do we want to use?
* Which cell types are we interested in?
* What type of RNAseq do we want to analyze?

I'd do some exploration and settle on a first estimate of the data we wanted. Then, I'd settle in to that month's jupyter notebook and start hacking away. Unsurprisingly, I have a lot of thoughts about the right way to use a notebook:

[10 Rules for Falling in Love with Jupyter Notebooks]({% post_url 2019-12-16-notebook_rules %})

Gathering the data would usually take longer than expected. For example, I'd hit some bug halfway through that would cause me to lose like 10% of my data somewhere, or something goofy like that. But I'd eventually have a solid dataset. After that, I'd start applying different algorithms. Should I use regression, or create two classes? If I create GC-rich and AT-rich classes, should I use a t-test to compare means, or would a KS-test comparing distributions be more appropriate? Let's try all three options.

First attempts almost always fail. Continuing the previous example, maybe we think transcript length is a factor we need to consider and I should subsample my classes to normalize the distributions of transcript lengths. Again, this is just a toy example. But it illustrates where this process leads. Now I need to create a view of my dataset, then reapply my algorithms. The process was very cyclical. Maybe on one cycle, we'd realize that we needed to bring in another dataset, to spice things up.

Eventually, we'd find a signal we believed to be real. Usually, we would confirm our signal by coming up with another experiment. "If this signal is real, then biologically, this measurable fact should also occur." If the confirmation checked out, we'd spend a bit of time tweaking things. Maybe there was some way to make the signal-to-noise ratio better. Finally, we'd put effort into visualization. I would create graphs everyday. A general rule I learned from Mauro was: the sooner you visualize your data, the sooner you understand it. But the graphs themselves were "for internal use only" and never provided enough context to tell the whole story. Plot making was also a very iterative process, and could either be frustrating or a nice break, depending on the day.

Here's an algorithm that summarizes what I just described and how we did research:

1. Create a hypothesis
2. Gather a dataset
3. Build a view of the data
4. Apply a number of analyses to the view
5. Come up with a hypothesis about why your analysis failed, and how to correct it.
6. Repeat steps 2-5, bringing in new data as necessary.
7. Eventually, find a signal, or reject the hypothesis.
8. Once a signal is found, tweak the analysis and dataset to increase signal-to-noise.
9. Create a graph that best exemplifies your data's story.

When I write it in a neat list like that, it sounds like that might be achievable in a day or two. Nope. This transpired on the timescale of a month to a semester. There were a couple of times when Mauro and I thought we had a plan that would take a week or two. Nope. Going from 1 to 9 always took at least a month.

That's research.  

## 3rd year, Fall Semester (2016)

Primarily because Mauro wanted to get them over with, I was the first of my cohort to take my Orals. I knocked them out in the beginning of summer. I wish I could say that I also knocked Orals out of the ballpark; that they were as easy as Quals. Sadly, words are hard.

There was never any chance of me failing Orals, that's not how my program operated. My proposal was well written, my slides had a reasonable amount of data, and I knew what I was talking about. That's enough to pass. Nevertheless, I had a short debrief with Mauro after the event. The only sentence I remember was:

> Praveen says we need to work on your speaking skills, and I agree.

Speaking isn't a natural skill for me. Classic STEM stereotype, right? I'd given a decent number of presentations in high school and undergrad, but I still sucked at speaking. In retrospect there were two obvious reasons why:

1. Presentations are deceptively difficult. I was always underprepared.
2. I'd never had a tight feedback loop on a presentation. Even though I had presented before, I had never put myself in a situation where I could realize my mistakes and practice implementing a solution.

It wasn't until my favorite class in grad school that I remedied this shortcoming. TODO LINK

### Failures

The other thing that happened throughout the summer and into early fall was that... **nothing** worked.

Most of these posts focus on the highlights of grad school and my successes. But there were certainly frustrating days. This period was about 100 of them back-to-back. Most of the summer was spent trying to demonstrate that we could find a subset of Xist-like lncRNAs which had an Xist-like effect on epigenetics. It was a straightforward and reasonable hypothesis. Despite trying dozens of different datasets and variations on our primary hypothesis, I never found any signal strong enough to be confident in.

Given the success of my preliminary work, this summer was aggravating. More importantly, it raised a lot of doubt in myself (_We would find something interesting if I were better at statistics_) and my project (_Kmers might be too simple to uncover anything truly insightful_). I'm certain that people with more skill and perseverance than me, working on higher profile and more impactful research than me, have dropped out of PhD programs because they were unfortunate enough to get stuck in this period too long. Luck is an inherent element in these ventures.

Always remember that; _especially_ when things are going well.

### No classes

For the first time since I was four, August rolled around without me starting class. The Fall semester consisted entirely of research. Since full days of research were also how I spent my summers, it wasn't a novel situation. Yet, it felt different psychologically. It felt like routine and stagnation.

My saving grace was that I had a lightbulb moment about my project. The thought was something along the lines of, _"What if, instead of splitting a phenotype into two groups and measuring if lncRNAs within either of those groups are significantly more Xist-like, I try the opposite approach? What if I find the most and least Xist-like lncRNAs and check if they have a distinguishing phenotype?"_ Here's the thing about my "lightbulb moment". At the time, it felt like one more attempt to make something (i.e. anything) work. It wasn't until months later when several separate experiments panned out of this technique that I realized how pivotal this simple inversion was.

I still don't know how much to read into this insight. It makes me wonder, however, how often the "lightbulb thoughts" of our lives are considered mundane at the time. If my life were a movie, there would have been dramatic music playing in the background so I could know that this was a crucial moment. In reality, I had no evidence to support thinking this idea was any better than any of my other recently failed ideas.

Follow up question: if this discrepancy between Hollywood-manufactured expectations (that I'll recognize my own good ideas) and reality is real, does it matter? It most likely does.

### Side projects

My second saving grace was working on side projects. Writing and talking about side projects and the work they involve can be mildly controversial. Personally, I find them enjoyable, they fit into the current rhythm of my life, and they are a great way to learn. But that's me (for now). This section is in no way prescriptive.

My favorite side projects are ones where I recognize a skill deficiency I want to improve and I come up with a fun thing to build within that domain. As I mentioned above, the lack of classes in the Fall and the routine of research made me feel like I was stagnating. Two of the projects I worked on that directly related to skills I wanted to learn were [MazeDay](https://github.com/Jessime/MazeDay2017) and [LunchApp](https://github.com/Jessime/LunchApp).

TODO LINKS

In a sentence, `LunchApp` was my first foray into the web; it taught me how much more difficult programming is when you have to think about a stack of languages and technologies, but also how powerful the web is as a software distribution platform. Similarly, `MazeDay` was the first time I programmed anything while leading a group; I got my first taste of how tricky it is to manage and inspire people, while getting to see what it looks like to build something you couldn't have accomplished alone.

I can't quantify this feeling, but my impression is that these two projects had a huge influence on my career trajectory. First, they gave me experience I never would have gotten if I'd continued focusing on scientific programming. More entertainingly, they were a major source of material during interviews. People love a good story and it was easy to turn these projects into stories while discussing difficult debugging situations or learning architectures like Model-View-Controller.

I wouldn't trade the time I spent on these projects for twice as much time to spent on my main PhD project.  

## 3rd year, Spring Semester (2017)

Research was going well enough at this point that Mauro was convinced we would be able to submit a Nature paper at the beginning of February. Instead, on February 3rd, I got an email that began with:

> Hi Jessime,
>
> Congratulations, you passed level 3 within Google's coding challenge! Keep playing!

### Foobar

This was a pretty crazy moment. I had been spending weekends playing [Google foobar](https://medium.com/magentacodes/things-you-should-know-about-google-foobar-invitation-703a535bf30f). During the week, I was spending every possible moment trying to make figures in `matplotlib`. That meant I had one or two days a week that I could spend learning all about algorithms and data structures.

I don't have much exposure to competitive programming, so I don't know how standard my process was, but this is basically how I went about solving Google's coding problems:

1. Brute force the problem to check for understanding. Submitted code had to run in a certain amount of time which pretty much ensured that you used a reasonable combination data structures and algorithms. But, just to make sure I understood what the problem wanted me to achieve, I'd write some O(n<sup>2</sup>) algorithm that would pass the first couple of test cases before failing the tests meant to ensure code efficiency.
2. Figure out where my first attempts were spending too much time. Usually, it'd be possible to identify some spot in the code that was duplicating work unnecessarily.
3. Read through a bunch of Wikipedia pages to figure out which algorithm or data structure made sense for the problem. This is where my experience possibly differed from other applicants. By this point in grad school, I had casually _come across_ enough CS fundamentals to know which half dozen Wikipedia pages might be relevant to a given problem, but I still had to go through those six, actually _understand_ them, plus decide which to implement. "Oh! This is definitely a dynamic programming problem". "Oh! I need to build a graph and do depth first search!" That kind of thing.
4. Debug. Of course, debugging really occurred throughout the process, but most of the problems contained tiny variations on a core concept like DFS. So, there would always be a stage where you had to figure out edge cases.

Even without the possibility of an internship, the exercise of working through CS basics was a wonderful learning experience.

### Pressure

I already knew this about myself, but the spring semester highlighted how easily motivated I am by pressure and deadlines. Mauro was laser focused on getting our paper out since it would be his lab's first. He had me _almost_ as focused. It's a feat to be as focused as him for any period of time... Anyway, part of what helped highlight the positive effect of Mauro's pressure on me was witnessing and discussing how much it didn't help Megan and David. Megan in particular started needing a different type of management style than Mauro was providing and we spent a lot of lunches talking about it.

People default to attempting to motivate people the same way they would be motivated. One of my aspirations in life is to understand how to identify what drives individuals and learn how I can provide their needed style of encouragement and management.

## 4th year, Fall Semester (2017)

The Spring of 2017 blended into the Summer as we went through a series of journal rejections. Each time we'd send the paper off to a journal, I'd switch gears and try to make progress on "mega communities" (a slightly different project). We had some ideas for a follow-up paper which had potential, but I never had enough time to work on it before we'd have to transition back to polishing the original paper for the next resubmission. A few weeks of not working on something is enough time for me to completely lose my flow.

The beginning of Fall was marked by a fantastic trip up to Washington D.C. with Wes, Sherif and Kimiko (another BCB student, a year below us). We participated in an [NCBI hackathon](https://ncbi-codeathons.github.io/), which was a great way of getting out of our UNC bubble and seeing what other people were working on. While that weekend was memorable, it was also a bit upstaged by a trip to Egypt in September. Laura, Wes, and I went for 10 days to go to Sherif's wedding. It was a lovely adventure. I even curated a [photo album](https://photos.app.goo.gl/a91Y7luMsCGO7wIJ3) afterwards.  

### How to Start a Startup

[Startup UNC](http://startup.unc.edu/index.php/about/) was the best class I've ever taken. I still got research done, but this class is where my brain was this semester.  

TODO LINK

Opportunities like this are the reason I don't think my PhD was a waste despite not going into academia. Did I learn and grow during my PhD? Absolutely. Did I learn and grow more than I would have in industry? Who knows. Could I have taken a class like this in industry? Absolutely not.

Well, maybe if I got into YC.

### Peter

I was co-mentored by Peter Mucha, an applied mathematics professor who liked telling stories using networks. It's how he made his living. While Peter made a number of superb technical contributions to my work over the years, listening to him and Mauro chat was my favorite part of our dynamic.

I've talked to graduate students who had problems with their PIs because sometime the PIs would text them too much about non-work related topics. I have trouble imagining that. Mauro made sure to keep his relationship with his students as professional as humanly possible. Peter though was a gregarious guy and any meeting the three of us had together involved a decent bit of chatting. It wouldn't be an exaggeration to say that 80% of the personal things Mauro and I knew about each other were mediated by the 0.1% of my time in grad school spent in Peter's office. And yes, Peter did catch on to this dynamic and jokingly call us out on it.  

One general take away here is how wildly different PIs are. This isn't an insightful comment in and of itself. Humans are wildly different along many different axes. Anyone who's starting graduate school, however, should strongly consider weighting their potential PI's personality as their most important factor for joining a lab.

I don't know of any factor more correlated with a student's success in graduate school than a good working relationship with their PI.
