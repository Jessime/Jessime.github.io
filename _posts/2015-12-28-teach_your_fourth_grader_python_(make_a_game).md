---
title: "Teach Your Fourth Grader Python (Make a Game)"
last_modified_at: 2015-12-28
categories:
  - Blog
tags:
  - "Old Blogger"
---
Welcome to the second post on introducing your child to Python! You should have Anaconda (or another version of Python) installed on your computer before continuing. As I mentioned before, I wrote this code for and with a class of 4th graders. Did all of them understand all of the concepts? No, of course not; that wasn't really the point. All of the students thought that the game was fun. All of the students gained a little bit of insight into the technology they use everyday. That's the point.<br />
<br />
Similarly, I'm not going to attempt to fully describe everything that's going on in the code here either. The hope is that I can given enough of a description that you'll be able to either guess or google how to change a line if you wanted to do something similar. What if you decided you wanted to do division problems instead? What if you wanted to add a third player? Exercises like these are fun ways to familiarize yourself with what's going on in a script.<br />
<br />
Remember, this is for Python 3 and won't work with Python 2. Leave a comment if you want the 2.7 version for any reason. Here is the code in full:
<br />
<pre class="brush:python;">import time
import random

#Introduction
print("Hello, Players!")
print("Welcome to Multiplication Battles!")
print("")

#Input information
player1 = input("What is your name, Player 1? ")
player1_points = 0
player2 = input("What is your name, Player2? ")
player2_points = 0 
length_per_round = int(input("How many seconds do you want each round to be? "))
highest_num = int(input("What's the largest number you want to multiply? "))

#Launch Player1's game
print("")
input("{}! Hit Enter to start your time.".format(player1))
current_time = time.time()
end_time = current_time + length_per_round
while current_time &lt;= end_time:
    
    #Do math
    a = random.randint(0, highest_num)
    b = random.randint(0, highest_num)
    c = a*b
    answer = int(input("What is {}x{}? ".format(a,b)))
  
    #Check if right or wrong
    if answer == c:
        print("You're Correct!")
        player1_points += 1
    else:
        print("Sorry. {}x{}={}.".format(a,b,c))
  
    #Must update the time at the end of each loop.
    current_time = time.time()

print("You scored {} points!".format(player1_points))

#Get ready for Player2
print("")
input("{}! Hit Enter to start your time.".format(player2))
current_time = time.time()
end_time = current_time + length_per_round
while current_time &lt;= end_time:
  
    #Do math
    a = random.randint(0, highest_num)
    b = random.randint(0, highest_num)
    c = a*b
  
    #Check if right or wrong
    answer = int(input("What is {}x{}? ".format(a,b)))
    if answer == c:
        print("You're Correct!")
        player2_points += 1
    else:
        print("Sorry. {}x{}={}.".format(a,b,c))
    
    #Must update the time at the end of each loop.
    current_time = time.time()
print("You scored {} points!".format(player2_points))

#Decide a winner
print("")
if player1_points &gt; player2_points:
  print("{} wins! Good job!".format(player1))
elif player2_points &gt; player1_points:
  print("{} wins! Good job!".format(player2))
else:
  print("It was a tie! You two should play again!")

</pre>
<br />
Now we'll go through a section by section breakdown. Any line that begins with a # is a comment, and doesn't effect the way the code runs. Think of them as notes to yourself that the computer ignores. 
<br />
<pre class="brush:python;">import time
import random
</pre>
These two lines give us access to other pieces of code we'll use later in the script.&nbsp;<a href="https://docs.python.org/3/library/">This page</a>&nbsp;lists all of the 'libraries' that come standard with Python. 
<br />
<pre class="brush:python;">#Introduction
print("Hello, Players!")
print("Welcome to Multiplication Battles!")
print("")print ""
</pre>
This is the beginning of the game. The keyword 'print' is how text shows up in the console when running python. Notice that everything being printed in inside of quotation marks. This just indicates that we are printing some normal text, technically called a <a href="https://docs.python.org/3.5/library/stdtypes.html">'string'</a>. Other things, like integers, for example, can also be printed.
<br />
<pre class="brush:python;">#Input information
player1 = input("What is your name, Player 1? ")
player1_points = 0
player2 = input("What is your name, Player 2? ")
player2_points = 0 
length_per_round = int(input("How many seconds do you want each round to be? "))
highest_num = int(input("What's the largest number you want to multiply? "))
</pre>
Before launching into questions, the game collects a little bit of information about who's playing. The first thing we do is create 'player1' by asking the game players to input the name of the first player. Whatever the player types in will be stored inside of the variable 'player1'. We need to keep track of how many points the first person has, so we'll create another variable called player1_points. Since the game hasn't started, the first player currently has 0 points. The reason that the words on the left hand side of the equals sign are called variables is because their values can change over the course of the program. When the first player correctly answers a question, they'll gain a point and we'll overwrite the score stored in 'player1_points'. We'll see how this works later. Variables are a pretty complicated concept for 4th graders. The idea was one of the biggest difficult while teaching this course. If anyone has difficulty understanding what's going on here, I highly recommend checking out <a href="https://automatetheboringstuff.com/chapter1/">'How to Automate the Boring Stuff'</a>. <br />
<br />
We then repeat the process for the second player, and collect their information. Lastly, we need to know how long we want each round to last and what the largest number is that we feel comfortable multiplying. Maybe we want to go easy and play a game for 30 seconds only multiplying up to 10. Or we could go for something more challenging and give ourselves a minute to multiply numbers up to 20. Whatever you want to do. Notice the 'int' surrounding the 'input' on the last two lines. 'int' stands for 'integer', and we use this because we want Python to treat our entries in these lines like numbers instead of 'strings'.

<br />
<pre class="brush:python;">#Launch Player1's game
print("")
input("{}! Hit Enter to start your time.".format(player1))
current_time = time.time()
end_time = current_time + length_per_round
</pre>
Line number 3 is a nice way to pause the game until the first player is ready. But what's going on with the '{}'? It's just a placeholder in the text. When it is printed to the console, the first player's name will be displayed in the sentence. So, if I were playing, for example, the prompt would read, 'Jessime! Hit Enter to start your time.' As soon as I hit enter, the next line of code would execute. 
<br />
The next line is where one of our imports come in handy. We're just going to access the computer's clock to store the current time. We need to do this because we want the player to answer questions for 30 seconds, or however long was chosen. So we need to know what time the player started. We then calculate when the player's time is up (by adding up our current time and how long we want to play), and store it in the 'end_time' variable.

<br />
<pre class="brush:python;">while current_time &lt;= end_time:
    
    #Do math
    a = random.randint(0, highest_num)
    b = random.randint(0, highest_num)
    c = a*b
    answer = int(input("What is {}x{}? ".format(a,b)))
</pre>
This is where the first player begins getting questions. The first line is what's known as a <a href="http://learnpythonthehardway.org/book/ex33.html">while loop.</a> Loops are another tough subject; use the link and other resources on Google to get more information if necessary. What's happening here is quite straightforward though. We're telling Python 'Hey, execute this next bit of code over and over until the first player runs out of time'. The 'next bit of code' means all of the lines which start 4 spaces over. The code that we're going to execute over and over is:<br />
<br />
<ol>
<li>Generate a question</li>
<li>Ask the player the question</li>
<li>Give the player a point if they answer correctly</li>
<li>Tell the player the correct answer if they miss the question</li>
<li>Update the time and see if the 30 seconds is up or not</li>
</ol>
<div>
These five steps will be repeated. Lines 4-7 in the code above knock out the first two steps. We create 'a' and 'b' by using the 'random' library to generate a random integer in the range of 0 to our highest number (12, for example). The correct solution to the question will be 'a' times 'b', which we store as 'c'. Then we ask the question to the player and store their guess as 'answer'.</div>
<div>
<br /></div>
<div>
</div>
<pre class="brush:python;">        #Check if right or wrong
        if answer == c:
            print("You're Correct!")
            player1_points += 1
        else:
            print("Sorry. {}x{}={}.".format(a,b,c))
</pre>
<b>Note: This should be indented 4 spaces, but the syntax highlighter won't allow is. Look at the whole code or the player2 example for proper indentation.&nbsp;</b><br />
At this point, one of two things can happen. Either the player is right, or they're wrong. Line two says, if the answer the player gave is equivalent to the correct answer, execute the next bit of code. Again, the 'next bit of code' means all of the lines that are indented 4 spaces over. So, if the player get's the question correct, we're going to do two things. We print to the console letting the player know they answered correctly. We then increment 'player1_points' by one. That is, if the question is the first correctly answered, 'player1_points' goes from 0 to 1. If the first player has 4 points already, then 'player1_points' will now be equal to 5. If the player did not correctly answer the question, we print the correct equation.<br />
<br />
<pre class="brush:python;">    #Must update the time at the end of each loop.
    current_time = time.time()
</pre>
This line is absolutely key to the while loop. It's the last line of the while loop, which means, since we're in a loop, we're about to jump back up to line 22 (of the whole code). Once we are back at 22, we're going to reevaluate if we have any time left. The only way that the 'current_time' variable will be accurate is if we update it by 'current_time = time.time()'. If we don't have this line, the while condition will always be true, you'll enter an infinite loop, and you'll have to shutdown python manually. Make sure to have this line.<br />
<br />
Once the current time is greater than the end time, we'll exit out of the while loop, and the first player's turn will be over.
<br />
<pre class="brush:python;">print("You scored {} points!".format(player1_points))
</pre>
We can let the first player know how many points they scored. It may not look like it from the line count, but at this point, we're pretty much finished. A majority of the rest of the code is a duplicate of what we just did, but for the second player.
<br />
<pre class="brush:python;">#Get ready for Player2
print("")
input("{}! Hit Enter to start your time.".format(player2))
current_time = time.time()
end_time = current_time + length_per_round
while current_time &lt;= end_time:
  
    #Do math
    a = random.randint(0, highest_num)
    b = random.randint(0, highest_num)
    c = a*b
  
    #Check if right or wrong
    answer = int(input("What is {}x{}? ".format(a,b)))
    if answer == c:
        print("You're Correct!")
        player2_points += 1
    else:
        print("Sorry. {}x{}={}.".format(a,b,c))
    
    #Must update the time at the end of each loop.
    current_time = time.time()
print("You scored {} points!".format(player2_points))
</pre>
Literally the only change here is that I've replaced 'player1' with 'player2'. Now that each player has had their turn, the only thing left to do is figure out who the winner is.

<br />
<pre class="brush:python;">#Decide a winner
print("")
if player1_points &gt; player2_points:
  print("{} wins! Good job!".format(player1))
elif player2_points &gt; player1_points:
  print("{} wins! Good job!".format(player2))
else:
  print("It was a tie! You two should play again!")
</pre>
This block of code should look very similar to the part where we decided if the players correctly answered the question or not. The only difference is that there are now three things that can happen:<br />
<br />
<ol>
<li>Player 1 can win.</li>
<li>Player 2 can win.</li>
<li>The players can tie.</li>
</ol>
Only one of these three statements will print, and we make the decision by comparing 'player1_points' to 'player2_points' and responding appropriately. <br />
<br />
And that's it! Once the scripts executes this last line, it will automatically end and the game is over.