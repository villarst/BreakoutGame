"""
Overlay.py handles all over the overlay elements such as the lives,
game over screen, the win screen, and the pause text. It passes the
lives, and score from Game.py to display the correct amount.
@authors Corey Rice & Steve Villarreal
@version Sprint 2022
"""
import pygame
import pygame.font


class Overlay(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

    def setupOverlay(self, screen, lives, score, RED):
        font = pygame.font.Font(None, 34)
        text = font.render("Score: " + str(score), 1, RED)
        screen.blit(text, (20, 10))
        text = font.render("Lives: " + str(lives), 1, RED)
        screen.blit(text, (1100, 10))

    def gameOver(self, screen, BLACK):
        font = pygame.font.Font(None, 74)
        text = font.render("GAME OVER", 1, BLACK)
        screen.blit(text, (450, 300))

    def gameWon(self, screen, BLACK):
        font = pygame.font.Font(None, 74)
        text = font.render("LEVEL COMPLETE", 1, BLACK)
        screen.blit(text, (450, 300))

    # Pause when p is pressed displays a message on the screen
    # and holds the program inside of a loop until the user either
    # presses space, or escape. Then exits the loop and continues to update the game.
    def pause(self, screen, BLACK, clock):
        loop = 1
        font = pygame.font.Font(None, 74)
        text = font.render("PAUSED", 1, BLACK)
        screen.blit(text, (460, 320))
        texttwo = font.render("Press Space to continue", 1, BLACK)
        screen.blit(texttwo, (320, 390))
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        loop = 0
                    if event.key == pygame.K_SPACE:
                        screen.fill((0, 0, 0))
                        loop = 0
            pygame.display.update()
            # screen.fill((0, 0, 0))
            clock.tick(60)