import pygame
import time
import sys

from pygame.locals import *

pygame.init()
screen=pygame.display.set_mode ((640,480),0,32)

screen.fill((255,0,0))

x=0
y=0
z=0

while x<640:

    pygame.draw.circle(screen,(0,255,0),(x,y),50)
    time.sleep(0.5)  # wait .5 seconds
    x=x+60
    y=y+60

    pygame.display.update()

#code to control using x
while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.display.quit()
        sys.exit()
