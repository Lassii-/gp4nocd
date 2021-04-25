# Grand Prix 4 NoCD fix
## Overview
The commonly available prepatched version of Grand Prix 4 has an annoying problem of nagging for a CD despite being cracked if you don't have an optical drive in your PC. This tool modifies that version's GP4.exe to remove the said check so the game can be played without using the virtual drive-trick as described by the source where you get the game.

The tool accomplishes this by changing two code jumps to NOPs thus bypassing the check. It's functionality has been tested to the degree that the game launches without any tridcks but no long testing has been done.

## How to use
You should have Python 3 installed on your PC, then place the GP4.file (see the table below for hashes to make sure you have the correct file) in the same folder as my tool and run the tool using Python and follow the instructions. You should end up with a modified GP4.exe that no longer requires any virtual drive tricks.

I might look into getting a runnable executable made somehow for Windows so you don't have to install and know to use Python to use this tool.

Hashes of the GP4.exe that works with this tool. The tool also has a built-in hash check before it does anything so if you don't know to check the hash, you can just try the tool.
| Algo  | Hash |
| ------------- | ------------- |
| MD5  | eb6d756ad1a17e8f8b6f77177507b550  |
| SHA1  | 592903176a7d52e0ad0deef2541a88554ed4181d  |
