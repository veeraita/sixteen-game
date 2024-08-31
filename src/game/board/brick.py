class Brick():
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f"Brick({self.value})"
    
    def __str__(self):
        return str(self.value)