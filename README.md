# Tic-Tac-Toe 🎮
 
A simple two-player Tic-Tac-Toe game built with Python and Tkinter.
 
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
 
---
 
## Features
 
- Two-player gameplay locally (X vs O)
- Clean GUI created using Python's built-in `tkinter` library
- Winning combination highlighted in green with message box feedback
- Turn indicator label updates after each move
- Win detection across all rows, columns, and diagonals
---
 
## Screenshots
 
> *Two players take turns on a 3×3 grid — first to align three symbols wins.*
<img src="assets/player_X_wins.png">
---
 
## Requirements
 
- Python 3.x  

---
 
## Getting Started
 
**Clone the repository:**
 
```bash
git clone https://github.com/DonLyons/tic-tac-toe.git
cd tic-tac-toe
```
 
**Run the game:**
 
```bash
python tic_tac_toe.py
```
 
---
 
## How to Play
 
1. Run the script — a window will open with a 3×3 grid
2. Player **X** always goes first
3. Players take turns clicking empty squares to place their symbol
4. The first player to get three in a row (horizontally, vertically, or diagonally) wins
5. Winning squares are highlighted in green and a popup announces the winner
6. Close the window to exit
---
 
## Project Structure
 
```
tic-tac-toe/
└── tictactoe.py   # Main file
```
 
---
 
## How It Works
 
The game uses a list of 9 `tkinter` Button widgets on a 3×3 grid. On each click:
 
- The button is assigned the current player's symbol (**X** or **O**)
- All seven winning combinations are checked against assigned button text
- If a winner is found, the winning buttons turn green and a dialog appears
- Otherwise, the turn passes to the next player
---
 
## Possible Improvements
 
- [ ] Draw detection (board full with no winner)
- [ ] Restart button without closing the app
- [ ] Score tracking across multiple rounds
- [ ] Single-player mode with an AI opponent
---

 

