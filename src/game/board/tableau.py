class Tableau:
    """
    The tableau consists of a set of (typically) four piles that make up the main table of the game.
    Each brick that is drawn from the urn is first placed into one of the tableau piles.
    """

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

        This function checks whether a sequence of bricks can be legally added to the pile
        at the specified index (`pile_idx`). The move is considered valid if:

        1. The pile is empty, and the first brick in the sequence has the maximum possible rank (`self.max_rank`), or
        2. The pile is not empty, and the first brick in the sequence has a value directly below the top brick of the pile.

        Additionally, the sequence of bricks must be in strict descending order by their value.

        If all these conditions are met, the bricks are added to the pile, and the function returns `True`.
        If any condition is not satisfied, the function returns `False`, and no bricks are added.
        """
        pile = self.piles[pile_idx]
        brick_values = [b.value for b in bricks]

        if (
            ((len(pile) == 0) and (bricks[0].value == self.max_rank))
            or ((len(pile) > 0) and (bricks[0].is_below(pile[-1])))
        ) and (sorted(set(brick_values), reverse=True) == brick_values):
            pile.extend(bricks)
            return True
        else:
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
