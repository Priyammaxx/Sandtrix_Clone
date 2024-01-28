import pygame, sys
from path_finder import Path, IX
import numpy as np

pygame.init()

cell_size = 80
rows, column = 9,5
WIDTH, HEIGHT = cell_size * column , cell_size * rows

screen = pygame.display.set_mode((WIDTH - 1, HEIGHT - 1))
clock = pygame.time.Clock()

# grid = np.zeros(45)
color = {0: (0,0,0), 1: (63,110,181), 2: (114,183,84)}

grid = np.array([1,1,0,1,1,
                0,0,0,0,0,
                0,1,0,1,0,
                0,1,0,1,0,
                0,1,1,1,0,
                0,0,0,0,1,
                1,0,1,1,1,
                0,0,1,1,0,
                0,0,0,0,1])

# grid = np.array([1,1,1,1,1,
#                 1,0,0,0,0,
#                 1,0,0,1,0,
#                 1,0,1,0,0,
#                 0,0,0,0,0,
#                 1,1,0,0,1,
#                 0,0,0,1,0,
#                 1,1,0,1,0,
#                 0,0,0,1,1])



path = Path(grid,8,grid)
is_path = path.find_path()
print(is_path)
points = []

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 300)

steps = 0


def draw_maze(Screen):
    for j in range(rows):
        for i in range(column):
            rect = pygame.Rect(i*cell_size, j*cell_size, cell_size-1, cell_size-1)
            pygame.draw.rect(Screen, color[grid[IX(i,j)]], rect)

def draw_path(Screen):
    for i in points:
        rect = pygame.Rect(i[0]*cell_size, i[1]*cell_size, cell_size-1,cell_size-1)
        pygame.draw.rect(Screen, color[2], rect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == GAME_UPDATE and steps < len(path.points_visited):
            points.append(path.points_visited[steps])
            steps += 1

    screen.fill('white')
    draw_maze(screen)
    draw_path(screen)
    pygame.display.update()
    clock.tick(60)