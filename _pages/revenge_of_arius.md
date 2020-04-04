---
permalink: /revenge_of_arius/
title: "The Revenge of Arius"
---

{% include figure image_path="/assets/images/revenge_start_screen.png" alt="The Revenge of Arius" caption="I managed to launch the game 6 years later on a different platform." %}


Here's a quick timeline of how I came up with [The Revenge of Arius](https://github.com/Jessime/revenge_of_arius):

1. Over Winter Break of 2013-2014, I spent a bit of time playing tower defense games.
2. During the spring semester, I took Intro to Programming and Analytical Chemistry. A lot of my time in Analytical was spent doodling tower defense game ideas in my notebook.
3. By the time I graduated, I had a game in my head, the knowledge of for loops, and a decently free summer before grad school.
4. I lived at home for a few weeks and worked on this game from 9 AM to 9 PM.

Given that this was my first project, there's significantly more wrong with the game and the code than right with it. But here are a few things that stand out now as being kind of impressive:

* I did all the art myself. I'm a terrible artist, but this [game board looks pretty sweet](https://raw.githubusercontent.com/Jessime/revenge_of_arius/master/tut19.png).
* I had no idea how networking worked, but the game was turn-based, so I came up with a scheme wherein I:
  * serialize the entire game state to a string,
  * [email the string to a throwaway gmail account](https://github.com/Jessime/revenge_of_arius/blob/master/mails.py#L247) (ignore the password),
  * check for unread emails once every few seconds when it isn't your turn,
  * and download the email and rebuild the updated game state from the string.
 * I threw away my first implementation which was entirely procedural and taught myself classes. The [class for squares on the board](https://github.com/Jessime/revenge_of_arius/blob/master/nodes.py#L11) is pretty solid.
 * There are even early signs of thinking about software engineering and maintainability. Look at this ["why"-focused comment](https://github.com/Jessime/revenge_of_arius/blob/master/nodes.py#L184)!
* I made a [full tutorial](https://github.com/Jessime/revenge_of_arius/blob/master/audio.py#L11) with both audio and visuals.

There are plenty of low points and doozies, too:

* Want to update the ice resistance of a reindeer? Do it [here](https://github.com/Jessime/revenge_of_arius/blob/master/unit_stats.py#L6).
* How do you feel about [magic numbers](https://github.com/Jessime/revenge_of_arius/blob/master/track_card.py#L19)? Want [more](https://github.com/Jessime/revenge_of_arius/blob/master/track_card.py#L59)?
* I decided I _had_ to show stats at the end of the game and ended up building a ["player health over time" graph](https://github.com/Jessime/revenge_of_arius/blob/master/end.py#L3) from the ground up.
