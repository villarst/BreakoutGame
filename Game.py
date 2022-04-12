"""
Classic Breakout game made with pygame. Game utilizes
block, ball, paddle, and overlay to create the game features
on the screen to bounce a ball around with a paddle to break blocks
to win the game. We referenced the following website for ball interaction.
https://www.101computing.net/breakout-tutorial-using-pygame-adding-a-bouncing-ball/
@authors Corey Rice & Steve Villarreal
@version Spring 2022
"""
import pygame
import random
from Paddle import Paddle
from Ball import Ball
from Block import Brick
from Overlay import Overlay
from pygame import mixer

pygame.init()
# Define the colors that we use for objects inside of the game.
WHITE = (255, 255, 255)
LIGHTBLUE = (0, 176, 240)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
# Define the score and lives for the player to see
score = 0
lives = 3

# Start a new window by creating a variable for a pygame display
size = (1200, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")
o = Overlay()

# A list to store all the sprites that are in the game, paddle, ball, and blocks
all_sprites_list = pygame.sprite.Group()

# Create the Paddle and its x,y starting coordinates
paddle = Paddle(RED, 300, 10)
paddle.rect.x = 450
paddle.rect.y = 750

# Create the ball one and its x,y starting coordinates
ball = Ball(RED, 10, 10)
ball.rect.x = 345
ball.rect.y = 495

# Create the second ball and its x,y starting coordinates
balltwo = Ball(LIGHTBLUE, 10, 10)
balltwo.rect.x = 445
balltwo.rect.y = 595

# Loops that creates the positioning and calls the
# block file to create the blocks that are to be broken
all_bricks = pygame.sprite.Group()
for i in range(10):
    # For random color generation of blocks in row 1
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = [r, g, b]

    brick = Brick(rgb, 120, 70)
    brick.rect.x = 1 + i * 120
    brick.rect.y = 50
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(10):
    # For random color generation of blocks in row 2
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = [r, g, b]

    brick = Brick(rgb, 120, 70)
    brick.rect.x = 1 + i * 120
    brick.rect.y = 130
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(10):
    # For random color generation of blocks in row 3
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = [r, g, b]

    brick = Brick(rgb, 120, 70)
    brick.rect.x = 1 + i * 120
    brick.rect.y = 210
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(10):
    # For random color generation of blocks in row 4
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = [r, g, b]

    brick = Brick(rgb, 120, 70)
    brick.rect.x = 1 + i * 120
    brick.rect.y = 290
    all_sprites_list.add(brick)
    all_bricks.add(brick)

# Put the created ball and paddle into the sprite list
all_sprites_list.add(paddle)
all_sprites_list.add(ball)
# Mixer is used to play the background music and the -1 on play loops the music
mixer.music.load('converted_retrorace-108750.wav')
mixer.music.play(-1)
# This mixer line is found the bounce sound that plays when the ball bounces
bouncesound = mixer.Sound('converted_mixkit-arcade-game-jump-coin-216.wav')
# The loop that will continue until the player loses, wins, or closes the window
carryOn = True

# This clock controls how much the screen is updated
clock = pygame.time.Clock()

# The main loop
while carryOn:
    # Event handling loop. This is for if the user does an event such as move or close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    # This handles the users left and right key presses for moving the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(10)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(10)

    # Adds a second ball.
    if keys[pygame.K_i]:
        all_sprites_list.add(balltwo)

    if keys[pygame.K_p]:
        o.pause(screen, BLACK, clock)

    all_sprites_list.update()

    # These if statements make sure the ball bounces off of the edges of the window
    if ball.rect.x >= 1190:
        ball.velocity[0] = -ball.velocity[0]
        bouncesound.play()
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
        bouncesound.play()
    if ball.rect.y > 790:
        ball.velocity[1] = -ball.velocity[1]
        bouncesound.play()
        lives -= 1
        if lives == 0:
            o.gameOver(screen, BLACK)

            pygame.display.flip()
            pygame.time.wait(3000)

            # Stop the Game
            carryOn = False

    # These if statements make sure the second ball bounces off of the edges of the window
    if balltwo.rect.x >= 1190:
        balltwo.velocity[0] = -balltwo.velocity[0]
        bouncesound.play()
    if balltwo.rect.x <= 0:
        balltwo.velocity[0] = -balltwo.velocity[0]
        bouncesound.play()
    if balltwo.rect.y > 790:
        balltwo.velocity[1] = -balltwo.velocity[1]
        bouncesound.play()
        lives -= 1
        if lives == 0:
            o.gameOver(screen, BLACK)

            pygame.display.flip()
            pygame.time.wait(3000)

            # Stop the Game
            carryOn = False

    if ball.rect.y < 40:
        ball.velocity[1] = -ball.velocity[1]

    if balltwo.rect.y < 40:
        balltwo.velocity[1] = -balltwo.velocity[1]

    # Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddle):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        bouncesound.play()
        ball.bounce()
    # Second ball logic for ball and paddle
    if pygame.sprite.collide_mask(balltwo, paddle):
        balltwo.rect.x -= balltwo.velocity[0]
        balltwo.rect.y -= balltwo.velocity[1]
        bouncesound.play()
        balltwo.bounce()

    # Check if there is a collision with the ball and any of bricks
    brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
    for brick in brick_collision_list:
        ball.bounce()
        bouncesound.play()
        score += 1
        brick.kill()
        if len(all_bricks) == 0:
            o.gameWon(screen, BLACK)

            pygame.display.flip()
            pygame.time.wait(3000)

            # Stop the Game
            carryOn = False

    # Check if there is a collision with the second ball and any of bricks
    brick_collision_list = pygame.sprite.spritecollide(balltwo, all_bricks, False)
    for brick in brick_collision_list:
        balltwo.bounce()
        bouncesound.play()
        score += 1
        brick.kill()
        if len(all_bricks) == 0:
            o.gameWon(screen, BLACK)

            pygame.display.flip()
            pygame.time.wait(3000)

            # Stop the Game
            carryOn = False

    # Making the background white
    screen.fill(WHITE)
    # Calls the overlay and sets it up.
    o.setupOverlay(screen, lives, score, RED)

    # These lines draw and display all the sprites onto the screen
    all_sprites_list.draw(screen)
    pygame.display.flip()

    # This clock updates 60 times a second, AKA 60 frames per second
    clock.tick(60)

# This line is just to ensure if we exit the main loop we exit the pygame engine
pygame.quit()