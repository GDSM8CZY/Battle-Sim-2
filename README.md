# Battle Sim 2
This game is a simple text-based battle simulator that runs in the terminal, I used it for my final project in AP Comp Sci Principles. This version is slightly updated from the one I submitted. The previous game I made was for my Python 1 final, where I was much less experienced.

## New Gameplay
- There are many new weapons
- You select a name for yourself and the enemy
- Player stats are saved in a separate file based on name
- Added ASCII art from [https://www.asciiart.eu/]

## Code Changes
- Instead of classes for each weapon, there is now a 'Weapon' class
- Instead of a separate class for the player and the enemy, there is now a 'Fighter' class
- Classes now have an init() method and other methods in the classes

## Instalation
You can install with pip or pipx, or any other method for installing GitHub repos.
pip example:
```terminal
pip install git+https://github.com/GDSM8CZY/BattleSim2.git
```
pipx example:
```terminal
pipx install git+https://github.com/GDSM8CZY/BattleSim2.git
```
Then to play type in terminal
```terminal
battlesim2
```
