import random
from .brick import Brick
from config import MAX_RANK, N_STACKS


class Urn:

    all_bricks = [
        Brick(value) for value in range(1, MAX_RANK + 1) for i in range(N_STACKS)
    ]

    def __init__(self):
        self.remaining_bricks = self.all_bricks
        random.shuffle(self.remaining_bricks)

    def draw_brick(self):
        return self.remaining_bricks.pop()

    def __len__(self):
        return len(self.remaining_bricks)

    def __repr__(self):
        return str(self.remaining_bricks)
