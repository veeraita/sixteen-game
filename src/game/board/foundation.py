class Foundation():

    def __init__(self):
        self.n_piles = 0
        self.stacks = {i: [] for i in range(1, 7)}

    def get_top_brick(self, stack_idx):
        stack = self.stacks[stack_idx]
        if len(stack) == 0:
            return None
        return stack[-1]

    def __str__(self):
        top_bricks = [self.get_top_brick(i) for i in self.stacks.keys()]
        foundation_str_rows = ["Foundation\n\t1\t2\t3\t4\t5\t6"]
        return f"Foundation\n" + "\t".join([f"{self.get_top_brick(i)}" for i in self.stacks.keys()])