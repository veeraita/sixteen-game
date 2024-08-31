import random
from .brick import Brick

class Urn():

    all_bricks = [Brick(value) for value in range(1, 17) for i in range(6)]

    def __init__(self):
        self.remaining_bricks = self.all_bricks
        random.shuffle(self.remaining_bricks)
    
    def draw_brick(self):
        return self.remaining_bricks.pop()
    
    def __len__(self):
        return len(self.remaining_bricks)
    
    def __repr__(self):
    	return str(self.remaining_bricks)
    