class Brick:
    def __init__(self, value):
        self.value = value

    def is_below(self, brick):
        return self.value == (brick.value - 1)

    def __repr__(self):
        return f"Brick({self.value})"

    def __str__(self):
        return str(self.value)
