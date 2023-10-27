import numpy as np
import random
import pygame
from essentials import cell_size


def IX(x,y):
    return x + y * 80 
    # 80 = num_cols

class Sand:
    def __init__(self):
        self.num_rows = 144
        self.num_cols = 80
        self.grid = np.zeros(self.num_cols * self.num_rows, dtype=tuple)
        self.cell_color_name = np.zeros(self.num_cols * self.num_rows, dtype=str)
        # R = Red, G = Green, B = Blue, Y = Yellow

    def sand_update(self):
        for y in range(self.num_rows - 2, -1, -1):
            for x in range(self.num_cols):
                if self.grid[IX(x,y)] != 0:
                    if self.grid[IX(x,y+1)] == 0: # move down if cell below is empty
                        self.grid[IX(x,y+1)] = self.grid[IX(x,y)]
                        self.grid[IX(x,y)] = 0
                        self.cell_color_name[IX(x,y+1)] = self.grid[IX(x,y)] # color code update
                        self.cell_color_name[IX(x,y)] = ''
                    else:
                        if x == 0:
                            if self.grid[IX(1,y)] == 0 and self.grid[IX(1,y+1)] == 0:
                                self.grid[IX(1,y+1)] = self.grid[IX(0,y)]
                                self.grid[IX(0,y)] = 0
                                self.cell_color_name[IX(1,y+1)] = self.cell_color_name[IX(0,y)]# color code update
                                self.cell_color_name[IX(0,y)] = ''
                        elif x == self.num_cols - 1:
                            if self.grid[IX(x-1,y)] == 0 and self.grid[IX(x-1,y+1)] == 0:
                                self.grid[IX(x-1,y+1)] = self.grid[IX(x,y)]
                                self.grid[IX(x,y)] = 0
                                self.cell_color_name[IX(x-1,y+1)] = self.cell_color_name[IX(x,y)]# color code update
                                self.cell_color_name[IX(x,y)] = ''
                        else:
                            if self.grid[IX(x-1,y)] == 0 and self.grid[IX(x-1,y+1)] == 0:
                                if self.grid[IX(x+1,y)] == 0 and self.grid[IX(x+1,y+1)] == 0:
                                    if random.choice([0,1]):
                                        self.grid[IX(x-1,y+1)] = self.grid[IX(x,y)]
                                        self.grid[IX(x,y)] = 0
                                        self.cell_color_name[IX(x-1,y+1)] = self.cell_color_name[IX(x,y)] # color code update
                                        self.cell_color_name[IX(x,y)] = ''
                                    else:
                                        self.grid[IX(x+1,y+1)] = self.grid[IX(x,y)]
                                        self.grid[IX(x,y)] = 0
                                        self.cell_color_name[IX(x+1,y+1)] = self.cell_color_name[IX(x,y)] # color code update
                                        self.cell_color_name[IX(x,y)] = ''
                                else:
                                    self.grid[IX(x-1,y+1)] = self.grid[IX(x,y)]
                                    self.grid[IX(x,y)] = 0
                                    self.cell_color_name[IX(x-1,y+1)] = self.cell_color_name[IX(x,y)] # color code update
                                    self.cell_color_name[IX(x,y)] = ''
                            elif self.grid[IX(x+1,y)] == 0 and self.grid[IX(x+1,y+1)] == 0:
                                self.grid[IX(x+1,y+1)] = self.grid[IX(x,y)]
                                self.grid[IX(x,y)] = 0
                                self.cell_color_name[IX(x+1,y+1)] = self.cell_color_name[IX(x,y)] # color code update
                                self.cell_color_name[IX(x,y)] = ''

    def return_cell_color(self,x,y):
        return self.cell_color_name[IX(x,y)]

    def reset(self):
        self.grid = np.zeros(self.num_cols * self.num_rows, dtype=tuple)
        self.cell_color_name = np.zeros(self.num_cols * self.num_rows, dtype=str)
    
    def draw(self, screen):
        for y in range(self.num_rows - 1, -1 , -1):
            for x in range(self.num_cols):
                sand_value = self.grid[IX(x,y)]
                if sand_value != 0:
                    sand_rect = pygame.Rect(x * cell_size,
                                            y * cell_size,
                                            cell_size,
                                            cell_size)
                    pygame.draw.rect(screen, sand_value, sand_rect)
                    
