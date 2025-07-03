import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from game.board import Board
from game.food import Food
from game.snake import Snake

def main():
    pygame.init()
    board_width, board_height = 20, 20
    cell_size = 20
    window_size = (board_width * cell_size, board_height * cell_size)
    pygame.display.set_mode(window_size, pygame.DOUBLEBUF | pygame.OPENGL)
    gluOrtho2D(0, board_width, 0, board_height)
    clock = pygame.time.Clock()

    board = Board(board_width, board_height)
    snake = Snake()
    food = Food(board_width, board_height)
    food.respawn(snake.body)

    running = True
    direction = (1, 0)  # Initial direction: right
    speed = 5           # Mabagal sa simula (5 FPS)

    while running:
        clock.tick(speed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_DOWN and snake.direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_LEFT and snake.direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
                    direction = (1, 0)

        snake.direction = direction

        # --- WRAP AROUND LOGIC ---
        head_x, head_y = snake.body[0]
        dx, dy = snake.direction
        new_head = (
            (head_x + dx) % board_width,
            (head_y + dy) % board_height
        )
        # Check self-collision only
        if new_head in snake.body:
            print("Game Over!")
            running = False
            continue

        snake.body.insert(0, new_head)
        # Check collision with food
        if new_head == food.get_position():
            snake.grow()
            food.respawn(snake.body)
            speed = min(speed + 1, 20)
        else:
            snake.body.pop()

        board.draw_board(snake, food)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()