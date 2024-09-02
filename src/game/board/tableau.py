class Tableau:
    def __init__(self, max_rank=16, n_piles=4):
        self.max_rank = max_rank
        self.n_piles = n_piles
        self.piles = {i: [] for i in range(1, self.n_piles + 1)}

    def get_max_pile_length(self):
        return len(max(self.piles.values(), key=len))

    def is_valid_pile_idx(self, pile_idx):
        return pile_idx in self.piles.keys()

    def add_new_brick(self, brick, pile_idx):
        """
        Adds a single newly drawn brick to the specified pile within the tableau.

        This function places the provided brick into the pile identified by `pile_idx`.
        If the pile is currently empty, it recognizes this as the start of a new pile
        and prints a corresponding message. If the pile already contains bricks, the
        brick is simply appended to the end of the pile.

        In both cases, the function prints a message confirming the brick placement and
        returns `True`.
        """
        pile = self.piles[pile_idx]
        if len(pile) == 0:
            print(f"Brick {brick} placed in pile {pile_idx}. A new pile started.")
            pile.append(brick)
            return True
        else:
            print(f"Brick {brick} placed in pile {pile_idx}.")
            pile.append(brick)
            return True

    def add_bricks(self, bricks, pile_idx):
        """
        Attempts to add a sequence of bricks to a specified pile within the tableau.

        This function determines if the given sequence of bricks can be legally added to the pile
        at the specified index (`pile_idx`). The move is valid under the following conditions:

        1. If the target pile is empty, the bricks can only be added if the first brick in the sequence
        has the maximum possible rank (`MAX_RANK`, 16 in the original game).
        2. If the target pile is not empty, the first brick in the sequence must have a rank that is
        directly below (i.e., lower than) the rank of the brick currently on top of the pile.

        If the move is valid, the bricks are added to the pile, and the function prints a confirmation message
        and returns `True`. If the move is invalid, the function prints an error message and returns `False`.
        """
        pile = self.piles[pile_idx]

        if (len(pile) == 0) and (bricks[0].value == self.max_rank):
            print(
                f"Bricks {', '.join([str(b) for b in bricks])} moved to empty pile {pile_idx}."
            )
            pile.extend(bricks)
            return True
        elif (len(pile) > 0) and (bricks[0].is_below(pile[-1])):
            print(
                f"Bricks {', '.join([str(b) for b in bricks])} moved to pile {pile_idx}."
            )
            pile.extend(bricks)
            return True
        else:
            print("Cannot make the move.")
            return False

    def tableau_to_tableau(self, pile1, pile2):
        """
        Attempts to move a sequence of bricks from one pile to another within a tableau.

        This function checks if any contiguous sequence of bricks from `pile1` can be moved to `pile2`.
        The bricks are eligible for transfer if they are arranged in descending order of their value.
        The first valid sequence that can be moved will be transferred to `pile2`.

        If the move is successful, the bricks are removed from `pile1`, and the function returns `True`.
        If no valid sequence can be moved, the function returns `False`.
        """
        p1_bricks = self.piles[pile1]
        for i in range(len(p1_bricks)):
            # Check if the bricks are in order from largest to smallest
            if (
                sorted(set(p1_bricks[i:]), key=lambda x: x.value, reverse=True)
                == p1_bricks[i:]
            ):
                # Check if the move is successful
                if self.add_bricks(p1_bricks[i:], pile2):
                    self.piles[pile1] = p1_bricks[:i]
                    return True
        return False

    def tableau_to_foundation(self, pile_idx, foundation):
        """
        Check if the top brick of the selected tableau pile can be moved to the foundation,
        and if it can, perform the move.
        """
        brick = self.piles[pile_idx][-1]
        res = foundation.add_brick(brick)
        if res:
            self.piles[pile_idx].pop()
            return True
        return False

    def __str__(self):
        tableau_str_rows = ["Tableau\n\t1\t2\t3\t4"]
        tableau_str_rows.append("\t" + "- " * 14)
        for row in range(self.get_max_pile_length()):
            print_str = ""
            for col in range(1, 5):
                if len(self.piles[col]) > row:
                    print_str += "\t" + str(self.piles[col][row])
                else:
                    print_str += "\t"
            tableau_str_rows.append(print_str)
        return "\n".join(tableau_str_rows)
