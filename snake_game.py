import pygame
import sys
from pygame.locals import *
from settings import Settings
from snake import Snake
from cube import Cube

class SnakeGame:
    """Overall class to manage the game"""
    def __init__(self):
        """Initialize the game"""
        pygame.init()
        self.settings = Settings()

        self.window = pygame.display.set_mode((self.settings.window_width, self.settings.window_height))
        pygame.display.set_caption("Snake Game")

        self.snake = Snake(self.settings.snake_color, (10, 10))
        self.food = Cube(self.snake.random_food(self.settings))

    def run_game(self):
        """Run the main loop of the game"""
        while True:
            # Time delay settings
            self.settings.time()

            # Check events
            self.check_events()

            # Redraw the window
            self.settings.redraw_window(self.window, self.snake)

    def check_events(self):
        """Check keys event"""
        # Check keys
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.snake.dirx = -1
                self.snake.diry = 0
                self.snake.turns[self.snake.head.position[:]] = [self.snake.dirx, self.snake.diry]
            elif keys[pygame.K_RIGHT]:
                self.snake.dirx = 1
                self.snake.diry = 0
                self.snake.turns[self.snake.head.position[:]] = [self.snake.dirx, self.snake.diry]
            elif keys[pygame.K_UP]:
                self.snake.dirx = 0
                self.snake.diry = -1
                self.snake.turns[self.snake.head.position[:]] = [self.snake.dirx, self.snake.diry]
            elif keys[pygame.K_DOWN]:
                self.snake.dirx = 0
                self.snake.diry = 1
                self.snake.turns[self.snake.head.position[:]] = [self.snake.dirx, self.snake.diry]

        # Check the movement of the snake's body
        self.snake.check_body_movement(self.settings)

if __name__ == '__main__':
    sg = SnakeGame()
    sg.run_game()