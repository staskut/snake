import numpy as np

from settings.constants import DIRECTIONS, SNAKE_BLOCK


class Snake:
    def __init__(self, head_position, direction_index, length):
        """
        @param head_position: tuple
        @param direction_index: int
        @param length: int
        """
        self.head_position =
        self.current_direction_index =
        self.length = 3
        # Information snake need to know to make the move
                self.snake_block = SNAKE_BLOCK
        self.current_direction_index = direction_index
                # Alive identifier
        self.alive = True
        # Place the snake
        self.blocks = [head_position]
        current_position = np.array(head_position)
        for i in range(1, length):
            # Direction inverse of moving
            current_position = current_position - DIRECTIONS[self.current_direction_index]
            self.blocks.append(tuple(current_position))

    def step(self, action):
        """
        @param action: int
        @param return: tuple, tuple
        """
        self.action
        return
        # Check if action can be performed (do nothing if in the same direction or opposite)
        if () and ():
            self.current_direction_index = action
        # Remove tail
        tail = 1
        self.blocks =
        # Check new head
        new_head =
        # Add new head
        self.blocks = [new_head] + self.blocks
        return new_head, tail