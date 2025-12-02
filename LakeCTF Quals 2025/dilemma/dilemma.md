Link:
https://lakectf.epfl.ch/challenges#dilemma-131
# dilemma
#### 28/11/2025 - 29/11/2025
## Description: 
```
A classic dilemma. Hint: there are no hidden tricks.
You're sandboxed, don't waste tiem poking the filesystem or the network.
You just need to solve it the standard way.
Example python: while True: print(1)\nEOF
nc chall.polygl0ts.ch 6667
```
### Tools used:
 - Kali Linux VM (Virtual Box)
 - Ghidra
 - Python 3
 - Claude AI
## Solution:
After connecting to the challenge via netcat it ask us to provide some Python code for player 1. 

<img width="610" height="176" alt="image" src="https://github.com/user-attachments/assets/4965af1e-bc64-4bb0-9ff8-b66f52f89368" />

So, when code prints some number it opens some "Box" with some number inside. Player 1 also has 50 attemps he needs to use.

<img width="660" height="75" alt="image" src="https://github.com/user-attachments/assets/770becbe-8524-491f-8181-6b2d435175a0" />

I wrote a 'for' loop, which prints all numbers from 1 to 50 and luckily the player 1 succeeded by finding number 1 in box 4.

According to this I realized, that the task of each player is to find his number in one of the boxes. Sounds easy, huh ?
However, there was a problem: I had no idea how  many players are there.

To find it out I decided to analyze the task file using Ghidra. (Unfortunately file didn't contain the real flag).

First of all, lets search for strings, that i got in the output.

<img width="909" height="229" alt="image" src="https://github.com/user-attachments/assets/64ec77d9-e730-4a32-b533-f3f57185a820" />
<img width="869" height="203" alt="image" src="https://github.com/user-attachments/assets/6d346fdf-2cbb-4dc6-986d-fda815118f94" />

Yep, that is just what we need. Let's see where these strings are used.

<img width="743" height="911" alt="image" src="https://github.com/user-attachments/assets/6dbcea9e-ff7d-4663-8167-b9aadf1a5b88" />

I got a function graph, which displays all the logic of the program. The main thing here is that it ends with that block in the bottom. Let's look closer.

<img width="295" height="280" alt="image" src="https://github.com/user-attachments/assets/4b0dbcf7-bbd6-4b25-913a-7d9d9417a383" />
<img width="352" height="327" alt="image" src="https://github.com/user-attachments/assets/198af46e-58dc-43e1-9b1d-31c6d8b4cc7a" />

Yeeesss !!! That's the one !

Here we see, that when each player succeedes the ```local_llf4``` variable increases by 1. If it equals to 65 in hexadecimal form (100 in decimal) the flag will be displayed.

So, exactly 100 players need to find their numbers in boxes. 100 players and 100 boxes.

Here is the algorithm, which i developed to solve this challenge:
<img width="638" height="770" alt="image" src="https://github.com/user-attachments/assets/fbc83cf9-82fa-476a-b2c8-5782395a1748" />

Of course, I did not want to find all 100 numbers by myself, so the only right way was to write a script, that will do it instead of me.

Unfortunately I did not have enough time and programming skills to write it by my own, so Claude AI did it for me :3.

If you want to see the code please refer to the dilemma.py file.

<img width="737" height="111" alt="image" src="https://github.com/user-attachments/assets/26d936c4-d7b9-456e-b936-554b3385428a" />

And finally we got the flag ! The script completes the game in ~20 seconds.
