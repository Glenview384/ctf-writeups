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
To find it out I decided to analyze the task file using Ghidra. (Unfortunately file didn't print the real flag).

First of all, lets search for strings, that i got in the output.

<img width="909" height="229" alt="image" src="https://github.com/user-attachments/assets/64ec77d9-e730-4a32-b533-f3f57185a820" />
<img width="869" height="203" alt="image" src="https://github.com/user-attachments/assets/6d346fdf-2cbb-4dc6-986d-fda815118f94" />

Yep, that is just what we need.


