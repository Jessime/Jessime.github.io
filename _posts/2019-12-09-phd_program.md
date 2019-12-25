---
title: "PhD Reflections"
last_modified_at: 2019-12-15
categories:
  - Blog
tags:
  - Life
---

I finished my PhD less than a year ago.

Now is the perfect time to spend a few days thinking over what I did and learned in the last five years. Originally, I wanted to title this post something along the lines of "What getting a PhD is like". That's a preposterous title. PhD programs vary wildly by both discipline and school. Even within my own cohort, our journeys seemed marked more by their _dis_-similarities. Even this version of my own story is  different than what it would have been if I had written these notes in real time.

Instead, here are some things I remember about graduate school.

The rest of this post is broken down into events on a per-semester basis (it's a good way to make sure I don't skip over those middle chunks). The purpose of each anecdote is reflect some value I extracted out of my time as a PhD student. Overall, I had a great time in graduate school, and generally feel like I learned a lot. Most students don't say that. They'll likely tell you it was [depressing and anxiety inducing](https://www.insidehighered.com/news/2018/03/06/new-study-says-graduate-students-mental-health-crisis). Perhaps some of these details will shed light on what made my experience a net positive.

## 1st year, Fall Semester (2014)

I have a disproportionate number of memories from this semester, because everything was new. Besides starting graduate school, I had just gotten married, and moved from Kentucky to North Carolina. My wife and I decided to get a dog. I mention this because neither I nor graduate school are good at separating work and life. They're the same thing. This fact is reflected in my writing.

One of the cool things about graduate school is that you start with a cohort. It's like getting handed free friends. They're a group of people of similar ages, who have similar interests, and few of them have outside obligations because they're also starting something new. Then, you're all forced to go on this adventure together. There's nothing better for building strong friendships than a good adventure.

An amusing observation I made within the first few weeks of school that still sticks with me is that all of the graduate students (myself included, I'm sure) we're trying to figure out where they ranked in the intelligence/success/social hierarchy. Nothing surprising there, all groups of people do that. What made it amusing was, there seemed to be a large amount of confusion about exactly _how_ to do the ranking. In undergrad and high school, class difficulties and grades were a solid heuristic. And it probably goes without saying that grades were something graduate students cared about a lot. All of that was taken away. Instead, it manifested itself in silly conversations like, "Have you found your rotation PI yet? Oh, me? Yea, I signed last week. I got my first choice! Pretty exciting, right?!"

I mention this observation not only because it was one of my first, but because it became even more relevant over the next few years, not less. To stereotype, graduate students are fiercely competitive people. In many ways, a PhD is a terrible place for competing:

1. There's a lot of competition. People are good.
2. More importantly, there are few clear measurements of success, especially since everyone has slightly different priorities than you.
3. The solid benchmarks, like passing orals and having a paper accepted can be years apart. There are no weekly quizzes to get 100s on.

I wonder what fraction of grad student anxiety is driven by people who have been able to rely on grades for validation their entire life abruptly living in a world where it's fairly unclear how successful you are.

### Rotations

As I alluded to already, my program had us do rotations. We had to pair with three PIs over the course of our first year, and spend about three months working in their lab. At the end of our first year, we would join one of those three labs. I began my rotations with Tim Elston for a few reasons. First and foremost, Tim seemed like a great guy to know on a professional and personal level. I'm not going to belabor the point here (but will elsewhere), but people make or break everything. Second, I really wanted to do something like [whole cell modeling](cell.com/action/showPdf?pii=S0092-8674%2812%2900776-3), and Tim was doing some really interesting systems biology. Third, if I'm being really honest, was that even though I had joined the bioinformatics curriculum I was nervous about joining a purely computational lab. On the account that I... you know... basically didn't have any programming experience.

Two things I learned from the Elston lab: the importance of writing things down, and the difficulty of doing both wet and dry lab.

I spent most of the time working with Lior, another graduate student. Lior was smart, serious, and open. And at the risk of oversimplifying, she didn't like grad school that much. We were running delicate microfluidic experiements that would take a long time to set up. And we were using fairly expensive microscopes. In other words, we were working in an environment where mistakes were costly. I did everything I knew to do to minimize the likelihood of making mistakes. When she would show me some procedure, I'd pay close attention, and absorb as much as I could. But I never wrote anything down, because I naturally find it distracting. Fairly quickly though, I tried to replicated a task she'd shown me and I couldn't remember some basic step. New things are hard. I went back to Lior and asked her my question. She said, "You know, I'm not really looking forward to repeating myself a bunch of times. You should take notes when I show you something."

Since then, I've gotten in the habit of scratching out bare bone notes in a non-distracting way during things (meetings, tutorials, etc.), going back as soon as possible afterwards, and fleshing things out. It's not a perfect system, but it's a major improvement. Especially as the scope of my responsibilities increase, I find the benefit of note taking grows proportionately.

I also learned that it's hard to balance a multi-part project like splitting your time between wet- and dry- lab projects. My dream was to collect my own data, and also be able to analyze it. That was a major appeal of the Elston lab and my project. In the end, I spent all of my time collecting data. Many of my colleagues tried to pull off this duality. I estimate that maybe one or two of them managed it well. The price of context switching is high. It's higher than most people account for. By the time you're back from the lab with your data, you've forgotten all of the nitty gritty details of the analysis that turn out to be essential for any real forward progress and insights.

People who can context switch with minimal penalties are magicians.

For my second rotation, I knew I had to take the leap of faith a do a computational project. I rotated with Mauro Calabrese, who I had heard give a compelling talk about lncRNAs. He was a recently hired molecular biologist, who had some preliminary data showing that a simple computational technique might provide insights into lncRNAs. Spoiler alert: these are the opening lines from my PhD defense:

> On November 10th, 2014--which is an easy date for me to remember, because it was my 22nd birthday--I walked into Mauro’s office for the very first time.
We sat down at the little round table in his office and he said,
"I have this idea about kmers."
Over the next hour, he described this idea that:
There is a class of molecules, found in almost every living organism that help form life as we know it.
But, we don't understand how these molecules work, or more importantly, what sort of diseases arise when they malfunction.
He thought it might be possible to write a computer program to describe these molecules in a way no one else had.
By describing the molecules in this new way, we might be able to predict what they do,
and even help other scientist find ways of stopping them from causing disease.

What makes this story a bit crazy is that a couple days after that, Mauro was showing me how to `ssh` into UNC's cluster and `cd` around the filesystem. I _must_ have used a terminal terminal before that, but I can't recall any specific instances. I had taken an Intro to Python class in undergrad, and made a game on my own over the summer, but that was likely all done in IDLE. I was using [Spyder](https://www.spyder-ide.org/) by the time I got to Mauro's lab. This I know for sure, because I still a couple of `.py` files on Google Drive (what's `git`?) that look like:

```python
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 11:39:57 2014

@author: Jessime
"""

nucleo = ["A", "G", "T", "C"]
...
```

That docstring is a hallmark of Spyder.

Mauro had two graduate students, David and Megan. I don't know two other people I would have rather had as lab mates. My initial impression of the two over the first week or so... was that they were probably dating... In retrospect, that was a goofy thought, given that David had a wedding ring on and Megan didn't. But they worked so well together, were so close, and would bicker so much, that I couldn't think of any other explanation. They're Exhibit A for people making or breaking grad school. Even before winter break, I had a pretty good idea I was going to join Mauro's lab.

### Classes

Even though rotations accounted for about 40h/week, they were only half of our responsibilities. Classes weren't as memorable, but they were a lot of work that first semester. My transcript says I took:

* `BBSP 901 RESEARCH IN BBSP`: This covered our rotations.
* `BCB 710 BIOINFORMATICS COLLOQ`: We had a weekly colloquium, which mostly served as a way for PIs to advertise their research. It's where I heard Mauro talk.
* `BBSP 903A RESEARCH IN BBSP - PART I`: "First Year Group" was everyone's favorite thing to complain about. It was basically a year long orientation. A decent amount of busy work was involved, but I generally found it worthwhile. It was a chill time to do things like discuss research ethics.
* `BCB 710 BIOINFO/SEQ ANALYSIS`: Given that a majority of my project was sequence analysis, you might guess that this was my favorite class. You'd be wrong. It was fairly dysfunctional from start to finish. Neither of the two instructors showed up to the final, because they each thought the other was covering it.
* `BCB 716 NEURAL INFO PROC`: Have you ever seen a student fall asleep in class and feel a little embarrassed for them? Now, have you ever seen a student fall asleep in a two student class? I have. I'm going to abstain from going into details, because there's no take home lesson here.
* `BCB 720 INTRO STATISTICAL MODELING`: This class single handedly made up for the lack of rigor of all the other classes. I probably spent 20 hours a week learning stats and `R` the entire semester. In the end it was worth it. Stats is still my weakest subject, but I used variations of what I learned in that class on a weekly basis for the rest of grad school. If you're in any sort of data driven field, take a decent stats course. Take it!

For me, each semester of grad school was easier than the semester before it (with the possible exception of the final semester, which had a lot going on). Between lab and 720, I basically did nothing except grad school. I very quickly fell into a routine of:

1. Go to school from 9:30 to 6:00
2. Go home, eat dinner, hang out with Laura for an hour
3. Start on 720 homework. I'd give up on it around midnight.
4. Write some code for an hour or two in the early AM.

## 1st year, Spring Semester (2015)

One of the things that really paid off for me in grad school was that I spent more time exploring the ecosystem of scientific computing than any other grad student. Mostly, I just thought Python was really cool. But even the more computationally minded students were still coming out of a pure CS background, and there were a lot of tools that existed that none of us knew about. Not until I found them, anyway. To be a total hipster about it, I found out about Jupyter notebooks before they were cool by browsing the [r/Python](https://reddit.com/r/Python). My grad school story would have been fundamentally worse if I hadn't found notebooks.

Not all of my explorations were quite so fruitful. Over winter break, I was exploring the idea of learning C, since some of my Python code was slow. My goal was to write the C equivalent of:

```python
with open('infile.txt') as infile;
    for line in infile:
        print(line)
```

I imagined it would probably be about 6 lines, and run 50x faster. The latter may be true, I never got around to testing it. We were at my wife's house and I was describing this goal to a friend of ours who was doing is undergrad in CS at the time. He chuckled and told me that it was probably going to be more than 6 lines. He kindly explained a number of the implementation details I would need to consider to do what I wanted. I don't recall them all, but I do remember being fully convinced that I wouldn't be learning C that break. Maybe next year.

### Rotations

I spent a month or so of the spring with Mauro, and it was largely unremarkable. I continued working on my kmer project. My spring semester rotation was defined by Brian Kuhlman's lab. I worked on a protein-folding problem using a software program called Rosetta, written in C++. This was the computational experience I had been gunning for, and the protein folding problem is what introduced me to research my sophomore year of high school.

Most of my time was spent working with another grad student named Tim. Tim was a saint. As he patiently watch me fumble my way around the terminal, he explained both the CS and bio as clearly as one could hope for. Plus, he introduced me to as many cool tools as he could without overwhelming me. Tim taught me `git`. He showed me how to use `tmux`. He helped me write my first for-loop in bash. He pointed me to (vim adventures)[https://vim-adventures.com/] so I could stop using `nano`. He didn't even make fun of me when he saw my homebrewed and python-based `tree` script. Though, he did rightly point out that, "If all you have is a hammer, everything is going to look like a nail." I'm sure I could add to this list if I thought more.

There was just one problem with Tim. He and another grad student in the lab, Ryan, were both 5th years. They were going to graduate and start a company together in the coming year. Selfishly, I had to ask myself, "What good does that do me?" Even though I knew that I didn't want to stay in the lab, given that the friends I had made were leaving, my rotation in the Kuhlman lab was a crucial learning experience.

### Classes

Several classes (`RESEARCH IN BBSP`, `BIOINFORMATICS COLLOQ`, and `RESEARCH IN BBSP - PART II`) were the same as first semester. The new ones were:

* `BCB 712 BIOINFO/DATABASES`: The professor for this class was a super chill guy who was married to the mayor of Chapel Hill. My wife and I ran into them at several of my wife's work events. It was always awkward because the professor never remembered who I was despite the fact that I not only took his course, but I also was is TA the next year... Anyway, the class we also super chill. I almost wish it had been more intense; I could use a little more competence in SQL. But, we learned just enough that I have a basic understanding of things like:
  * How to write simple SQL
  * How to design a reasonable multi-table database schema
  * I was really into OOP during this class, so I spent a lot of time thinking about the relationship between real world things, tables, rows, columns, classes, objects, and attributes. This has paid off pretty nicely while using Django's ORM, for example.
* `BCB 715 BIOINFO/MATH MODELING`: This was co-taught by Tim and Jeremy Purvis. 715 was basically systems biology using differential equations, and a little bit of statistical modeling. In principle, this class should been really interesting. In practice, the material _was_ interesting, but largely overshadowed by trying to figure out what the hell was going on with Matlab. Whenever I finally got programs working, I always found an immense sense of satisfaction from watching whatever toy system evolve over time. Thankfully, I wasn't the only one who struggled with Matlab though. This was when I really became friends with Wes and Sherif. Not that they were any real help with Matlab, but the pain was a lasting bonding experience. Five years later, we still joke about how mad Wes was about the final homework assignment.
* `BCB 717 STRUCTURAL BIOINFO`: This class was taught by Kuhlman the same time I was rotating, and focused on demonstrating principles of structural bioinformatics using PyRosetta, which was/is a janky python wrapper around Rosetta. This was the first and last time I felt like an expert in a class. Others certainly didn't feel the same, since this was the birthplace of the How To Learn to Code summer course that I ended up teaching each summer.
* `BCB 722 TOPICS IN POPULATION GENETICS`: Pedagogically, Praveen made this the best class of the semester. He was one of the few PIs who cared as much about instruction as he did research. One of the things he focused on most was teaching from a first-principles approach. "Given these three basic assumptions, let's see if we can calculate this value you've always been told to memorize." It would have been amazing to have him in a class I personally had more use for, like Sequence Analysis.
* `BCB 725 INTRO TO STATISTICAL GENETICS`: I remember so little about this class that I'm genuinely unsure who the instructor(s) was/were.

Overall, first year classes were neither a waste of time, nor overly useful. They seemed to have been structured around the philosophy that Bioinformatics is at the cross-section of many fields, therefore, each student should at least _know that these subjects exist_. 80% of the students will never use SQL again, but the 20% that do will at least know enough to start reading tutorials they find on Google. The curriculum writers set a low, but reasonable bar.

## 2nd year, Fall Semester (2015)

The main event of the summer was Written Qualifying Exams (Quals). Every program has their own structure for Quals. Ours was that you had four days to answer four of six questions. Each question was basically an exam from one of the BCB modules we had taken over the last year. I had an entertaining incident where my hot water heater broke at the beginning of the four days, but overall, Quals did not live up to the hype. Sure, you had to work on them for eight hours a day for four days; but there was no real chance of failing.

### NSF GRFP

Writing the NSF was fun. I believe I'd say that even if I didn't get it, but it was also a massive amount of work. Two things made it fun. The first was that I got to work closely with Mauro on it. He's one of the few people I'd readily admit is a better writer than I am; and we work well together. The second is that I found a writing process that works for me. I started to describe the process as part of this post, but it turns out that I have a lot of thoughts on the matter, and it deserves its own space:

[A Method for Writing Persuasively]({% post_url 2019-12-15-writing-persuasively %})

This process is a lot of effort, so I only use it for high stakes things like grants or pitches. As I mentioned previously, I'd spend a few hours each night working something. That semester my nights were NSF. Once I had a solid working draft, I'd send Mauro my edits once every few days. He would have edits back to me before I woke up in the morning. The first thing I'd do when I woke up was read the latest round of edit, and let them sit in the back of my mind while I went about my day. By the time I sat down in the evening, I'd have a pretty good idea how I wanted to start addressing them. By the end of the semester, I felt like it was probably the best thing I've ever written. A paper and a thesis later, I still feel that way.

### Class

I only took one class this semester, `COMP 790 Machine Learning`. Both the class and the professor were fast-paced and intense. While I admittedly couldn't keep pace with some of the later mathematics, having a chance to think about machine learning from the ground up was a solid balance to the ML hype that was happening at the time. We started with linear regression and worked our way up from there.

I managed to track down my [final report](https://drive.google.com/open?id=0B0vJr0M-2sGXOHBIWFhsWXVNcTBNZmFHa2x4eGxmdzVGY09Z). If you skim quickly enough, it looks like I'm doing math.  

## 2nd year, Spring Semester (2016)

### Class

My last class for BCB was `STOR 893 Object Oriented Data Analysis`. I was _so excited_ for this class. I didn't know was OODA was, but it sounded rad. Turns out, the entire class was about [PCA](https://en.wikipedia.org/wiki/Principal_component_analysis). Up until that point, I'd been under the impression that one of the downsides of PCA was that it wasn't particularly interpretable. This PI's entire career was telling stories about datasets he had done PCA (or some slight variation) on. The first week or two of lectures were captivating. Past that, however, it lost its appeal for most people, including myself.

### Research

In some programs, classes remain a significant requirement for many years. This was not the case for me. By my second year, and for the rest of my graduate school career, lab was 80-90% of my time. Here's what "research" meant for me.

We'd always start with a hypothesis. For example:

> lncRNAs with higher GC content are more likely to be found in the nucleus.

People say that "80% of data science is cleaning data." Those people are right. It's a lot of work.

This is a bit of a toy example, but we'd have to figure out:

* Which lncRNA transcripts do we want to use?
* Which cell types are we interested in?
* What type of RNAseq do we want to analyze?

I'd do some exploration and settle on a first estimate of the data we wanted. Then, I'd settle in to that month's jupyter notebook and start hacking away. Unsurprisingly, I have a lot of thoughts about the right way to use a notebook:

[10 Rules for Falling in Love with Jupyter Notebooks]({% post_url 2019-12-16-notebook-rules %})

Gathering the data would usually take longer than expected. I'd hit some bug half way through that'd cause me to lose like 10% of my data somewhere, or something goofy like that. But I'd eventually have a solid dataset. After that, I'd start applying different algorithms. Should I use regression, or create two classes? If I create GC-rich and AT-rich classes, should I use a t-test to compare means, or would a KS-test comparing distributions be more appropriate? Let's try all three options.

First attempts always fail. Maybe in this example, we think that transcript length is a factor we need to consider, and I should subsample my classes so that the distributions of transcript lengths are approximately equal. Again, this is just a toy example. But you can see where this leads. I now need to create a view on my dataset, then reapply my algorithms. The process was very cyclical. Maybe on one cycle, we'd realize that we needed to bring in another dataset, to spice things up.

Eventually, we'd find a signal we believed to be real. Usually, we would confirm our signal by coming up with another experiment. "If this signal is real, then biologically, this measurable fact should also occur." If the confirmation checked out, we'd spend a bit of time tweaking things. Maybe there was some way to make the signal to noise ratio better. Finally, we'd put effort into visualization. I would make graphs everyday. A general rule I learned from Mauro was that the sooner you visualized your data, the sooner you understood it. But the graphs themselves were "in-house" and never provided enough context to tell the whole story. Plot making was also a very iterative process, and could either be frustrating or a nice break, depending on the day.

Here's an algorithm that summarizes what I just said and how we did research:

1. Create a hypothesis
2. Gather a dataset
3. Build a view on the data
4. Apply a number of analyses to the view
5. Come up with a hypothesis about why your analysis failed, and how to correct it.
6. Repeat 2-5, bringing in new data as necessary. Eventually, find a signal, or reject the hypothesis.
7. Once a signal is found, tweak the analysis and dataset to increase signal to noise.
8. Create a graph that best exemplifies your data's story.

When I write it in a neat list like that, it sounds like that might be achievable in a day or two. Nope. This is on the timescale of a month to a semester. There were a couple of times when Mauro and I thought we had a plan that would take a week or two. Nope. Going from 1 to 8 always took at least a month.

That's research.  

## 3rd year, Fall Semester (2016)

Primarily because Mauro wanted to get them over with, I was the first of my cohort to take my Orals. I knocked them out in the beginning of summer. I wish I could say that I also knocked them out of the ballpark; that they were as easy as Quals. Sadly, words are hard.

There was never any chance of me failing Orals, that's not how my program operated. My proposal was well written, my slides had a reasonable amount of data, and I knew what I was talking about. That's enough to pass. Nevertheless, I had a short debrief with Mauro after the event. The only sentence I remember was:

> Praveen says we need to work on your speaking skills, and I agree.

Speaking isn't a natural skill for me. Classic engineer, am I right? I'd given a decent number of presentations in high school and undergrad, but I still sucked at them. In retrospect there were two obvious reasons why:

1. Presentations are deceptively difficult. I was always underprepared.
2. I'd never had a tight feedback loop on a presentation. Even though I had presented before, I had never put myself in a situation where I could realize my mistakes and practice implementing a solution.

It wasn't until my favorite class in grad school that I remedied this shortcoming. LINK

### Failures

The other thing that happened throughout the summer and into early fall was that... **nothing** worked.

Most of this post focuses on the highlights of grad school, and my successes. But there were certainly frustrating days. This period was about 100 of them back-to-back. Most of the summer was spent trying to show that we could find a subset of Xist-like lncRNAs which had a local, Xist-like effect on epigenetics. It was a straightforward and reasonable hypothesis. Despite trying dozens of different datasets and variations on that primary hypothesis, I never found any signal strong enough to be confident in.

Given the success of my preliminary work, this summer was aggravating. More importantly, it raised a lot of doubt in myself (_We would find something interesting if I were better at statistics_) and my project (_Kmers might be too simple to uncover anything truly insightful_). I'm certain that people with more skill and perseverance than me, working on more high-profile and impactful research than me, have dropped out of PhD programs because they were unfortunate enough to get stuck in this period too long. There is certainly an element of luck to these ventures.

Always remember that; _especially_ when things are going well.

### No classes

Fall, the first semester of entirely research. Very mundane, but things start to come together.

Mazeday. This was one of a few side projects I now have on Github. They'll get their own section, but they were critical to my success in a more general sense. They're the way I continued to learn.
* How do you make a webapp?
* How do you program in a team?
*

## 3rd year, Spring Semester (2017)


Let's submit this month!

## 4th year, Fall Semester (2017)

NCBI hackathon.
Startup class. Also mostly falls outside of the scope of this, and should get its own post.

## 4th year, Spring Semester (2018)

Edits on the paper

## 5th year, Fall Semester (2018)

Summer at Google. Feeling "done" for the first time.

## 5th year, Spring Semester (2019)

Thesis writing, dissertation prep, and job hunting.
