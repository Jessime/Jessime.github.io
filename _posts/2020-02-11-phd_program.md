---
title: "PhD Reflections I (The Start)"
last_modified_at: 2019-12-15
categories:
  - Blog
tags:
  - Life
  - Grad School
---

## Starting a PhD in Bioinformatics at UNC-Chapel Hill

I finished my PhD less than a year ago.

Now's a perfect time to reflect on what I did and what I learned in those five years. I briefly considered titling this post something like "What getting a PhD is like". That's a preposterous title. PhD programs vary wildly by both discipline and university. Even between the individuals of my own cohort, our journeys seemed marked primarily by their _dis_-similarities. Even this version of my story is different from what it would have been if I had written these notes in real time.

Instead, these posts simply chronicle some of the moments I recall most vividly about graduate school.

The posts are sectioned into events on a per-semester basis (it's a good way to make sure those middle chunks aren't neglected). Each anecdote's purpose is to exemplify some value or capture some observation from my time as a PhD student. Overall, I had a great time in graduate school and generally feel like I learned a lot. Most students don't say that. They'll more likely tell you it was [depressing and anxiety-inducing](https://www.insidehighered.com/news/2018/03/06/new-study-says-graduate-students-mental-health-crisis). Hopefully, writing down these anecdotes and thoughts will help me clarify what made my experience a net positive.

Finally, five years is a long time. Links are sprinkled throughout the semesters as I ran into topics that deserved their own spaces.

## 1st year, Fall Semester (2014)

Because everything was new, I have a disproportionate number of memories from this semester. Besides starting graduate school, I had just gotten married and moved from Kentucky to North Carolina. My wife and I decided to get a dog. I mention this because neither I nor graduate school is good at separating work and life. They're the same thing. This duality is reflected in my stories.

One of the pros of graduate school is that everyone starts with a cohort. It's the closest thing to getting handed friends. The cohort generally includes people of similar ages who have similar interests. Few (if any) of them have outside obligations; they're also starting something new. Then, you're all forced to go on this adventure together. There's nothing better for building strong friendships than a good adventure.

An amusing observation I made in the first few weeks of school was that there seemed to be mass confusion about exactly how to determine the intelligence/success/social hierarchy among all the graduate students. It's hardly shocking that we (myself included, I'm sure) were attempting to "rank" everyone; all groups of people do that. What made it amusing was that nobody knew _how_ to do the ranking. In undergrad and high school, class difficulties and grades were a solid heuristic. It probably goes without saying that grades were something graduate students cared about a lot. Grad school removed all of those metrics. Instead, this ranking process manifested itself in silly, incessant conversations like, "Have you found your rotation PI yet? Oh, me? Yea, I signed last week. I got my first choice! Pretty exciting, right?!"

I mention this observation not only because it was one of my first, but because it became even more relevant over the next few years. To stereotype, graduate students are fiercely competitive people. In many ways, a PhD is a terrible place for competing:

1. There's a lot of competition. The people are top-tier.
2. More importantly, there are few clear measurements of relative success, especially since everyone has slightly different priorities from yours.
3. The solid benchmarks, like passing orals or having a paper accepted, can be years apart. There are no weekly quizzes to get 100s on.

It makes me wonder what percentage of grad student anxiety is driven by people who have relied on explicit heuristics (e.g., grades) for validation abruptly living in a world where it's fairly unclear how successful they are. I think it's high.

### Rotations

As I mentioned already, my program included rotations. We paired with three PIs over our first year and spent about three months working in each lab. At the end of the first year, we joined one of those three labs. I chose Tim Elston's lab as my first rotation for a few reasons. First and foremost, Tim seemed like a great guy to know on a professional and personal level. I'm not going to belabor the point here (though I will elsewhere), but people make or break everything. Second, I really wanted to do something like [whole cell modeling](cell.com/action/showPdf?pii=S0092-8674%2812%2900776-3), and Tim was doing some really interesting systems biology. Third, if I'm being really honest, even though I had joined the bioinformatics curriculum I was nervous about joining a purely computational lab. Since I...you know...didn't have any real computational experience.

Two things I learned from the Elston lab: the importance of writing things down and the difficulty of doing both wet and dry lab.

I spent most of the time working with Lior, another graduate student. Lior was smart, serious, and direct. And, at the risk of oversimplifying, she didn't like grad school that much. We were running delicate microfluidic experiments that would take hours to prepare, plus we were using fairly expensive microscopes. In other words, we were working in an environment where mistakes were costly. I did everything I knew to do to minimize the likelihood of making mistakes. When she would show me some procedure, I'd pay close attention and absorb as much as I could. But I never wrote anything down because I naturally find it distracting. Fairly quickly, though, I tried to replicate a task she'd shown me and couldn't remember some intermediate step. New things are hard. I went back to Lior and asked her my question. She said, "You know, I'm not really looking forward to repeating myself a bunch of times. You should take notes when I show you something."

Since then, I've gotten in the habit of scratching out bare-boned notes in a non-distracting way during meetings, tutorials, etc., going back as soon as possible afterwards, and fleshing things out. It's not a perfect system, but it's a major improvement. Especially as the scope of my responsibilities increases, I find that the benefit of note-taking grows proportionally.

I also learned that it's hard to balance a multi-part project like splitting your time between wet- and dry-lab work. My dream coming out of undergrad was to both collect and analyze my own data. That was a major appeal of rotating in the Elston lab. In the end, I spent all of my time collecting data. Many of my colleagues tried to balance these two types of work. I estimate that maybe one or two of them managed it well. The price of context-switching is high. It's higher than most people account for. By the time you're back from the lab with your data, you've forgotten all of the nitty-gritty details of the analysis that turn out to be essential for any real forward progress or insights.

People who can context-switch with minimal penalties are magicians.

For my second rotation, I decided I had to take a leap of faith and do a computational project. I rotated with Mauro Calabrese, who I had heard give a compelling presentation about lncRNAs. He was a recently appointed molecular biologist who had preliminary data showing that a simple computational technique might provide insights into lncRNA function. Spoiler alert, these are the opening lines from my PhD defense:

> On November 10th, 2014--which is an easy date for me to remember, because it was my 23rd birthday--I walked into Mauro’s office for the very first time.
We sat down at the little round table in his office and he said,
"I have this idea about kmers."
Over the next hour, he described this idea that:
There is a class of molecules, found in almost every living organism, that help form life as we know it.
But, we don't understand how these molecules work, or more importantly, what sort of diseases arise when they malfunction.
He thought it might be possible to write a computer program to describe these molecules in a way no one else had.
By describing the molecules in this new way, we might be able to predict what they do,
and even help other scientists find ways of stopping them from causing disease.

What makes this story a bit crazy is that a couple days after our conversation in the office Mauro was showing me how to `ssh` into UNC's cluster and `cd` around the filesystem. I _must_ have used a terminal before that, but I can't recall any specific instances. I had taken an Intro to Python class in undergrad and made a game on my own over the summer, but that was likely all done in IDLE. I know I was using [Spyder](https://www.spyder-ide.org/) by the time I got to Mauro's lab because I still a couple of `.py` files on Google Drive (because what's `git`?) that begin with:

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

Mauro had two graduate students, David and Megan. I don't know two other people I would have rather had as labmates. My initial impression of the two over the first week or so was...that they were probably dating? In retrospect, that was a goofy thought, given that David had a wedding ring on and Megan didn't. But they worked so well together, were so close, and would bicker so much that I couldn't think of any other explanation. They're Exhibit A for people making or breaking grad school. Even before winter break, which marked the halfway point of the rotation, I had a pretty good idea I was going to join Mauro's lab.

### Classes

Even though rotations required about 40 hrs/wk, they were only half of our responsibilities. Classes weren't as memorable, but they were time-intensive that first semester. My transcript says I took:

* `BBSP 901 RESEARCH IN BBSP`: This covered our rotations.
* `BCB 710 BIOINFORMATICS COLLOQ`: We had a weekly colloquium which mostly served as a way for PIs to advertise their research. It's where I heard Mauro talk.
* `BBSP 903A RESEARCH IN BBSP - PART I`: "First Year Group" was everyone's favorite thing to complain about. It was basically a yearlong orientation. A decent amount of busy work was involved, but I generally found it worthwhile. It was a chill time to do things like discuss research ethics.
* `BCB 710 BIOINFO/SEQ ANALYSIS`: Given that a majority of my project was sequence analysis, you might guess that this was my favorite class. You'd be wrong. The class was fairly dysfunctional from start to finish. Neither of the two instructors showed up to the final, because they each thought the other was covering it.
* `BCB 716 NEURAL INFO PROC`: Have you ever seen a student fall asleep in class and feel a little embarrassed for them? Now, have you ever watched a student fall asleep in a two-student class? I have. I'm going to abstain from going into details, because there's no take-home lesson here.
* `BCB 720 INTRO STATISTICAL MODELING`: This class singlehandedly made up for the lack of rigor of all the other classes. I probably spent 20 hours a week learning stats and `R` the entire semester. In the end, it was worth it. Stats is still my weakest subject, but I used variations of what I learned in `720` on a weekly basis for the rest of grad school. If you're in any sort of data-driven field, take a decent stats course. Take it!

For me, each semester of grad school was easier than the semester before it (with the possible exception of the final semester, which had a lot going on). Between lab and `720`, I basically did nothing except grad school. I very quickly fell into a routine of:

1. Go to school from 9:30 to 6:00.
2. Get home, eat dinner, hang out with Laura for an hour.
3. Start on 720 homework. I'd give up on it around midnight.
4. Write some code for an hour or two in the early AM.

## 1st year, Spring Semester (2015)

Spending more time exploring the ecosystem of scientific computing than any other grad student I knew paid off for me. Mostly, I just thought Python was really cool. Even though there were more computationally minded students, they were coming from a more theoretical CS background, so a lot of software tooling existed that none of us knew about. Not until I found it, anyway. To be a pretentious hipster about it, I found out about Jupyter notebooks before they were cool by browsing the [r/Python](https://reddit.com/r/Python) subreddit. My grad school story would have been fundamentally worse if I hadn't found notebooks.

TODO notebooks

Not all of my explorations were quite so fruitful. Over winter break, I explored the idea of learning C since some of my Python code was slow. My lofty goal to "learn C" was chiseled away until I set my sights on simply writing the C equivalent of:

```python
with open('infile.txt') as infile;
    for line in infile:
        print(line)
```

I imagined it would probably be about the same number of lines and run 50x faster. The latter may be true, but I never got around to testing it. I described this goal to a friend who was doing his undergrad in CS at the time. He chuckled and told me that would take somewhat more effort than Python. He kindly explained a number of the implementation details I would need to consider. I don't recall them all, but I do remember that I couldn't guarantee a maximum line length in my files, which threw us both. I left the conversation fully convinced I wouldn't be learning C that break. Maybe next year.

### Rotations

I spent about a month of the spring semester with Mauro, and it was largely unremarkable. I continued working on my kmer project. My spring was defined by Brian Kuhlman's lab. I joined a protein-folding project, working on/with a program called Rosetta, written in C++. This was the computational experience I had been gunning for (plus the protein folding problem is what introduced me to research during my sophomore year of high school).

I mostly worked alongside another grad student named Tim. Tim was a saint. As he patiently watched me fumble my way around the terminal, he explained both CS and biology as clearly as one could hope. Plus, he introduced me to as many cool tools as he could without overwhelming me. Tim taught me `git`. He showed me how to use `tmux`. He helped me write my first for-loop in `bash`. He pointed me to [vim adventure](https://vim-adventures.com/) so I could stop using `nano`. He didn't even make fun of me when he saw my home-brewed and python-based `tree` script. Though he did rightly point out that, "If all you have is a hammer, everything is going to look like a nail." I'm sure I could add to this list if I thought about it more.

There was just one problem with Tim. He and another grad student in the lab, Ryan, were both 5th years. They were going to graduate and start a company together in the coming year. Selfishly, I had to ask myself, "What good does that do me?" Even though I decided that I didn't want to join the lab, given that the friends I had made were leaving, my rotation in the Kuhlman lab was a crucial learning experience.

### Classes

Basic classes (`RESEARCH IN BBSP`, `BIOINFORMATICS COLLOQ`, and `RESEARCH IN BBSP - PART II`) were the same as first semester. The new ones were:

* `BCB 712 BIOINFO/DATABASES`: The professor for this class was a super chill guy who was married to the mayor of Chapel Hill. Laura and I ran into them at several of my wife's work events. It was always awkward because the professor never remembered who I was despite the fact that I not only took his course but was also his TA the following year... Anyway, the class was also super chill. I wish it had been more intense; I could use a little more competence in SQL. But we learned just enough that I have a basic understanding of things like:
  * How to write simple SQL
  * How to design a reasonable multi-table database schema
  * I was really into OOP during this class, so I spent a lot of time thinking about the relationship between real-world things, tables, rows, columns, classes, objects, and attributes. This has paid off pretty nicely while using Django's ORM, for example.
* `BCB 715 BIOINFO/MATH MODELING`: This was co-taught by Tim Elston and Jeremy Purvis. `715` focused on systems biology using differential equations and finished with a bit of statistical modeling. In principle, this class should have been really interesting. In practice, the material _was_ interesting but largely overshadowed by trying to figure out what the hell was going on with Matlab. Whenever I finally got programs working, I always felt an immense sense of satisfaction from running the code and watching the evolution of the problem's model system over time. Thankfully, I wasn't the only one who struggled with Matlab. Coping with Matlab was when I became friends with Wes and Sherif. Not that they were any real help with Matlab, but the pain was an excellent bonding experience. Five years later, we still joke about how angry Wes was about the final homework assignment.
* `BCB 717 STRUCTURAL BIOINFO`: This class was taught by Kuhlman the same time I was rotating and focused on demonstrating principles of structural bioinformatics using PyRosetta, which was/is a janky python wrapper around Rosetta. This was the first and last time I felt like an expert in a class. Other students certainly didn't feel as comfortable, since this class was the birthplace of the How To Learn to Code summer course that I ended up teaching each summer.
* `BCB 722 TOPICS IN POPULATION GENETICS`: Pedagogically, Praveen Sethupathy made `722` the best class of the semester. He was one of the few PIs who cared as much about instruction as he did research. One of the things he focused on most was teaching from a first-principles approach. "Given these three basic assumptions, let's see if we can calculate this value you've always been told to memorize." It would have been amazing to have him in a class I personally had more use for, like Sequence Analysis.
* `BCB 725 INTRO TO STATISTICAL GENETICS`: I remember so little about this class that I'm genuinely unsure who the instructor(s) was/were.

Overall, first-year classes were neither a waste of time nor overly useful. They seem to have been structured around the philosophy that bioinformatics is at the cross-section of many fields; therefore, each student should at least _know that these subjects exist_. 80% of the students will never use SQL again, but the 20% that do will at least know enough to start reading tutorials they find on Google. The curriculum designers set a low but reasonable bar.

## 2nd year, Fall Semester (2015)

The main event of the summer was Written Qualifying Exams (Quals). Every program has its own structure for Quals. Ours involved four days used to answer four of six questions. Each question was essentially an exam from one of the BCB modules we had taken the previous year. At the beginning of the four days I had a funky incident where my hot water heater broke, resulting in fewer than the necessary number of showers over the exam period, but, overall, Quals did not live up to the hype. Sure, you had to work on them for eight hours a day for four days, but there was no real chance of failing.

### NSF GRFP

Writing the [NSF](https://www.nsfgrfp.org/) was fun. I'd like to believe I'd still say that if I hadn't gotten the award, though it was also a massive amount of work. Two things made it fun. First, I got to work closely with Mauro and my friend Drake on it. They're some of the few people I'd readily admit are better writers than I am (specifically, Mauro along the scientific/rhetorical axes and Drake along the conventional/stylistic axes), and we work well together. Second, I found a writing process that works for me. Like my opinions on usage of Jupyter notebooks, it turns out that I have a lot of thoughts on the matter:

[A Method for Writing Persuasively]({% post_url 2019-12-15-writing_cohesively %})

This process is a lot of effort, so I only use it for high-stakes writing like grants or pitches. My routine throughout grad school included a few hours each night working on _something_. That semester, my nights were NSF. Once I had a solid working draft, I'd send Mauro my edits once every few days. He would have edits back to me before I woke up in the morning. As soon as I'd wake up, I'd read the latest round of edits and let the suggestions sit in the back of my mind while I went about my day. By the time I sat down in the evening, I'd have a pretty good idea how I wanted to start addressing them. Once a week or so, when we had a full set of changes, Drake and I would take a night to hammer out a full round of edits on the current draft. By the final week or two before the deadline, that cadence was increased to almost every night to focus on copy and polish. By the end of the semester, I felt like it was probably the best thing I'd ever written. A paper and a thesis later, I still feel that way.

### Class

I only took one class this semester, `COMP 790 Machine Learning`. Both the class and the professor were fast-paced and intense. While I admittedly couldn't keep pace with some of the later mathematics, having a chance to think about machine learning from the ground up was a solid balance to the ML hype that was happening at the time. We started with linear regression and worked our way up from there.

I managed to track down my [final report](https://drive.google.com/open?id=0B0vJr0M-2sGXOHBIWFhsWXVNcTBNZmFHa2x4eGxmdzVGY09Z). If you skim quickly enough, it looks like I'm doing math.  
