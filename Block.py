"""
Block.py is for the bricks that will be broken and sets up
the structure of the blocks such as width and height for the
size of the blocks.
@authors Corey Rice & Steve Villarreal
@version Sprint 2022
"""
import pygame

BLACK = (0, 0, 0)


# The class Brick helps create a brick to be broken when the user bounces a ball
# into it. This class just draws the brick with rect which is a rectangle in pygame
class Brick(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()