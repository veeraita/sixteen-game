class Tableau:
    def __init__(self, max_rank=16, n_piles=4):
        self.max_rank = max_rank
        self.n_piles = n_piles
        self.piles = {i: [] for i in range(1, self.n_piles + 1)}

    def get_max_pile_length(self):
        return len(max(self.piles.values(), key=len))

    def get_active_piles(self):
        """
        Returns the indices of the piles in the tableau which contain bricks.
        """
        return [p for p in self.piles.keys() if len(self.piles[p]) > 0]

    def is_valid_pile_idx(self, pile_idx):
        return pile_idx in self.piles.keys()

    def add_new_brick(self, brick, pile_idx):
        """
        Adds a single newly drawn brick to the specified pile within the tableau.

        This function places the provided brick into the pile identified by `pile_idx` and returns the pile.
        """
        pile = self.piles[pile_idx]
        pile.append(brick)
        return pile

    def add_bricks(self, bricks, pile_idx):
        """
        Attempts to add a sequence of bricks to a specified pile within the tableau.

        This function determines if the given sequence of bricks can be legally added to the pile
        at the specified index (`pile_idx`). The move is valid under the following conditions:

        1. If the target pile is empty, the bricks can only be added if the first brick in the sequence
        has the maximum possible rank (`max_rank`, 16 in the original game).
        2. If the target pile is not empty, the first brick in the sequence must have a rank that is
        directly below (i.e., lower than) the rank of the brick currently on top of the pile.

        If the move is valid, the bricks are added to the pile, and the function returns `True`. 
        If the move is invalid, the function returns `False`.
        """
        pile = self.piles[pile_idx]

        if ((len(pile) == 0) and (bricks[0].value == self.max_rank)) or (
            (len(pile) > 0) and (bricks[0].is_below(pile[-1]))
        ):
            pile.extend(bricks)
            return True
        else:
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
            bricks_to_move = p1_bricks[i:]
            if (
                sorted(set(bricks_to_move), key=lambda x: x.value, reverse=True)
                == bricks_to_move
            ):
                # Check if the move is successful
                if self.add_bricks(bricks_to_move, pile2):
                    self.piles[pile1] = p1_bricks[:i]
                    return bricks_to_move
        return None

    def tableau_to_foundation(self, pile_idx, foundation):
        """
        Check if the top brick of the selected tableau pile can be moved to the foundation,
        and if it can, perform the move.
        """
        if len(self.piles[pile_idx]) > 0:
            brick = self.piles[pile_idx][-1]
            stack_idx = foundation.add_brick(brick)
            if stack_idx:
                self.piles[pile_idx].pop()
                return brick, stack_idx
        return None, None

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
