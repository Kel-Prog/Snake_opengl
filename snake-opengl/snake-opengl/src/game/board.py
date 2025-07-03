from OpenGL.GL import *

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw_board(self, snake, food):
        # Clear screen
        glClear(GL_COLOR_BUFFER_BIT)

        # Draw snake (green)
        for segment in snake.body:
            self.draw_cell(segment, (0, 1, 0))

        # Draw food (red)
        if food.get_position():
            self.draw_cell(food.get_position(), (1, 0, 0))

    def draw_cell(self, position, color):
        x, y = position
        glColor3fv(color)
        glBegin(GL_QUADS)
        glVertex2f(x, y)
        glVertex2f(x + 1, y)
        glVertex2f(x + 1, y + 1)
        glVertex2f(x, y + 1)
        glEnd()

    def check_boundaries(self, position):
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.height