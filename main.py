# import stuff
import pygame
import sys
#import keyboard
import random
from getkey import getkey
import flask_server

# start flask server
flask_server

# class land woohooooooo *****


# make colors for easyness
class Colors:
  def __init__(self):
    self.white = (255, 255, 255) # white
    self.black = (30, 30, 30) # black
    self.green = (0, 255, 0)

# make the screen
class Screen:
  def __init__(self):
    self.x = 640
    self.y = 480
    self.size = (self.x, self.y)

# make class objects
colors = Colors()
screen = Screen()

# no more classland

# initalize pygame
pygame.init()

# set window title
pygame.display.set_caption("pong.")

# set screen size
surface = pygame.display.set_mode(screen.size)

# setup ball
ball_radius = 8
ball_x = (screen.x / 2)
ball_y = (screen.y / 2)
ball_pos = (ball_x, ball_y)

# make paddle image
paddle_width = 10
paddle_height = 80

paddle_image = pygame.Surface((paddle_width, paddle_height))
paddle_image.fill(colors.white)

# make paddle rectangle
paddle_rect = paddle_image.get_rect()
paddle_rect.x = 60
paddle_rect.y = (screen.y / 2) - (paddle_height / 2)

# make right paddle image
rpaddle_width = 10
rpaddle_height = screen.y

rpaddle_image = pygame.Surface((rpaddle_width, rpaddle_height))
rpaddle_image.fill(colors.white)

# make right paddle rectangle
rpaddle_rect = rpaddle_image.get_rect()
rpaddle_rect.x = (screen.x - rpaddle_width)
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
    key_pressed = getkey()

    # force 60fps
    clock.tick(60)

    # make ball rectangle for collision
    ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)

    # paddle movement
    if key_pressed == 'w' and paddle_rect.y > 0: # move up
        paddle_rect.y -= player_speed

    if key_pressed == 's' and paddle_rect.y < y_size - paddle_height: # move down
        paddle_rect.y += player_speed

    # startup game
    if started is False:
        if key_pressed == 'w' or 's': # wait until user input
            started = True

            # make ball go to start
            ball_x = (screen.x / 2)
            ball_y = (screen.y / 2)
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
        
        if ball_y > screen.y or ball_y < 0:
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
    surface.fill(colors.black) # fill background with black

    # draw right wall for singleplayer
    pygame.draw.rect(surface, colors.white, rpaddle_rect)

    # draw the paddle
    pygame.draw.rect(surface, colors.white, paddle_rect)

    # draw the ball
    pygame.draw.circle(surface, clors.green, ball_pos, ball_radius)

    # update the display
    pygame.display.update()

    # handle window close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

pygame.quit()
sys.exit()