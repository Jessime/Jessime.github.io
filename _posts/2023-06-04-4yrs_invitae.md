---
title: "Four Years of Invitae"
last_modified_at: 2023-06-04
categories:
  - Blog
tags:
  - Work
---

This was my last week at Invitae after four years there. It was my first industry role, and fully qualified as a "journey". Because I'm continuing to experiment with  ChatGPT, I decided to reflect on my time at Invitae in a mock interview. 

__Note:__ Ignore ChatGPT's gratuitous comments before each question.


**Jessime:**

I want you to act as a reporter. I’m someone who just left a job of four years in the biotech industry. It’s your job to ask me questions about my time in the role. Try to only ask one or two questions at a time. 

------------------

**ChatGPT:**

Absolutely, let's dive into it. To start, could you tell me about the key responsibilities you had in your role? Additionally, what was the most significant project you worked on during your tenure?


------------------

**Jessime:**

I had three main roles while I was at Invitae. 

In my first role, I was a pipeline engineer who helped build our non-invasive prenatal screen (NIPS) product. This was mainly individual contributor work, and wrote the code that plugged the NIPS pipeline into the rest of the Invitae ecosystem. I also contributed to some portions of the variant caller, which felt impactful. 

Second, I was the head of the Systems Engineering Guild (SEG). The tagline I came up with was, “getting the right people the right information at the right time”. I’ve written about the SEG elsewhere, but it was a great opportunity for me to steer the high-level architecture of our bioinformatics platform. The role also gave me the freedom to learn significantly more about other teams and other systems at Invitae than I otherwise would have. 

And finally, I was the Bioinformatics Tech Lead for Invitae’s Modernize Exome project, which at the time was one of Invitae’s top priorities. I led a team of ~6-8 bioinformaticians (as part of a group of ~30-50 people total) transitioned our Exome product from Hyb Capture to PCR-free Whole Genome. We revamped the entire assay from the ground up. 

------------------

**ChatGPT:**

That's a remarkable set of roles and accomplishments. Could you share some challenges you faced while transitioning Invitae's Exome product from Hyb Capture to PCR-free Whole Genome, and how you and your team overcame them? Also, how did your experience with the Systems Engineering Guild help you in your leadership role for the Modernize Exome project?


------------------

**Jessime:**

The first challenge we faced was the most important: hiring. I had the chance to hire four of the members of my team. My lead and I spent many hours discussing our philosophy on hiring, and many more hours interviewing and recruiting. We ended up with a truly all star cast, who helped us overcome the rest of our issues over the next couple years. 

Other problems we ran into were fairly standard. We ran into walls with legacy systems, and had to have thoughtful debates about what tech debt to add and what to address. We were also up against aggressive timelines from management, and a lot of work went into keeping scope sane. 

One fun and unique technical hurdle we ran into was that our product needed to be able to handle saliva and buccal samples. It wasn’t until fairly late in the game that we realized that small regions of homology between the bacterial and human genomes were causing bacteria reads to stick around in our aligned BAM files. The speed at which we came up with a pipeline that could detect and mask these reads was one of the most impressive things I’ve ever been a part of. Not only was the fix done quickly, but it worked beautifully. 

We also faced multiple rounds of layoffs. The smallest of these was still a major distraction and hit to moral. And the largest dismantled the team entirely. 

And I absolutely wouldn’t have been able to lead the Exome project as well without my SEG experience. It gave me the ability to keep a comprehensive view of the entire scope of work, which was helpful for judging timelines, for distributing tasks, and keeping stakeholders informed. 

------------------

**ChatGPT:**

Sounds like you faced some intense challenges but managed to navigate them successfully. Can you elaborate on your philosophy on hiring that you mentioned, and how did it contribute to building an effective team for the Modernize Exome project? Furthermore, how did you and your team maintain morale and productivity during periods of layoffs and organizational uncertainty?


------------------

**Jessime:**

Those two questions are intimately linked. 

It’s so tempting to look at the body of work that you need help finishing and hire the first person who’s technically capable of getting that work done. Technical skill and previous experience are certainly necessary above some threshold, but they shouldn’t be your number one priority. The first question I ask myself after an interview is, “will this person make the other people on the team more excited to come to work everyday, or less?” Because that’s how you get force multipliers that make an outsized impact. To be clear, that question isn’t simply code for “is this person cool or fun?” The person needs to have a good personality, they need to be curious, and have a reasonable business sense, and not explode or crumble under pressure. Interestingly, this question, at least for me, also covers a large swath of the technical expertise. I’m not going to be excited about working with someone incompetent, even if they’re fun. 

Because we focused so heavily on hiring people who work well in a team, when the pressure was on we were largely able to trust and rely on each other. 

------------------

**ChatGPT:**

That's an insightful approach to building a cohesive team. Could you delve more into how your background as a pipeline engineer influenced your work on the Modernize Exome project? Additionally, what have you learned about balancing immediate business needs with long-term tech debt during your tenure at Invitae?


------------------

**Jessime:**

There's a surprisingly large difference between a bioinformatician and a software engineer. Pipeline engineers tend to sit in the middle, helping the bioinformaticians write production-ready code. While everyone on the team was incredibly skilled in their own domains, I had the most experience writing enterprise software. So I did what I could to teach the team what I knew as we went along.

The second question is tricky, but a good one. I've learned a handful of specific lessons:

* Sometimes business plans pivot dramatically. So it's dangerous to spend time on paying down tech debt if you're not sure you have the support of leadership. 
* A certain amount of tech debt is expected, and healthy. But the interest it costs is real.
* You should save a little capacity to pay down tech debt as you go along (leave things better than how you found them). And you should leave a little capacity for concerted tech-debt repayment efforts.
* Knowing the historical rationale (deadlines, business ambiguity, etc.) behind the current state of the code makes you much more sympathetic.
* Immediate business needs should, generally, take priority

Despite these tidbits, I don't feel like I have a comprehensive scope of the tradeoffs. There's some sweet middle between the two priorities. It's worth making an effort to find that middle, but it's difficult.

------------------

**ChatGPT:**

Your insights on straddling the line between bioinformatics and software engineering, as well as managing tech debt are very informative. As you reflect on your experience, can you share a standout moment or accomplishment that you're particularly proud of during your time at Invitae? Moreover, how has this experience at Invitae shaped your career and professional goals moving forward?


------------------

**Jessime:**

I wish life were more like the movies. It would feel so empowering to have those "standout moments" where everything clicks together, and after a frenzied weekend of coding, have implemented a solution. In reality, difficult problems and complex systems are solved/build incrementally, in installments of frustration and effort. It's only in retrospect that I can look back and be proud of what Invitae has accomplished. And while I was fortunate enough to be part of multiple important product launches, I'm most proud of the relationships I made during my tenure and the reputation I gradually established. I, "was knowledgeable about the company's systems, displayed strong leadership potential, and possessed excellent communication skills", I also, "was proactive in providing well-thought-out advice and guidance to teammates, and was engaged and curious during meetings." That's worth being proud of.

On the theme of relationships, the mentors I had while I was at Invitae are the reason I feel prepared to strike out on my own. I had previously thought I'd want to work at a number of smaller companies before trying my own thing, but people like Josh, Andrea, Saj, Arun, Danielle, Jess, and Shane, helped me make the most of the last four years. An Invitae principle was "freedom with accountability", and each of these leaders embodied that principle. They gave me the leeway to make my own decisions about where to focus my time and energy; I was encouraged to jump into whatever issues I thought were most important and could use my help. They also kept me accountable and honest by challenging me when I needed it, and pushed me by displaying their own investment in our projects. If I'm lucky, I'll have opportunities to work with some of them again. 

------------------

**ChatGPT:**

Your reflection speaks volumes about your dedication and growth during your time at Invitae. What are some key skills or lessons that you've learned from your mentors that you'll be carrying forward? Lastly, as you look to venture on your own, what area or challenge in biotech are you hoping to address or contribute to?


------------------

**Jessime:**

Another phrase that floated around a lot was, "calm is contagious". This one's important to me because it's 1) something I've valued in my leads, 2) I'll need to continue to work on. Sure, it's easy to not sweat the small things. But when something feels urgent and important I can jump to conclusions or rush decisions. Or if the number of important things occurring at once feels overwhelming, I can feel paralyzed by indecision, and spend too long in analysis mode. What's more, I know this stress can be felt by others and benefits nobody. It's something I've already gotten better at, and will continue to improve.

To the final question: I want to work on "what comes after a diagnostic test". I mean that in two ways. First, it turns out that a majority of WES and WGS tests are inconclusive. I want to build the standard of care for families struggling with a rare disease who just received an inconclusive test. Second, receiving a diagnosis isn't the end of the story, only the end of the first chapter. I want to do what I can to turn our knowledge of genomics into novel precision therapies. 

Thanks for all the questions.

------------------

**ChatGPT:**

Your perspective on managing stress and decision-making in high-pressure environments will surely serve you well as you venture out on your own. Your vision to support families navigating inconclusive tests and to use genomics knowledge to develop precision therapies is commendable and needed in the biotech industry.
Thank you for sharing your experience and insights. I wish you all the best in your future endeavors. And, should you need any information or help along the way, I'm here to assist you.

