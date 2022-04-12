"""
Paddle.py sets up the paddle that the user moves around to
bounce the ball back to break the blocks. It sets up the color,
width, and height of the paddle that is created in Game.py
@authors Corey Rice & Steve Villarreal
@version Sprint 2022
"""
import pygame

BLACK = (0, 0, 0)


# The Paddle class draws the paddle when passed the color, length, and width
# from the game class which is derived from Sprite
class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        # Pass in the color of the paddle, its width and height.
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the paddle as a rectangle in pygame
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

    # moveLeft checks to see that the paddle is not moving off the
    # screen when the player moves it all the way to the left
    def moveLeft(self, pixels):
        self.rect.x -= pixels

        if self.rect.x < 0:
            self.rect.x = 0

    # moveRight checks to see that the paddle is not moving off the
    # screen when the player moves it all the way to the right
    def moveRight(self, pixels):
        self.rect.x += pixels

        if self.rect.x > 900:
            self.rect.x = 900