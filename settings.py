import pygame

class Settings:
    """A class to store all settings for Snake Game"""
    def __init__(self):
        """Initialize the game settings"""
        self.window_width =  700
        self.window_height = 700
        self.rows = 35
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.snake_color = (0, 153, 255)

    def settings(self, window):
        """Main settings for the game"""
        pygame.time.delay(50)
        pygame.time.Clock().tick(10)
        self.redraw_window(window)

    def redraw_window(self, window):
        """Redraw the window"""
        window.fill(self.black)
        self.draw_grid(window)
        pygame.display.update()

    def draw_grid(self, window):
        """Draw the grid"""
        size = self.window_width // self.rows

        x = 0
        y = 0
        for row in range(self.rows):
            x += size
            y += size

            pygame.draw.line(window, self.white, (x, 0), (x, self.window_width))
            pygame.draw.line(window, self.white, (0, y), (self.window_height, y))