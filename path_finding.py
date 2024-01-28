# from sand import IX

def IX(x,y):
    return x + y * 80

class Path:
    def __init__(self, grid, initial_y, sand_grid):
        self.grid = grid
        self.sand_grid = sand_grid
        self.initial_y = initial_y
        self.y = initial_y
        self.x = 0
        self.val = self.grid[IX(0,self.y)]
        self.backtrack_point = ()
        self.points_visited = [(self.x, self.y)]
        self.backtrack_move = '' # move on which backtrak created
        self.y_max = 144
        self.x_max = 80

    def find_path(self):
        found = False
        run = True
        last_moved = 'UP'
        backtrack_move_dict = {'DOWN':'UP', 'UP':'DOWN', 'LEFT':'RIGHT','RIGHT':'LEFT'}
        # last_moved_backtrack = ''   # move on which backtrack created
        while run:
            if last_moved == 'UP':
                if self.right() == True:
                    last_moved = 'RIGHT'
                elif self.up() == True:
                    last_moved = 'UP'
                elif self.left() == True:
                    last_moved = 'LEFT'
                elif self.backtrack_point:
                    self.x = self.backtrack_point[0]
                    self.y = self.backtrack_point[1]
                    self.backtrack_point = ()
                    last_moved = backtrack_move_dict[self.backtrack_move]
                else:
                    run = False

            elif last_moved == 'RIGHT':
                if self.down() == True:
                    last_moved = 'DOWN'
                elif self.right() == True:
                    last_moved = 'RIGHT'
                elif self.up() == True:
                    last_moved = 'UP'
                elif self.backtrack_point:
                    self.x = self.backtrack_point[0]
                    self.y = self.backtrack_point[1]
                    self.backtrack_point = ()
                    last_moved = backtrack_move_dict[self.backtrack_move]
                else:
                    run = False

            elif last_moved == 'DOWN':
                if self.left() == True:
                    last_moved = 'LEFT'
                elif self.down() == True:
                    last_moved = 'DOWN'
                elif self.right() == True:
                    last_moved = 'RIGHT'
                elif self.backtrack_point:
                    self.x = self.backtrack_point[0]
                    self.y = self.backtrack_point[1]
                    self.backtrack_point = ()
                    last_moved = backtrack_move_dict[self.backtrack_move]
                else:
                    run = False

            elif last_moved == 'LEFT':
                if self.up() == True:
                    last_moved = 'UP'
                elif self.left() == True:
                    last_moved = 'LEFT'
                elif self.down() == True:
                    last_moved = 'DOWN'
                elif self.backtrack_point:
                    self.x = self.backtrack_point[0]
                    self.y = self.backtrack_point[1]
                    self.backtrack_point = ()
                    last_moved = backtrack_move_dict[self.backtrack_move]
                else:
                    run = False
            
            if (self.x,self.y) not in self.points_visited:
                self.points_visited.append((self.x,self.y))

            if self.x == self.x_max - 1:
                found = True
                # run = False # need to remove this later
            if self.x == 0 and self.y == self.initial_y:
                run = False
        return found

    def up(self):
        if self.y < 1:
            return False
        if self.grid[IX(self.x,self.y-1)] == self.val:
            if self.x > 0 and self.y < self.y_max-1:
                if self.grid[IX(self.x-1,self.y-1)] != self.val and self.grid[IX(self.x+1,self.y-1)] != self.val:
                    self.backtrack_point = (self.x,self.y)
                    self.backtrack_move = 'UP'
            self.y -= 1
            return True
        return False

    def down(self):
        if self.y == self.y_max - 1 :
            return False
        if self.grid[IX(self.x,self.y+1)] == self.val:
            if self.x < self.x_max-1 and self.y < self.y_max-1:
                if self.grid[IX(self.x+1,self.y+1)] != self.val and self.grid[IX(self.x-1,self.y+1)] != self.val:
                    self.backtrack_point = (self.x,self.y)
                    self.backtrack_move = 'DOWN'
            self.y += 1
            return True
        return False

    def right(self):
        if self.x == self.x_max - 1:
            return False
        if self.grid[IX(self.x+1,self.y)] == self.val:
            if self.x < self.x_max-1 and self.y > 0:
                if self.grid[IX(self.x+1,self.y-1)] != self.val and (self.y == self.y_max - 1 or self.grid[IX(self.x+1,self.y+1)] != self.val):
                    self.backtrack_point = (self.x,self.y)
                    self.backtrack_move = 'RIGHT'
            self.x += 1
            return True
        return False
        
    def left(self):
        if self.x < 1:
            return False
        if self.grid[IX(self.x-1,self.y)] == self.val:
            if self.x > 0 and self.y < self.y_max-1:
                if self.grid[IX(self.x-1,self.y+1)] != self.val and (self.y == self.y_max - 1 or self.grid[IX(self.x-1,self.y-1)] != self.val):
                    self.backtrack_point = (self.x,self.y)
                    self.backtrack_move = 'LEFT'
            self.x -= 1
            return True
        return False


    def delete_cells(self):
        points = 0
        for cell in self.points_visited:
            x = cell[0]
            y = cell[1]
            while self.grid[IX(x,y)] == self.val:
                self.grid[IX(x,y)] = 0
                self.sand_grid[IX(x,y)] = 0
                if (x,y) in self.points_visited:
                    self.points_visited.remove((x,y))
                y += 1
                points += 1
        return self.grid, self.sand_grid, points
    # return color code grid, then sand_grid
