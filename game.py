from tetramino_types import *
import random
from sand import Sand, IX
from path_finding import Path

class Game:
    def __init__(self):
        self.tetramino_list = [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), ZBlock(), TBlock()]
        self.current_tetramino = self.get_random_tetramino()
        self.next_tetramino = self.get_random_tetramino()
        self.sand = Sand()
        self.is_colliding = False
        self.is_inside = True
        self.game_over = False
        self.clears = 0
        self.points = 0
        # self.colors = ["Blue", "Red", "Yellow", "Green"]

    def reset(self):
        self.sand.reset()
        self.blocks = [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), ZBlock(), TBlock()]
        self.current_block = self.get_random_tetramino()
        self.next_block = self.get_random_tetramino()
        self.points = 0
        self.clears = 0

    # check for any clears on sand grid and there is a clear delete sand from those cells
    def check_clears(self):
        for y in self.color_on_left():
            path = Path(self.sand.cell_color_name, y, self.sand.grid)
            is_found = path.find_path()
            if is_found == True:
                print("PATH FOUND")
                print(path.points_visited)
                self.clears += 1
                self.sand.cell_color_name, self.sand.grid, self.points = path.delete_cells()
                print(self.clears)


    def clear_cells(self,path):
        self.sand.cell_color_name, self.sand.grid, self.points = path.delete_cells()

    def move_left(self):
        self.current_tetramino.move(-2,0)
        self.check()
        if self.is_inside == False:
            self.current_tetramino.move(2,0)
            self.is_inside = True
        if self.is_colliding:
            self.current_tetramino.move(2,0)
            self.tetramino_to_sand()

    def move_right(self):
        self.current_tetramino.move(2,0)
        self.check()
        if self.is_inside == False:
            self.current_tetramino.move(-2,0)
            self.is_inside = True
        if self.is_colliding:
            self.current_tetramino.move(-2,0)
            self.tetramino_to_sand()

    def move_down(self):
        self.current_tetramino.move(0,2)
        self.check()
        if self.is_colliding:
            if self.current_tetramino.get_absolute_position()[0].y < 1:
                self.game_over = True

            else:
                self.current_tetramino.move(0,-2)
                self.tetramino_to_sand()
    

    
    def rotate(self):
        self.current_tetramino.rotate()
        if self.is_inside == False:
            self.current_tetramino.undo_rotate()
        else:
            self.current_tetramino.block.rotate_block()

    # in terms of rows and columns of grid, not in pixels
    def check(self):
        for point in self.current_tetramino.get_absolute_position():
            if point.x < 0 or point.x + 8 > 80:
                self.is_inside = False
            if point.y > 0:
                if point.y + 8 > 144 or self.sand.grid[IX(point.x, point.y)] != 0 or self.sand.grid[IX(point.x + 7, point.y)] != 0 or self.sand.grid[IX(point.x, point.y + 7)] != 0 or self.sand.grid[IX(point.x + 7, point.y + 7)] != 0:
                    self.is_colliding = True
    # check when for this???
    # solved

    def tetramino_to_sand(self):
        for point in self.current_tetramino.get_absolute_position():
            for j in range(8):
                for i in range(8):
                    self.sand.grid[IX(i + point.x, j + point.y)] = self.current_tetramino.return_color(i,j)
                    self.sand.cell_color_name[IX(i + point.x, j + point.y)] = self.current_tetramino.color_code
        self.current_tetramino = self.next_tetramino
        self.next_tetramino = self.get_random_tetramino()
        self.is_colliding = False   # resets value
    

    def get_random_tetramino(self):
        if len(self.tetramino_list) == 0:
            self.tetramino_list = [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), ZBlock(), TBlock()]
        tetramino = random.choice(self.tetramino_list)
        self.tetramino_list.remove(tetramino)
        tetramino.rotation_state = random.choice([0,1,2,3])
        color = random.choice(["Blue", "Red", "Yellow", "Green"])
        tetramino.give_color(color)
        tetramino.color_code = color
        # gives random color to the randomly choosen tetramino
        # important to give color before returning tetramino to avoid out of index errors for block_color in block.py
        return tetramino
    

    # keep track of y-position of every next new color on left side of wall
    def color_on_left(self):
        current_color = 0
        if self.sand.return_cell_color(0,143) != (0,0,0):
            current_color = self.sand.return_cell_color(0,143)
        y_positions = []
        for j in range(143, 0,-1):
            if current_color != self.sand.return_cell_color(0,j):
                y_positions.append(j)
                if self.sand.return_cell_color(0,j) != (0,0,0):
                    current_color = self.sand.return_cell_color(0,j)
        return y_positions
    
    
    def draw_tetramino(self, screen):
        self.current_tetramino.draw(screen)

    def draw_sand(self,screen):
        self.sand.sand_update()
        self.sand.draw(screen)
        self.check_clears()