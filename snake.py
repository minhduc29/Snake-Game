from cube import Cube

class Snake:
    """Class to manage snake object"""
    def __init__(self, color, position):
        """Initialize the snake"""
        self.color = color
        self.head = Cube(position)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirx = 0
        self.diry = 1

    def check_body_movement(self):
        """Loop through the snake's body and check direction and position"""
        for i, cube in enumerate(self.body):
            # Current position of the cube on the grid
            cube_position = cube.position[:]

            # If the cube's current position is where we turned
            if cube_position in self.turns:
                # Get the position where we turned
                turn = self.turns[cube_position]

                # Move the cube in that position
                cube.move(turn[0], turn[1])

                # Check last cube in the body
                if i == len(self.body) - 1:
                    self.turns.pop(cube_position)

            # If we're not turning the cube
            else:
                # If the cube reaches the edge of the screen or we're just moving normally
                if cube.dirx == -1 and cube.position[0] <= 0:
                    cube.position = (self.settings.rows - 1, cube.position[1])
                elif cube.dirx == 1 and cube.position[0] >= self.settings.rows - 1:
                    cube.position = (0, cube.position[1])
                elif cube.diry == 1 and cube.position[1] >= self.settings.rows - 1:
                    cube.position = (cube.position[0], 0)
                elif cube.diry == -1 and cube.position[1] <= 0:
                    cube.position = (cube.position[0], self.settings.rows - 1)
                else:
                    cube.move(cube.dirx, cube.diry)

    def draw_snake(self, window):
        """Draw the snake"""
        for i, cube in enumerate(self.body):
            if i == 0:
                cube.draw_cube(window, True)
            else:
                cube.draw_cube(window)