import pygame
import random
from pathlib import Path

score_location = Path("scores.txt")
pygame.init()

screen = pygame.display.set_mode((500, 500))

clock = pygame.time.Clock()

pygame.display.set_caption('2d run')

pygame.mixer.music.load('firework.mp3')
pygame.mixer_music.play(0, 0.5)

# player info
playerX_coordinate = 190
playerY_coordinate = 452
player_length = 20
player_height = 10
player_jumping = False
player_jumpCount = 8
colors = [(255, 0, 100), (0, 255, 0), (0, 0, 255), (180, 0, 255), (255, 100, 255), (25, 134, 78), (90, 195, 77),
          (60, 13, 100), (69, 11, 200), (63, 183, 204), (150, 96, 200)]


def player():
    global player_jumpCount, player_jumping, playerY_coordinate

    # player body
    pygame.draw.rect(screen, (0, 0, 255), (playerX_coordinate,
                     playerY_coordinate, player_length, player_height))
    # box around the player body
    pygame.draw.rect(screen, (0, 0, 255), player_rect, 2)
    # player legs
    legs_height = 8
    legs_length = 5
    pygame.draw.rect(screen, (0, 0, 255), (playerX_coordinate,
                     playerY_coordinate + 10, legs_length, legs_height))
    pygame.draw.rect(screen, (0, 0, 255),
                     (playerX_coordinate + 16, playerY_coordinate + 10, legs_length, legs_height))

    # player jumping
    if player_jumping:
        # player extra body
        pygame.draw.rect(screen, (0, 0, 255), (playerX_coordinate,
                         playerY_coordinate - 10, player_length + 1, 10))
        pygame.draw.ellipse(screen, (255, 255, 255),
                            (playerX_coordinate + 2, playerY_coordinate - 8, 6, 7))
        pygame.draw.ellipse(screen, (255, 255, 255),
                            (playerX_coordinate + 13, playerY_coordinate - 8, 6, 7))
        if player_jumpCount >= -8:
            neg = 1
            if player_jumpCount < 0:
                neg = -1
            playerY_coordinate -= (player_jumpCount ** 2) * 0.5 * neg
            player_jumpCount -= 1
        else:
            player_jumping = False
            player_jumpCount = 8


obstacleX_position = [400, 700, 1000, 1300,
                      1600, 1900, 2200, 2500, 2800, 3100, 3400]
obstacleY_position = 430
obstacle_length = []
obstacle_height = 40
obstacle_color = []


def obstacles_and_collision():
    global gameOver, obstacle_length, obstacleX_position

    for i in range(11):
        obstacle_color.append(random.choice(colors))
        obstacle_length.append(random.randint(20, 30))

        obstacle_rect = pygame.Rect(
            obstacleX_position[i], obstacleY_position - 1, obstacle_length[i], obstacle_height)
        pygame.draw.rect(screen, obstacle_color[i], obstacle_rect)
        obstacleX_position[i] -= 5
        if obstacleX_position[i] <= -20:
            obstacleX_position[i] = 3300

        if player_rect.colliderect(obstacle_rect):
            gameOver = True
        # if player_rect.x > obstacle_rect.x:


floorX_coordinate = [0, 500]
floorY_coordinate = 470
floor_image = pygame.image.load('floor night.png')


def floor():
    for i in range(2):
        floorX_coordinate[i] -= 5
        if floorX_coordinate[i] <= -500:
            floorX_coordinate[i] = 500
        screen.blit(floor_image, (floorX_coordinate[i], floorY_coordinate))


gameOver = False


def background():
    bg = pygame.image.load('background.png')
    screen.blit(bg, (0, 0))


score = 0
score_font = pygame.font.Font('Sunday Morning.otf', 30)
scoreTextX_position = 20
scoreTextY_position = 25
high_score = score_location.read_text()


def show_score():
    score_text = score_font.render(
        'Score: ' + str(score // 5), True, (255, 255, 255))
    screen.blit(score_text, (scoreTextX_position, scoreTextY_position))


gameOver_font = pygame.font.Font('Sunday Morning.otf', 55)
gameOverTextX_position = 65
gameOverTextY_position = 190


def game_over():
    gameOver_text = gameOver_font.render('Game Over', True, (255, 255, 255))
    screen.blit(gameOver_text, (gameOverTextX_position, gameOverTextY_position))


hs_font = pygame.font.Font('Sunday Morning.otf',  15)


def show_high_score():
    high_score_text = hs_font.render(
        "Hgh Score: " + high_score, True, (255, 255, 255))
    screen.blit(high_score_text, (350, 35))


run_game = True

while run_game:
    background()
    player_rect = pygame.Rect(
        playerX_coordinate, playerY_coordinate, player_length, player_height)
    clock.tick(35)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run_game = False

    key_pressed = pygame.key.get_pressed()

    if key_pressed[pygame.KMOD_ALT and pygame.K_F4]:
        run_game = False

    if not gameOver:
        score += 1
        if key_pressed[pygame.K_UP] or key_pressed[pygame.K_SPACE]:
            player_jumping = True
        show_score()
        player()
        show_high_score()
    if gameOver:
        if score // 5 > int(high_score):
            score_location.write_text(str(score // 5))
        show_score()
        game_over()
        show_high_score()
    obstacles_and_collision()
    floor()
    pygame.display.update()
