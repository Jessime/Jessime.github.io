---
title: "A Marketing Retrospective: what the hell?"
last_modified_at: 2020-08-22
categories:
  - Blog
tags:
  - CodeStories
---

I recently finished teaching my first virtual CodeStories class, Intermediate Python for Bioinformatics 2020 (InPyBio-20). The course was eight weeks long and had three main components: 1) group Zoom meetings, twice a week for an hour each, 2) 30-minute 1:1 meetings with each of my four students, once a week, and 3) CodeStories work, which students largely completed on their own time. While I’ve worked on and taught this class over the last five years, this year was quite different. Besides it being virtual, it was the first time the course was paid and the first time I taught it outside the context of teaching graduate students at UNC how to code. Because this course marked an exciting step in CodeStories’s life (this is the first time I’ve sold something to anyone), I figured it’d be worth writing a retrospective.

## How’d it go?

Overall, it went surprisingly well! I haven’t had the opportunity to teach in a few years and had forgotten how much I enjoy education. A large portion of that enjoyment is getting to know the students, so having only four students was a boon as far as my attention was concerned. Besides the class size working out, the students themselves were pretty much perfect.

One of the hardest things to get right as an instructor is setting an appropriate pace given a spread of students with different backgrounds, different capabilities, and different interests. Ideally, one would “teach to the median” so roughly half the class could stand to go a little faster but is still interested, while the other half could use a little more explanation but is still grasping the core concepts. Just before the course began, I was concerned that I had misrepresented the course’s contents and/or pacing in a way that would cause students to drop the course and request a refund. Thankfully, all of the students were at approximately the same level of programming proficiency and experience. Some progressed faster than others, but not unreasonably so.

The individual students also worked well as a group. Everyone was polite, respectful, and eager to learn. Everyone participated in class and contributed to discussions, but nobody was domineering. This may sound like the _de facto_ state of a voluntary graduate-level course, but it certainly hasn’t been my experience in the past. It’s common to get groups where everyone will just wait silently for someone else to answer or to have that one oddball who constantly needs validation and responds to every question.

The course was fun for me, and all the feedback I’ve gotten has indicated that the students found it equally enjoyable and worthwhile.

## Presumably, the fact that CodeStories is self-paced exacerbates the difficulty of teaching to the median?

It definitely does. In the past, while teaching in person, I’d help alleviate the problem by pairing students who were farther ahead with those who were a little behind during group work time. Encouraging the more advanced students to explain their work to others was likely as good a learning experience as solving the original problem. Unfortunately, the technique didn’t work as well with only four students.

This year, I attempted to mitigate the issue by introducing “final projects” four weeks into the eight-week course. The idea was simple: if a student gets too far ahead, they should start working on the final project for a while. Truthfully, I should have thought of this idea a couple months earlier and invested more mental energy into fully realizing it. Even in its half-baked form, the idea of final projects was well-received by the students. And although we spent approximately 90% of the time on ideation and 10% on implementation, everyone (myself included) thought the process of coming up with your own project was time well spent. It gave the students—each in a different way—insights into how they might use their new programming skills for their own needs.

To circle back to “teaching to the median”: next time, I wouldn’t let the CodeStories portion of class be self-paced. Given students’ excitement about personal projects, I’d like to introduce them immediately. The key insight here is that, while CodeStories could be used as the core curriculum, personal projects could absorb variations in students’ backgrounds, capabilities, and interests. Each CodeStories lesson could be roughly targeted toward introducing one or two main concepts a week, similar to the [InPyBio’s curriculum goals](https://mycodestories.com/inter_python_biofx_20/#curriculum). As soon as a student finishes that week’s CodeStories lesson, their attention would shift to their project.

## It seems like personal projects carry their own risk of flying off the wall. How do you avoid that?

There’d need to be significantly more guidance than there was this time around. The start and end points of the projects particularly benefit from coordination.

I should have done a better job at providing project suggestions for students who didn’t have clear project goals. I made some suggestions, but only weakly, for fear of inhibiting creativity. While I certainly achieved my goal of allowing uninhibited creativity, I did so at the expense of considerable time. Given the real constraints of the course, more leadership would have been more useful.

Additionally, as projects are designed and implemented, keeping specific end goals in mind naturally helps provide guidance. Each project should be some sort of “pipeline” for processing biological data. The word “pipeline” is intentionally vague to allow flexibility in design choice but is used to convey that the program should be modular and output results in stages so that students’ success isn’t all-or-nothing in the final week. The programs should accept one or two parameters at each stage, output some interesting result, then use that result for the next stage. Even if a student only builds two stages, I’d consider this a huge success.

Importantly, the program should be steered toward a design that plugs into a web interface. This criterion is critical because the ultimate vision for these projects is that students have a working demo they could share with friends or even potential employers. The instructor would certainly be responsible for both guiding the design and for hooking up the projects to a course site. In practice, these responsibilities should be trivial for the instructor.

## It sounds like you’d change a lot about the personal projects. What else would you change?

I’ve never successfully fostered continuous dialogue and collaboration between students. One of my dreams is that when a student gets stuck they post a question about their problem and other students jump in to help. Personally, I’ve spent a bunch of time on [r/learnpython](https://www.reddit.com/r/learnpython/) and have found answering questions to be as beneficial to my growth as asking them. I want to set up students to have the same experience.

This year, I tried using GitHub Issues. The three main motivators were

1. it’s easy to nicely syntax highlight Python,
2. each question and its resulting discussion natively gets its own thread, and
3. students become a little more familiar with GitHub.

Despite me demonstrating it a couple of times and posting an announcement or two, nobody ever took the bait. I asked why that was during one of my final retros, and a student reported that GitHub was still just too intimidating.

I’d like to try placing everyone in a group chat in an app that everyone has already downloaded and is familiar with. The difficulty is that the app should also contain more technical features like syntax highlighting. Slack likely fits the bill best, as far as I’m aware, but even Slack isn’t ubiquitous.

In short, creating and maintaining a dialog between students where everyone feels comfortable asking questions and sharing thoughts is a simple change with a potentially large return on investment.

## Speaking of retros, did you learn anything else interesting during those interviews?

The feedback was primarily positive, thankfully, but I asked enough variations on “What would you change?” to have a fun list of suggestions. Some of the proposals are actionable; others, not so much. I recorded all of these interviews, which I would highly recommend for anyone gathering user feedback. It allows you to focus on the conversation instead of worrying about notes, which kills the flow. Because I have the recordings, I’ll be able to reference the specific suggestions when I need them later. None of the conversations raised issues that need to be addressed immediately.

The two specific questions (even down to the phrasing) I asked everyone were both financially focused:

1. Who financed the course?
2. Did you think it was worth the arguably high price tag?

The latter question received one “It was kinda pricey,” two “Yes, it was worth it,” and one “Absolutely.” The final response included a happy dance. Here’s a thesis: if 25% of your customer interviews involve happy dances, you’re probably on the right track.

A more controversial thesis is that institutions should be paying for their employees and students to take these sorts of courses. This thesis deserves an essay of its own, so I won’t try to convince anyone here. But I want to clarify that I don’t mean they “should be paying” in the moral or ethical sense. Sure, there’s an argument to be made that companies are morally obligated to take care of their employees, and education falls under that umbrella, but I find that those sorts of arguments lead to more lip service than action. Companies should be paying because it would save them costs and increase revenue by reducing employee churn and generating better employees, respectively. I suspect that, because the loss is difficult to quantify, companies greatly underestimate the institutional knowledge lost when an employee leaves to try something different. Similarly, it’s becoming increasingly clear that universities aren’t particularly well-positioned to train people to be productive members of the workforce. Industry would do well to begin thinking more about investing in its human capital.

Again, there’s much more to say about the theory behind this thesis. Unfortunately, what I learned during my retros was:

1. Three students paid for the course themselves while only one was reimbursed.
2. The three students who paid for themselves didn’t consider asking their employer for various reasons.
3. The student who was reimbursed had no trouble convincing their employer despite what might be considered roadblocks (e.g., lack of course accreditation or certification).

I’d like these numbers to be reversed. >75% of students should have their employers pay for the course. It’s worth explicitly noting that this is a biased viewpoint. My revenue is likely to be higher if individuals don’t have to cover the full price of the course. Critically, however, this isn’t just because companies have a bunch of cash to burn. Companies are the entities most likely to directly see returns on the expenditure, not the students themselves. The students, rather, are most likely to only capture a small portion of their generated value in the form of a raise, assuming they successfully transfer their new skills into utility for the company. In essence, companies are the first-degree beneficiaries of new skill and students are second-degree beneficiaries, connected through the company via salary increases.

## This has mostly been a list of things you would change. What do you want to keep around?

Props to Zoom for making remote teaching surprisingly easy and providing a number of useful features:

*   Sharing screens isn’t unique to Zoom, but it’s unique to remote teaching, and I took full advantage of the students being able to easily share their screens. Using class time to let students drive the programming session was a rich experience for everyone.
*   Breakout rooms weren’t something I used regularly given the size of the class, but I was impressed with how smooth and powerful the feature was when I did use it. It would be an extremely important tool if I had even eight or nine students.
*   Being able to record class was great. A couple of students missed class but were able to make it up. I even had a couple of upload requests from students who had attended a class but wanted to rewatch sections.

None of these features are particularly fancy, but I was encouraged by how intuitive remote teaching felt. There were even aspects that were better than in-person.

## Alright, so what’s the next move?

I don’t want to commit to anything until I take a bit of a breather to mull it over.

While I enjoyed getting to know the students and 1:1 time was a blast, this model is hardly scalable. Can I do something that requires half the time investment and accommodates 10x the students? Or can I quickly make something that’s a tenth of the price but with 100x the students? There are multiple ways to slice the question, but scalability is the topic on my mind at the moment.

The most definitive answer I have right now is that I’ve built part of an introductory course I’ve never launched. Finishing that seems like a reasonable next step. I’d previously given up on the idea for fear it would flop. I was going to sell the course as a MOOC (i.e., completely self-paced and self-taught) and had concerns that CodeStories wouldn’t be a solid foundation without an actively involved instructor. Currently, I believe that, with a couple rounds of free beta testing, these concerns could be addressed fairly easily. Just like more traditional MOOCs, video tutorials could be used to supplement the hints and provide more longform explanations of new topics. Additionally, the separation between an instructor actively engaged in the full course versus a completely hands-off MOOC is a false dichotomy. It should be possible to offer some sort of nearly on-demand interactive help to students.

I’m not sure what the exact mechanism here would be. Maybe we could sell something like a Question Pack. When a student gets stuck, they can buy the ability to ask questions on the fly with the guarantee of receiving a high-quality answer and underlying explanation within 24 hours. Or perhaps you schedule 15 minutes of Zoom time. Both of these solutions are personally unscalable. But it would be significantly easier to hire people to answer beginner questions in these formats than it would to hire someone to teach a full intermediate course.

The other problem I have to improve is sales and marketing. The investment there was huge, and I don’t have the capacity to brute-force a 10x scale-up on that side of the house. The only possible option is to find something more effective. I have vague ideas about leveraging the success and customer stories from InPyBio-20 into some sort of partnership with another online learning platform. But these ideas are even more amorphous than the development plans.

It’d be nice if a neon sign appeared and screamed “Next Step!” That hasn’t happened in the last five years, but maybe one day. Until then, the real game plan is to keep doing what I’ve done thus far. I’ll mull things over, work on what I feel like, keep an eye out for opportunities, and jump in with both feet when an opportunity appears.
