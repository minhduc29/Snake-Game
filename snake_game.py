import pygame
import sys
from time import sleep
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
        self.food = Cube(self.snake.random_food(self.settings), self.settings.food_color)

    def run_game(self):
        """Run the main loop of the game"""
        while True:
            # Time delay settings
            self.settings.time()

            # Check events
            self.check_events()

            # Main function for the snake to eat the food
            self.eat_food()

            # Check gameover
            self.game_over()

            # Redraw the window
            self.settings.redraw_window(self.window, self.snake, self.food)

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

    def eat_food(self):
        """Function for the snake eating food"""
        if self.snake.body[0].position == self.food.position:
            self.snake.longer(self.settings.snake_color)
            self.food = Cube(self.snake.random_food(self.settings), self.settings.food_color)

    def game_over(self):
        """Check if game is over"""
        try:
            for x in range(len(self.snake.body)):
                if self.snake.body[x].position in list(map(lambda z:z.position, self.snake.body[x+1:])):
                    self.show_score()
                    sleep(1.5)
                    self.snake.reset(self.settings.snake_color, (10, 10))
        except:
            self.show_score()
            sleep(1.5)
            self.snake.reset(self.settings.snake_color, (10, 10))

    def show_score(self):
        """Display the score if the player lost"""
        font = pygame.font.SysFont(None, 40)
        if len(self.snake.body) > 1:
            text = font.render(f'Your score: {len(self.snake.body)}', False, self.settings.white, (255, 128, 0))
        else:
            text = font.render(f'Resetting...', False, self.settings.white, (255, 128, 0))
        text_rect = text.get_rect()
        text_rect.center = self.window.get_rect().center
        button = pygame.Rect((0, 0, 250, 100))
        button.center = self.window.get_rect().center
        self.window.fill((255, 128, 0), button)
        self.window.blit(text, text_rect)
        pygame.display.update()

if __name__ == '__main__':
    sg = SnakeGame()
    sg.run_game()