from block import Block
import pygame
from essentials import Position, IX

class Tetramino:
    def __init__(self):
        self.rotation_state = 0
        self.x_offset = 0 # in pixels
        self.y_offset = 0 # in pixels
        self.x_grid = 0 # x position in grid
        self.y_grid = 0 # y position in grid
        self.cells = {}
        self.block = Block()
        self.color_code = ''

    # to initialise block with color
    def give_color(self,color):
        self.block.create_block(color)
    
    def return_color(self, x, y):
        return self.block.block_color[IX(x , y, 8)]

    def move(self, x, y):
        self.x_offset += (x * self.block.cell_size)
        self.y_offset += (y * self.block.cell_size)
        self.x_grid += x
        self.y_grid += y

    def get_block_position(self):
        start_points = self.cells[self.rotation_state]
        moved_points = []
        for position in start_points:
            point = Position(position.x, position.y)
            moved_points.append(point)
        return moved_points
    
    def get_absolute_position(self):
        start_points = self.cells[self.rotation_state]
        moved_points = []
        for position in start_points:
            point = Position(position.x + self.x_grid, position.y + self.y_grid)
            moved_points.append(point)
        return moved_points
    
    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == 4: # max rotation states = 4, indexed from 0-3
            self.rotation_state = 0
        # self.block.rotate_block()

    def undo_rotate(self):
        self.rotation_state -= 1
        if self.rotation_state == -1:
            self.rotation_state = 3

    def draw(self,screen):
        points = self.get_block_position()
        for point in points:
            for j in range(8):
                for i in range(8):
                    square = pygame.Rect(
                        (point.x + i) * self.block.cell_size + self.x_offset,
                        (point.y + j) * self.block.cell_size + self.y_offset,
                        self.block.cell_size,
                        self.block.cell_size)
                    pygame.draw.rect(screen, self.block.block_color[IX(i,j,self.block.block_side)], square)