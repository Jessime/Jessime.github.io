---
title: "What's a Bioinformatics Systems Engineer?"
last_modified_at: 2020-05-31
categories:
  - Blog
tags:
  - Invitae
  - Engineering
---

## Spoiler: everyone means something different. What do we mean?

In Fall of 2019, I took on a new set of responsibilities at Invitae (the company I work for which primarily creates and sells genomic assays for healthcare diagnostics) that were loosely referred to as “systems engineering”. Because that term is ill-defined, I want to lay out:

* how the initial problem statement was described
* how I’ve been thinking about my solutions to the problem
* some interesting side effects of this role and edge responsibilities

Given that I'm nearing my first product release, this seems like an appropriate time to write this down. Hopefully it will be useful for transferring knowledge and getting others up to speed.

### The Problem

The first description of the responsibility space that resonated with me was roughly:

> We should have someone in the bioinformatics ecosystem who is responsible for helping coordinate the development of an assay from a top down approach while the the bioinformatics team-lead is simultaneously responsible for developing the assay from the bottom up. Ideally, this should cause the two approaches to smoothly meet in the middle, as opposed to the assay-dev bioinformaticians throwing their code over the wall to the pipeline engineers in late-stage assay development.

There’s a lot to unpack in those two sentences. Two smaller things first:

1. This description is assay specific. That makes this systems engineering work different from something like “platform engineering”. The latter is more concerned with the overall usability of our infrastructure, and is largely agnostic to any individual assay.
2. While much of the work for these two approaches will be done simultaneously, assay development will usually begin with a Proof-of-Concept stage where the groundwork for the assay has been laid before top-down work begins.

While I’m using “top-down” and “bottom-up” in the standard way they’re generally applied to describe problem solving techniques, it’s worth being more specific here.

When Invitae starts developing an assay, the first role in bioinformatics land is a team lead (TL) who is primarily responsible for for developing a variant caller that can robustly meet commercial requirements. Developing the caller requires an intimate understanding of the underlying biology and the upstream lab processes that are used to generate sample data. The TL needs to understand exactly how the variant caller is going to behave for each sample type and focuses on improving the the caller for scenarios in which it behaves poorly. It’s a bit of a caricature, but I find it helpful to imagine that the TL is responsible for building an algorithm (maybe running in a jupyter notebook on a laptop) that can process a single sample. This is a _bottom-up_ approach.

Alternatively, one can consider approaching assay development as a series of black boxes for which there should be inputs and desired outputs; the implementation  details of any individual black box can safely ignored. In reality, Bioinformatics is responsible for designing a pipeline capable of handling potentially thousands of samples a day, not one. Therefore, the pipeline must be able to properly interact with the rest of Invitae’s software systems in order to fully process all samples from accessioning to report rendering. Early in assay development, the aforementioned inputs and outputs are ill-defined and a long list of questions must be asked, and their answers agreed upon, before the inputs and outputs are settled. For the inputs to any given node, these questions include:

* Do we have all the types of information we need to perform this operation?
* What format is the data in?
* Is the current format the one that actually makes sense for both teams?
* Do these parameters handle all the edge cases we are expecting?
* Do teams agree on the exact names of parameters?
* Are other systems going to be (in)directly affected by any changes or decisions made?

This list is non-exhaustive and a similar set of questions must be asked for the outputs as well. And while answering these questions is most difficult between teams, it’s worth noting that this work must also be done between bioinformatics nodes. Coordinating and designing these interfaces, often (though certainly not always) ignoring specifics of the underlying bioinformatics algorithms, is the focus of systems engineering. It’s the _top-down_ approach.

### A Solution Strategy

Personally, I like to make problems concrete as quickly as possible. Therefore, my strategy for tackling this integrations problem is to do so one implementation task at a time. Usually this process starts as an underspecified story ticket. Occasionally the ticket should really be an epic. In either case, the details of the task haven’t been elucidated and often aren’t even known to the ticket writer. Below describes the cycle I’ve gone through several times at this point to handle these tickets (and in the process address the larger task of building out a top-down view of the assay).

1. The ticket writer—usually the TL— and I figure out as much as we can in a single conversation about what we already know, what would be the ideal implementation as far as the Bioinformatics team is concerned, and who we think the stakeholders are.
2. This conversation is followed up by me poking around in the codebase and building as much of a skeleton as possible so I have a bit of a mental model before involving other people. This step results an exceedingly small percentage of the final implementation (maybe 1-5%) being written. Its main purpose is to set myself up for productive conversations in the future, not to attempt to complete the ticket immediately.
3. For this description, let’s assume that the ticket includes integrating with a system (or subpart of a system) I haven’t worked with before. Given what I’ve learned in steps 1 and 2, I set up a meeting with a lead or PM from that system. In my experience, it’s crucial to limit this initial meeting to a 1:1 (maybe inviting two people is okay). I use a majority of this meeting to learn as much as possible about their system. Usually I begin with something like, **“I know a little bit about system-XYZ, but I was hoping you could start at the beginning and just give me an overview of how system-XYX works, both in general and with respect to my project specifically”.** I’ve found this question to be invaluable, even if I have previous experience with the system and think I have a pretty good idea what they’re going to say.
  1. Firstly, because this is a new assay, I’m going to come away with a lot of low-level  details I didn’t know about before. Many details won’t be relevant, but some will. It’s hard to know a priori which details fall into which category.
  2. Secondly, and more importantly, everyone has their own mental model for what Invitae’s systems are and how they work. Asking an open-ended question like the one above gives the other person free rein to transfer that model to me, whereas initially if I asked a series of directed questions initially, the other person is forced to respond from within my current frame of reference for their system. Having a shared mental model lays a solid foundation for the rest of the conversation and for future conversations. For example, I have them share their thoughts and assumptions on what the purpose of their system is and what its domain is versus what sorts of tasks should be handled by Bioinformatics.   
  3. Thirdly, a tangential but equally important reason for asking this question is that people enjoy explaining things and being helpful. I’ve found that asking these types of question sets excellent tones for working relationships.
4. Sometime in the back half of the conversation I introduce my task (as well as my question and even my proposal, if I’ve made it that far). It’s fine if I only have a task, but the conversation is smoother if I’ve clarified the process enough to have a specific proposal. The conversation then naturally proceeds towards reaching some agreement on the proposal. Especially early in the assay development cycle, it’s unlikely that this 1:1 is enough to hammer out all the details. One or both of us reach a point where we realize we need input from other people to make a decision. We then figure out who needs to be included and set up another meeting.
5. For me, this step is the most difficult. At this point, I’ll have organized a meeting of a half dozen stakeholders. Because I organized it, and because it spawned out of a task I was assigned, I have to fight the feeling that I’m supposed to have all the answers. In reality, I’m likely the dumbest person in the room. Everyone else will have been working on the project for significantly longer and all will be experts in their respective systems. Ideally, my own naiveté can be leveraged into a net positive for the meeting.
First, to kick things off, I try to be as clear as possible about the purpose of the meeting and the specific interface decision I’m trying to reach a consensus on. Once that’s done, everyone is going to have opinions and considerations. As these opinions are tossed around and the meeting proceeds, I try to not be shy about asking clarifying questions and pressing on statements that seem to assume underlying knowledge. A lot of my questions are variations on **“Why?”**. “Why do you think that’s the most important factor?” Or, ”Why is that the convention we normally follow?” Given that everyone else is an expert, they’re carrying an enormous amount of context in their heads. It’s easy to for experts to forget how much they know. Because I’m not preoccupied weighing a million different factors around this decision, I can focus some of my attention on making sure everyone provides sufficient context and communicates clearly.
6. I can also focus on taking notes. Admittedly, this is something I’m weak at. But ideally, this role should focus heavily on capturing not only the outcome of a meeting, but the underlying rationale for why that particular decision was settled on. The closer this documentation is done to realtime, the more detail is captured.
7. After the meeting, I usually broadcast the decision to the larger relevant audience to confirm there weren’t unidentified stakeholders. Usually this is just a formality. Once this is done, the notes should be integrated into a central document so everyone can find the decision later.
8. Now I go back to writing code and implementing the decision the teams have made.
9. Depending on the stage of the project and the size of the ticket, I may loop back to a previous step when I run into another blocker. Talking again with the team lead or the representative from the other system are both likely scenarios.

Again, from a systems engineering perspective, this ticket implementation cycle is a means to an end, not the solution itself. The larger goal is to create a top-down view of the assay, and be able to say:

> This is how a samples flows through Biofx for this particular assay.

By repeatedly going through this process of finding a particular thread to pull on and seeing where it leads, I’ve found I’m able to put together the individual puzzle pieces into a single cohesive picture.

### Side Effects

Ideally, enough iterations of workflow described above would provide me not only with a comprehensive top-down view of the project, but also the project’s state at any given time. In reality, I find that there are enough moving parts, and I spend enough time on implementation, that there are often some blind spots. Regardless, it seems that working through these primary responsibilities of a systems engineer builds a unique perspective on the project, which in turn allows for a number of secondary contributions:

* Generally conveying the state of the project to others, particularly PMs. A common complaint when I started was that there wasn’t much visibility into what Bioinformatics was working on or how their portion of the project was progressing. Perhaps obviously, but when a PM is interested in getting visibility into a team they usually are interested in a high level, top-down description of where things are at. So, I try to have a concise and straightforward description of the current state of development floating in my head at all times, in case anyone asks. More specifically, I can “describe the state of development” by:
  * Ensuring that all remaining work is captured in tickets. As I have conversations with other teams, it often leads to the realization that additional, un-scoped work needs to be done. Besides working on the Interfaces document, it’s important to capture the newly discovered work in a ticket. PMs or the Team Lead can decide who’s best suited to handle the work.
  * Estimating timelines and risks of remaining work. Again, this is about being about to provide concise and straightforward descriptions of the assay development process. In addition to being able to talk about what’s happening right now, I want to be able to discuss arbitrary future timepoints.
  * At any point, I want to be able to say, _“Right now, we’re working on [Set_of_tickets_1]. In [X_units_of_time], we should have completed work on [Set_of_tickets_2]. We’ll still have [Set_of_tickets_3] to complete. If we’re significantly behind on work, the most probable reason is because [Subset_of_tickets_from_1,2] took longer than expected because [XYZ reasons]”._
* Coordinating with integration testing. Unsurprisingly, working on developing interfaces leads to one also working on testing them. Probably the biggest thing I can contribute here is a testing plan that hits as much of the surface area of the assays interfaces as possible. As stated about, I want to be able to say “This is how a samples flows through Bioinformatics for this particular assay.” A natural extension of that sentence is “Here are many ways a sample can flow through Bioinformatics that we should test for this assay.”

### Conclusion

Bringing a genomics assay to market is an enormous task, requiring many more skillsets and work than simply implementing a novel bioinformatics algorithm. The complexity of the effort, however, is part of what makes the job fun. The last eight months have allowed me to touch on being a bioinformatician, a software engineer, a systems architect, and a project manager. It has been an amazing opportunity to contribute across multiple levels of abstraction to help a new assay come to life.
