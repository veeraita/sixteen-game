from config import N_STACKS

class Foundation():

    def __init__(self):
        self.n_piles = 0
        self.stacks = {i: [] for i in range(1, N_STACKS + 1)}

    def get_top_brick(self, stack_idx):
        stack = self.stacks[stack_idx]
        if len(stack) == 0:
            return None
        return stack[-1]
    
    def game_won(self):
        top_bricks = [self.get_top_brick(i) for i in self.stacks.keys()]
        if None in top_bricks:
            return False
        return all([self.get_top_brick(i).value == 16 for i in self.stacks.keys()])
    
    def add_brick(self, brick):
        brick_placed = False
        for stack_idx in self.stacks.keys():
            stack = self.stacks[stack_idx]
        
            if (len(stack) == 0) and brick.value == 1:
                stack.append(brick)
                print(f"A new foundation stack started.")
                brick_placed = True
                break
            elif (len(stack) > 0) and (brick.value == stack[-1].value + 1):
                stack.append(brick)
                print(f"Brick {brick} added to stack {stack_idx}.")
                brick_placed = True
                break
        if not brick_placed:
            print("Cannot place the brick in the foundation.")
        
        return brick_placed

    def __str__(self):
        return f"Foundation\n\t" + "\t".join([f"{self.get_top_brick(i)}" for i in self.stacks.keys()])
