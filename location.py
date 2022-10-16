import pygame
import random
pygame.init()


class Location:
    def __init__(self) -> None:
        self.floor_x = [0, 500]
        self.floor_y = 470
        self.obstacleX_position = [400, 700, 1000, 1300,
                                   1600, 1900, 2200, 2500, 2800, 3100, 3400]
        self.obstacleY_position = 430
        self.obstacle_length = []
        self.obstacle_height = 40
        self.obstacle_color = []
        self.colors = [(255, 0, 100), (0, 255, 0), (0, 0, 255), (180, 0, 255), (255, 100, 255), (25, 134, 78), (90, 195, 77),
                       (60, 13, 100), (69, 11, 200), (63, 183, 204), (150, 96, 200)]
        self.gameOver = False

    def background_floor(self, screen):
        bg_image = pygame.image.load("background.png")
        bg_position = 0, 0
        floor_image = pygame.image.load("floor.png")

        screen.blit(bg_image, bg_position)
        for i in range(2):
            self.floor_x[i] -= 5
            if self.floor_x[i] <= -490:
                self.floor_x[i] = 490
            screen.blit(floor_image, (self.floor_x[i], self.floor_y))

    def obstacles_collisions(self, screen, player_rect):

        for i in range(11):
            self.obstacle_color.append(random.choice(self.colors))
            self.obstacle_length.append(random.randint(20, 30))

            obstacle_rect = pygame.Rect(
                self.obstacleX_position[i], self.obstacleY_position - 1, self.obstacle_length[i], self.obstacle_height)
            pygame.draw.rect(screen, self.obstacle_color[i], obstacle_rect)
            self.obstacleX_position[i] -= 5
            if self.obstacleX_position[i] <= -20:
                self.obstacleX_position[i] = 3300

            if player_rect.colliderect(obstacle_rect):
                self.gameOver = True
