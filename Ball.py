"""
Ball.py sets up all the operators and the rules for the ball
that will bounce around the screen with definitions such as
update, and bounce.
@authors Corey Rice & Steve Villarreal
@version Sprint 2022
"""
import pygame
from random import randint

BLACK = (0, 0, 0)


# The Ball class draws the ball when passed the color, length, and width
# from the game class which is derived from Sprite
class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the ball
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(4, 8), randint(-8, 8)]

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    # bounce changes the direction when bouncing off of something like a wall
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)