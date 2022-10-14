import pygame
pygame.init()


class Texts:
    def __init__(self) -> None:
        self.font1 = pygame.font.Font("Sunday morning.otf", 55)
        self.font2 = pygame.font.Font('Sunday Morning.otf',  15)
        self.font3 = pygame.font.Font('Sunday Morning.otf', 30)

    def game_over(self, screen):
        goX_coordinate, goY_coordinate = 65, 190
        go_text = self.font1.render(
            'Game Over', True, (255, 255, 255))
        screen.blit(go_text, (goX_coordinate,
                    goY_coordinate))

    def high_score(self, screen, high_score):
        hsX_coordinate, hsY_coordinate = 350, 40
        high_score_text = self.font2.render(
            "Hgh Score: " + high_score, True, (255, 255, 255))
        screen.blit(high_score_text, (hsX_coordinate, hsY_coordinate))

    def show_score(self, screen, score):
        scoreTextX_coordinate, scoreTextY_coordinate = 20, 25
        score_text = self.font3.render(
            'Score: ' + str(score // 5), True, (255, 255, 255))
        screen.blit(score_text, (scoreTextX_coordinate, scoreTextY_coordinate))
