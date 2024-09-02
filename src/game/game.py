from .board import Foundation, Tableau, Urn


class Game:

    def __init__(self, max_rank=16, n_stacks=6, n_piles=4):
        self.max_rank = max_rank
        self.n_stacks = n_stacks
        self.n_piles = n_piles

        self.urn = Urn(max_rank=self.max_rank, n_stacks=self.n_stacks)
        self.tableau = Tableau(max_rank=self.max_rank, n_piles=self.n_piles)
        self.foundation = Foundation(max_rank=self.max_rank, n_stacks=self.n_stacks)

        self.history = []

    def move_new_brick_to_tableau(self, brick, pile_idx):
        pile = self.tableau.add_new_brick(brick, pile_idx)
        self.history.append(("N", pile_idx))
        return pile

    def move_tableau_to_tableau(self, pile1, pile2):
        """
        Attempts to move a sequence of bricks from one pile to another within a tableau.

        This function checks if any contiguous sequence of bricks from `pile1` can be moved to `pile2`.
        The bricks are eligible for transfer if they are arranged in descending order of their value.
        The first valid sequence that can be moved will be transferred to `pile2`.

        If the move is successful, the bricks are removed from `pile1`, and the function returns the moved bricks.
        If no valid sequence can be moved, the function returns `None`.
        """
        p1_bricks = self.tableau.piles[pile1]
        for i in range(len(p1_bricks)):
            # Check if the bricks are in order from largest to smallest
            bricks_to_move = p1_bricks[i:]
            # Check if the move is successful
            if self.tableau.add_bricks(bricks_to_move, pile2):
                self.tableau.piles[pile1] = p1_bricks[:i]
                self.history.append(("T", pile1, pile2))
                return bricks_to_move
        return None
    
    def move_tableau_to_foundation(self, pile_idx):
        """
        Check if the top brick of the selected tableau pile can be moved to the foundation,
        and if it can, perform the move.

        If the move is successful, the brick is removed from the pile and the function returns both the brick and 
        the index of the foundation stack; otherwise, both will be `None`.

        """
        if len(self.tableau.piles[pile_idx]) > 0:
            brick = self.tableau.piles[pile_idx][-1]
            stack_idx = self.foundation.add_brick(brick)
            if stack_idx:
                self.tableau.piles[pile_idx].pop()
                self.history.append(("F", pile_idx, stack_idx))
                return brick, stack_idx
        return None, None

    def game_won(self):
        """
        Determine if the game has been won by checking that the top brick in each foundation stack
        is the game's maximum brick value.

        Returns `True` if the game has been won, `False` otherwise.
        """
        top_bricks = [
            self.foundation.get_top_brick(i) for i in self.foundation.stacks.keys()
        ]
        if None in top_bricks:
            return False
        return all(
            [
                self.foundation.get_top_brick(i).value == self.max_rank
                for i in self.foundation.stacks.keys()
            ]
        )

    def get_game_state(self):
        return {
            "tableau": self.tableau.piles,
            "foundation": self.foundation.stacks,
            "remaining_bricks": self.urn.remaining_bricks,
            "game_won": self.game_won()
        }
