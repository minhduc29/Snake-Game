import pygame

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

    def draw_cube(self, window, settings, head=False):
        """Draw the cube"""
        size = settings.window_width // settings.rows
        i = self.position[0] # Row
        j = self.position[1] # Column

        pygame.draw.rect(window, self.color, (i*size + 1, j*size + 1, size - 2, size - 2))

        if head:
            centre = size // 2
            radius = 3
            mid_cir = (i*size + centre - radius, j*size + 8)
            mid_cir2 = (i*size + size - radius*2, j*size + 8)
            pygame.draw.circle(window, settings.black, mid_cir, radius)
            pygame.draw.circle(window, settings.black, mid_cir2, radius)