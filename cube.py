class Cube:
    """Class to manage cube object"""
    def __init__(self, start, color):
        """Initialize the cube"""
        self.position = start
        self.color = color
        self.dirx = 1
        self.diry = 0

    def move(self, dirx, diry):
        """Move the cube"""
        self.dirx = dirx
        self.diry = diry
        self.position = (self.position[0] + self.dirx, self.position[1] + self.diry)

    def draw_cube(self, window, head=False):
        pass