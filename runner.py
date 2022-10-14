import pygame
pygame.init()


class Runner:
    # player info
    def __init__(self) -> None:

        self.playerX_coordinate = 190
        self.playerY_coordinate = 452
        self.player_length = 20
        self.player_height = 10
        self.player_jumping = False
        self.player_jumpCount = 8
        self.colors = [(255, 0, 100), (0, 255, 0), (0, 0, 255), (180, 0, 255), (255, 100, 255), (25, 134, 78), (90, 195, 77),
                       (60, 13, 100), (69, 11, 200), (63, 183, 204), (150, 96, 200)]

    def draw_player(self, screen):
        self.player_rect = pygame.Rect(
            self.playerX_coordinate, self.playerY_coordinate, self.player_length, self.player_height)
        # player body
        pygame.draw.rect(screen, (0, 0, 255), (self.playerX_coordinate,
                                               self.playerY_coordinate, self.player_length, self.player_height))
        # box around the player body
        pygame.draw.rect(screen, (0, 0, 255), self.player_rect, 2)
        # player legs
        legs_height = 8
        legs_length = 5
        pygame.draw.rect(screen, (0, 0, 255), (self.playerX_coordinate,
                                               self.playerY_coordinate + 10, legs_length, legs_height))
        pygame.draw.rect(screen, (0, 0, 255),
                         (self.playerX_coordinate + 15, self.playerY_coordinate + 10, legs_length, legs_height))

    def player_jump(self, screen):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_SPACE] or key_pressed[pygame.K_UP]:
            self.player_jumping = True
        # player jumping
        if self.player_jumping:
            # player extra body
            pygame.draw.rect(screen, (0, 0, 255), (self.playerX_coordinate,
                                                   self.playerY_coordinate - 10, self.player_length + 1, 10))
            pygame.draw.ellipse(screen, (255, 255, 255),
                                (self.playerX_coordinate + 2, self.playerY_coordinate - 8, 6, 7))
            pygame.draw.ellipse(screen, (255, 255, 255),
                                (self.playerX_coordinate + 13, self.playerY_coordinate - 8, 6, 7))
            if self.player_jumpCount >= -8:
                neg = 1
                if self.player_jumpCount < 0:
                    neg = -1
                self.playerY_coordinate -= (self.player_jumpCount **
                                            2) * 0.5 * neg
                self.player_jumpCount -= 1
            else:
                self.player_jumping = False
                self.player_jumpCount = 8
