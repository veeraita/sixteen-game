from board import Foundation, Tableau, Urn
from config import *


class Game:

    def __init__(self, max_rank=MAX_RANK, n_stacks=N_STACKS, n_piles=N_PILES):
        self.max_rank = max_rank
        self.n_stacks = n_stacks
        self.n_piles = n_piles

        self.urn = Urn(max_rank=self.max_rank, n_stacks=self.n_stacks)
        self.tableau = Tableau(max_rank=self.max_rank, n_piles=self.n_piles)
        self.foundation = Foundation(max_rank=self.max_rank, n_stacks=self.n_stacks)

        self.history = []

    def get_valid_moves(self):
        # Return a list of valid moves based on the current game state
        pass

    def make_move(self, move):
        if move in self.get_valid_moves():
            # Apply the move and update the game state
            self.history.append(move)
            return True  # Move was successful
        else:
            return False  # Invalid move

    def game_won(self):
        """
        Determine if the game has been won by checking that the top brick in each foundation stack
        is the game's maximum brick value.
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
            "game_won": self.game_won(),
            "valid_moves": self.get_valid_moves(),
        }
