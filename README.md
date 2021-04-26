# Grand Prix 4 NoCD fix
![Screenshot](https://raw.githubusercontent.com/Lassii-/gp4nocd/main/screenshot_small.png)
## Overview
The commonly available prepatched version of Grand Prix 4 has an annoying problem of nagging for a CD despite being cracked if you don't have an optical drive in your PC. This tool modifies that version's GP4.exe to remove the said check so the game can be played without using the virtual drive-trick as described by the source where you get the game.

The tool accomplishes this by changing two code jumps to NOPs thus bypassing the check. It's functionality has been tested to the degree that the game launches without the virtual drive trick but no long testing has been done in terms of gameplay.

## How to use
TODO

Hashes of the GP4.exe that works with this tool. The tool also has a built-in hash check before it does anything so if you don't know to check the hash, you can just try the tool.
| Algo  | Hash |
| ------------- | ------------- |
| MD5  | eb6d756ad1a17e8f8b6f77177507b550  |
| SHA1  | 592903176a7d52e0ad0deef2541a88554ed4181d  |

## How to compile
Compiling has been tested on Windows. The release binary has been compiled as 32bit to increase compatibility with older hardware that you might be using to run this game.

Compile for 32bit:
`nim c -d:release --opt:size --cpu:i386 -t:-m32 -l:-m32 GP4patcher.nim`
or for 64bit
`nim c -d:release --opt:size GP4patcher.nim`
