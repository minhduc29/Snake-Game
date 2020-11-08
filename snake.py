from cube import Cube

class Snake:
    """Class to manage snake object"""
    def __init__(self, color, position):
        """Initialize the snake"""
        self.color = color
        self.head = Cube(position)
        self.body = []
        self.body.append(self.head)