import pygame


class Overlay(pygame.sprite.Sprite):
    # This class represents a ball. It derives from the "Sprite" class in Pygame.

    def __init__(self):
        # Call the parent class (Sprite) constructor
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