class Snake:
    def __init__(self):
        self.body = [(0, 0)]
        self.direction = (1, 0)  # Moving right initially
        self.grow_flag = False

    def move(self):
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)

        if self.grow_flag:
            self.body.insert(0, new_head)
            self.grow_flag = False
        else:
            self.body.insert(0, new_head)
            self.body.pop()

    def grow(self):
        self.grow_flag = True

    def check_collision(self, board_width, board_height):
        head_x, head_y = self.body[0]
        if head_x < 0 or head_x >= board_width or head_y < 0 or head_y >= board_height:
            return True
        if len(self.body) != len(set(self.body)):
            return True
        return False

    def set_direction(self, new_direction):
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction

    def get_head_position(self):
        return self.body[0]

    def get_body(self):
        return self.body