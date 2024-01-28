import pygame, sys
from game import Game

pygame.init()

title_font = pygame.font.Font(None, 40)  # load font into variable
score_surface = title_font.render("Score", True, (255,255,255))
next_surface = title_font.render("NEXT", True, (255,255,255))
game_over_surface = title_font.render("GAME OVER", True, (255,255,255))

score_rect = pygame.Rect(500, 55, 170, 60)
next_rect = pygame.Rect(500, 215, 170, 180)

rows, columns = 144, 136
cell_size = 5
FPS = 60

WIDTH, HEIGHT = columns * cell_size, rows * cell_size

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 54)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # game.is_inside()
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                game.rotate()

        if game.game_over == True:
            game.game_over = False
            game.reset()

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
            game.move_left()
        if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
            game.move_right()
        if keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
            game.move_down()
        
        if event.type == GAME_UPDATE:
            game.move_down()
            WIN.fill('black')
            game.draw_sand(WIN)

    if game.game_over == True:
        print("GAME OVER")

            
    score_value_surface = title_font.render(str(game.points), True, (0,0,0))

    # WIN.fill((44, 44, 127))
    # WIN.blit(score_surface, (365, 20, 50, 50))
    # WIN.blit(next_surface, (375, 180, 50, 50))

    # if game.game_over == True:
    #     WIN.blit(game_over_surface, (325, 450, 50, 50))

    # pygame.draw.rect(WIN, (59, 85, 162), score_rect, 0, 10)
    # WIN.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
    # pygame.draw.rect(WIN, (59, 85, 162), next_rect, 0, 10)
    game.draw_tetramino(WIN)
    pygame.display.update()
    clock.tick(FPS)