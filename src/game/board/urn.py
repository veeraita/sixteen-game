import random
from .brick import Brick
from config import MAX_RANK, N_STACKS


class Urn:

    def __init__(self, max_rank=16, n_stacks=6):
        all_bricks = [
            Brick(value) for value in range(1, max_rank + 1) for i in range(n_stacks)
        ]
        self.remaining_bricks = all_bricks
        random.shuffle(self.remaining_bricks)

    def draw_brick(self):
        return self.remaining_bricks.pop()

    def __len__(self):
        return len(self.remaining_bricks)

    def __repr__(self):
        return str(self.remaining_bricks)
