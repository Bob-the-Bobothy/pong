# import stuff
import pygame
from pygame.locals import *
import sys
from getkey import getkey, keys
import random

# initalize pygame
pygame.init()

# set screen size
x_size = 640
y_size = 480
screen_size = (x_size, y_size)

# set screen size
surface = pygame.display.set_mode(screen_size)

# set window title
pygame.display.set_caption("pong.")

# make colors for easyness
white = (255, 255, 255) # white
black = (30, 30, 30) # black
green = (0, 255, 0)

# setup ball
ball_radius = 8
ball_x = (x_size / 2)
ball_y = (y_size / 2)
ball_pos = (ball_x, ball_y)

# make paddle image
paddle_width = 10
paddle_height = 80

paddle_image = pygame.Surface((paddle_width, paddle_height))
paddle_image.fill(white)

# make paddle rectangle
paddle_rect = paddle_image.get_rect()
paddle_rect.x = 60
paddle_rect.y = (y_size / 2) - (paddle_height / 2)

# make right paddle image
rpaddle_width = 10
rpaddle_height = y_size

rpaddle_image = pygame.Surface((rpaddle_width, rpaddle_height))
rpaddle_image.fill(white)

# make right paddle rectangle
rpaddle_rect = rpaddle_image.get_rect()
rpaddle_rect.x = (x_size - rpaddle_width)
rpaddle_rect.y = 0

# make a clock for running at 60fps
clock = pygame.time.Clock()

# player speed variable for easy testing
player_speed = 5

# make the game start not started
started = False

# set ball speed
ball_direction_x = -4

# set starting lives
lives = 3

while True:

    # force 60fps
    clock.tick(60)

    #getkey stuff
    key = getkey()

    # make ball rectangle for collision
    ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)

    # paddle movement
    if key == keys.UP and paddle_rect.y > 0: # move up
        paddle_rect.y -= player_speed

    if key == keys.DOWN and paddle_rect.y < y_size - paddle_height: # move down
        paddle_rect.y += player_speed

    # startup game
    if started is False:
        if key == keys.UP or keys.DOWN: # wait until user input
            started = True

            # make ball go to start
            ball_x = (x_size / 2)
            ball_y = (y_size / 2)
            ball_pos = (ball_x, ball_y)

            # set starting direction for the ball
            ball_direction_y = 0

    if started is True:
        # as soon as game is started, start moving
        # calc ball collisions
        if ball_rect.colliderect(paddle_rect) or ball_rect.colliderect(rpaddle_rect):
            # make the ball turn around when it collides
            ball_direction_x =- ball_direction_x
            ball_direction_y += random.randint(-1, 1) # make ball bounce in slightly different direction each time
        
        if ball_y > y_size or ball_y < 0:
            # make ball bounce off walls
            ball_direction_y =- ball_direction_y

        if ball_x < 0:
            # make you die
            lives -= 1
            started = False
            if lives == 0:
                break

        # make ball move
        ball_x += ball_direction_x
        ball_y += ball_direction_y
        ball_pos = (ball_x, ball_y)

    # make sure there isn't any leftover images
    surface.fill(black) # fill background with black

    # draw right wall for singleplayer

    pygame.draw.rect(surface, white, rpaddle_rect)

    # draw the paddle
    pygame.draw.rect(surface, white, paddle_rect)

    # draw the ball
    pygame.draw.circle(surface, green, ball_pos, ball_radius)

    # update the display
    pygame.display.update()

    # handle window close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

pygame.quit()
sys.exit()