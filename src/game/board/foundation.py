class Foundation:
    """
    The foundation is the set of stacks to which bricks are collected in order from
    smallest to largest. The ultimate objective of the game is to get all bricks to
    the foundation.

    In the terminal UI, the top card of each foundation stack is displayed.
    """

    def __init__(self, max_rank=16, n_stacks=6):
        self.max_rank = max_rank
        self.n_stacks = n_stacks
        self.stacks = {i: [] for i in range(1, self.n_stacks + 1)}

    def get_active_stacks(self):
        """
        Returns the indices of the piles in the tableau which contain bricks.
        """
        return [s for s in self.stacks.keys() if len(self.stacks[s]) > 0]

    def get_top_brick(self, stack_idx):
        stack = self.stacks[stack_idx]
        if len(stack) == 0:
            return None
        return stack[-1]

    def add_brick(self, brick):
        """
        Check if the given brick can be placed in the foundation, and if it can, perform the move.
        The brick is placed in the first suitable stack.
        """
        for stack_idx in self.stacks.keys():
            stack = self.stacks[stack_idx]

            if ((len(stack) == 0) and brick.value == 1) or ((len(stack) > 0) and (brick.value == stack[-1].value + 1)):
                stack.append(brick)
                return stack_idx
        return None

    def __str__(self):
        return f"Foundation\n\t" + "\t".join(
            [f"{self.get_top_brick(i)}" for i in self.stacks.keys()]
        )
