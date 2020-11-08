import pygame
import sys
from pygame.locals import *
from settings import Settings
from snake import Snake

class SnakeGame:
    """Overall class to manage the game"""
    def __init__(self):
        """Initialize the game"""
        pygame.init()
        self.settings = Settings()

        self.window = pygame.display.set_mode((self.settings.window_width, self.settings.window_height))
        pygame.display.set_caption("Snake Game")

        self.snake = Snake(self.settings.snake_color, (10, 10))

    def run_game(self):
        """Run the main loop of the game"""
        while True:
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # Main settings for the game
            self.settings.settings(self.window)

if __name__ == '__main__':
    sg = SnakeGame()
    sg.run_game()