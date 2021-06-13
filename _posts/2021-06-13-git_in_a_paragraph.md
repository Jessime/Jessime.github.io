---
title: "Get your First Git Contribution"
last_modified_at: 2021-06-13
categories:
  - Blog
tags:
  - Tutorial
---

I had a friend transition from her PhD to industry recently, and she messaged me expressing some annoyance at learning `git`.

Picking up `git` on the fly is hard. It certainly was a source of frustration for me as I began my career. I think there are two main barriers:

1. `git` can do a billion things. It's hard to know what's relevant and what's not.
2. There's new terminology flying all over the place. What does PR stand for again?

Here's a minimal explanation of everything you'd need to know to make an edit to a code base so you can continue on with the work you're _actually_ trying to get done. I'm going to make a few assumptions, like the fact that you have access to your companies code project which is hosted in GitHub. I'm also avoiding _any_ technical depth. I've linked out to terms if you want to do additional reading.

## Keys

"ssh keys" are a password. GitHub has great docs explaining this part. You'll need to make a key for your computer, described [here](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent). You'll also have to let GitHub know what key it should be looking for, described [here](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

## Repo

["Repo"](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository) is short for repository. It's a folder containing your code project. In this situation, you'll start with a "remote repo" which is the code sitting on GitHub. You'll want to make a copy of that repo on your computer.

## Clone

["Clone"](https://git-scm.com/docs/git-clone) means make a copy. Let's say you have code on GitHub at https://github.com/Jessime/youtube_history, and you want to make an edit to it. You can create a local copy of the code by running:

```
git clone git@github.com:Jessime/youtube_history.git
```

## Branch

["Branch"](https://git-scm.com/docs/git-branch) is a version of the code where you can make your edits. To create a new branch, run:

```
git checkout -b the-name-of-your-branch
```

At this point, you can finally start making edits to the codebase.

## Commit

["Commit"](https://git-scm.com/docs/git-commit) means to save the changes you've made to your code. You can save all the changes you've made with:

```
git add -A && git commit -am 'Write a message describing your changes.'
```

(I'm skipping over the concept of `staging` here. I don't think it immediately matters.)

## Push

["Push"](https://git-scm.com/docs/git-push) will share your code changes back to the original repo on GitHub. To share the commits in your new branch:

```
git push --set-upstream origin the-name-of-your-branch
```

## Pull Request (PR)

Now we're back in GitHub land, and I'll defer to their [documentation](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) again. A PR gives the other people working on your project the opportunity to review your code, make comments and suggestions, and allows you to make edits based on their suggestions. Once everyone is happy with the state of the code, you can ["merge" the PR](https://docs.github.com/en/github/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request).

<hr>

**Congrats!** You've made a change to the code that everyone has access to.

If you've made it this far and you're wondering what to do next, you may want to sync up your local repo with the remote one. The merge of your code into the repo's main branch only happened on GitHub. You'll probably want to switch branches back to your main branch and ["pull"](https://git-scm.com/docs/git-pull) the changes. Assuming you've followed this tutorial exactly, you should be able to accomplish this via:

```
git checkout - && git pull
```
