class Brick:
    """
    Bricks are the devices with which the game 16 is played. They have a numerical value from 1 to 16.
    """
    def __init__(self, value):
        self.value = value

    def is_below(self, brick):
        return self.value == (brick.value - 1)

    def __repr__(self):
        return f"Brick({self.value})"

    def __str__(self):
        return str(self.value)
