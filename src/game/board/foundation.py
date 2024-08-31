class Foundation():

    def __init__(self):
        self.n_piles = 0
        self.stacks = {i: [] for i in range(1, 7)}

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
    
    def add_brick(self, brick, stack_idx):
        if (stack_idx < 1) or (stack_idx > 6):
            print("Error: invalid stack number.")
            return False
        
        stack = self.stacks[stack_idx]
        
        if (len(stack) == 0) and brick.value == 1:
            stack.append(brick)
            print(f"A new foundation stack started.")
            return True
        elif (len(stack) > 0) and (brick.value == stack[-1].value + 1):
            stack.append(brick)
            print(f"Brick {brick} added to stack {stack_idx}.")
            return True
        else:
            print("Cannot place the card here.")
            return False

    def __str__(self):
        top_bricks = [self.get_top_brick(i) for i in self.stacks.keys()]
        foundation_str_rows = ["Foundation\n\t1\t2\t3\t4\t5\t6"]
        return f"Foundation\n" + "\t".join([f"{self.get_top_brick(i)}" for i in self.stacks.keys()])