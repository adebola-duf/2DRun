import pygame
from location import Location
from runner import Runner
from Text import Texts
from pathlib import Path

pygame.init()
clock = pygame.time.Clock()

pygame.mixer.music.load('firework.mp3')
pygame.mixer_music.play(0, 0.5)

screen_size = screen_length, scree_height = 500, 500
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("2D Run")

location = Location()
runner = Runner()
text = Texts()
score_location = Path("scores.txt")
high_score = score_location.read_text()
score = 0

run_game = True
while run_game:
    clock.tick(35)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run_game = False
    if not location.gameOver:
        score += 1
        location.background_floor(screen)
        runner.draw_player(screen)
        runner.player_jump(screen)
        location.obstacles_collisions(screen, player_rect=runner.player_rect)
        text.high_score(screen, high_score)
        text.show_score(screen, score)
    else:
        if score // 5 > int(high_score):
            score_location.write_text(str(score // 5))
        location.background_floor(screen)
        location.obstacles_collisions(screen, player_rect=runner.player_rect)
        text.game_over(screen)
        text.high_score(screen, high_score)
        text.show_score(screen, score)

    pygame.display.update()
