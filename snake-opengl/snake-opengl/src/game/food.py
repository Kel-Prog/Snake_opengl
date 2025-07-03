class Food:
    def __init__(self, board_width, board_height):
        self.board_width = board_width
        self.board_height = board_height
        self.position = None

    def spawn_food(self, snake_positions):
        import random
        while True:
            x = random.randint(0, self.board_width - 1)
            y = random.randint(0, self.board_height - 1)
            if (x, y) not in snake_positions:
                return (x, y)

    def get_position(self):
        return self.position

    def respawn(self, snake_positions):
        self.position = self.spawn_food(snake_positions)


