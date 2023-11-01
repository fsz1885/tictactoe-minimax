# **Tic-Tac-Toe CLI Game**

A console-based Tic-Tac-Toe game that supports both player vs. player and player vs. AI modes. The game employs the Minimax algorithm for AI decision-making.

## **Minimax Algorithm: An Introduction**

The **Minimax algorithm** is a decision-making algorithm used for two-player games such as Tic-Tac-Toe, Chess, and Checkers. It predicts future moves to make the best decisions, assuming the opponent will also play optimally.

- **Maximizer:** Represents one player (often the AI) aiming to achieve the highest score possible.
- **Minimizer:** Represents the other player aiming to achieve the lowest score possible.

In our Tic-Tac-Toe context:
- The AI, when playing as 'X', aims to maximize its score, anticipating that its opponent will play optimally to minimize the AI's score.
- Conversely, when the AI plays as 'O', it seeks to minimize its score, predicting that 'X' will play to maximize its score.

This recursive approach continues until a terminal state—like a win, loss, or draw—is reached. Correctly implemented Minimax ensures the AI always plays optimally.

## **Key Features**

- Play Tic-Tac-Toe directly in your console.
- Four engaging modes to choose from:
    - Player vs. Player
    - Player vs. AI
    - AI vs. Player
    - AI vs. AI
- The AI, powered by the Minimax algorithm, always makes the best possible move.

## **Gameplay Guide**

1. **Launch:** Start the game by executing the program.
2. **Choose Mode:** Decide your preferred gameplay mode.
3. **Make Your Move:** Utilize the following keys, inspired by their keyboard positions:
    - `q` -> position 0
    - `w` -> position 1
    - `e` -> position 2
    - `a` -> position 3
    - `s` -> position 4
    - `d` -> position 5
    - `z` -> position 6
    - `x` -> position 7
    - `c` -> position 8

> **Note:** The game's board positioning is inspired by a standard QWERTY keyboard layout.

4. **Victory or Draw:** The game concludes once a player secures three consecutive symbols (horizontally, vertically, or diagonally) or when the board is completely filled, resulting in a draw.
