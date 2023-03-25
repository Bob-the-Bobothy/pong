# bad pong clone

### main loop:

bounce ball of your paddle and into the wall on the right. try to stay alive as long as possible

*maybe implement slow speeding up of the ball*

## code approximation area:

for the ball:

1. draw ball object
2. make ball start moving on keypress
   1. start timer
    - in a random direction: 60 degree range
3. crossroads:
    - if ball is hit by paddle:
        1. make the get stopped by the paddle
        2. make the ball get turned around
        3. make the ball go in the degree angle as before, but reversed
    - if ball makes it past paddle:
        1. make ball go back to center
        2. lose one life?
        3. stop timer til resumed
4. make ball bounce off right wall:
   1. check if it's touching
   2. stop ball
   3. reverse direction but randomize y by ~10 degrees
5. if ball hits bottom or top, bounce
   1. check for collision
   2. stop ball
   3. reverse y but not x
   4. continue