from colors import Colors
from essentials import *

class Block:
    def __init__(self):
        self.block_side = block_side # = 8
        self.cell_size = cell_size # = 5 in pixels
        # one block side has 8 cells
        self.block_color = []

    def create_block(self, color): # creates square block of desired color
        for i in range(self.block_side):
            for j in range(self.block_side):
                self.block_color.append(Colors.return_color(color))
                
    def rotate_block(self):
        new_block_color = []
        for j in range(8):
            for i in range(8):
                new_block_color.append(self.block_color[IX(j,7-i,8)])
        self.block_color = new_block_color