Description
This is a numpad that you will use to enter a PIN code:
1 2 3
4 5 6
7 8 9

At the very beginning you start with "5", afterwards you always start with a previous button and move your finger accordingly to the instructions.
The instructions consist of letters that tell you how to move your finger: U (move up), D (move down), L (move left), R (move right). Instructions consist of multiple lines.
At the end of every line (and only there) you actually need to press the button you're on. The pressed buttons are the PIN code.

Examplary solution
Given that instructions are:
RUU
DDDL
URLLL
Starting with "5" you move right to "6", then you move up to "3", then you're supposed to move up again but you can't so you stay at "3". You reached the end of the line so "3" is the first digit of your pin code.
Then you're on the second line of instructions. You start with the last digit ("3"). You move down to "6", then again down to "9", then down again but you can't move so you stay at "9" then you move left to "8". You reached the end of the line so "8" is the second digit of the pin code.
The third line - you start with "8", move up to "5", move right to "6", move left to "5", move left to "4", you should move left again but can't so you stay at "4". "4" is the last digit of the pin code.
So for these instructions the PIN code is 384.

Example to solve
Please solve the following exercise and find a PIN code for this set of instructions:
RLRLLLULULULUUDUULULRDDLURURDDLDUUDDLRDDUUUDD
LDLRLDDDLUDRDRRUDUURLRULLUDDRLURLUULDLLRLLUDLRLRUDLULRLRRL
LLRRDURRDLDULRDUDLRDRDRURULDU
DULRRDRLRLUDLLURURLLRLRDLLDLLDRDUURL
DUULULUUDUDLLRLRURULLDLRRLURDLLDUDUDDRURRLUDULULD

Write a small application/self/class (depending on your technology), that accepts input instructions and returns the correct PIN code.