# Sixteen

Sixteen (_sexton_ in Swedish) is a solitaire-type card game originating in the 19th century.

## Getting started
The command line version of the game can be started by running the Python file `src/cli.py`.

### Prerequisities
- The program is written in Python 3.8.

## Rules

### The pack
The game is played with bricks that have ranks from 1 to 16. Typically 6 bricks of each rank is included in the pack, totaling 96 bricks.

### The setup
At the start of the game, all bricks are placed in the urn and randomly shuffled.

The playing table consists of the tableau and the foundations. The tableau is made up of maximum of four piles. The foundations are six stacks on which a whole sequence of bricks must be built up. When starting out, the tableau and foundations do not have any bricks.

### The object of the game
The ultimate objective of the game is to move all bricks into the foundations, so that each of the foundation stacks contains bricks from 1 to 16 in strict ascending order. If that can be done, the game is won.

### The play
Each turn of the game consists of two phases. In the first phase, a brick is drawn from the urn, and the player can place it on any of the piles in the tableau. In the second phase, the player can move bricks within the tableau or from the tableau to the foundations, according to the following movement rules:

- A sequence of bricks can be moved from the top of a tableau pile onto another only if it is in strict descending order by the value of the bricks. Furthermore, the highest brick in the sequence must have a value directly below the top brick of the destination pile.
    - For example, if pile 1 has bricks 8-5-4-3 and pile 2 has bricks 16-3-6, the bricks 5-4-3 from pile 1 can be transferred on top of the brick 6 on pile 2.
- Any empty piles in the tableau can be filled only with a 16, or an ordered sequence of bricks starting with 16.
- A brick can be moved from the top of a pile in the tableau to any of the foundation stacks so that the stack is in strict ascending order from 1 to 16.
