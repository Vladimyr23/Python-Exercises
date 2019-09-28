#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Vlad
#
# Created:     23/11/2015
# Copyright:   (c) Vlad 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#import modules
import sys
import pygame
import time

# initiate pygame
pygame.init()

#set size and position of screen
screen=pygame.display.set_mode ((640,480),0,32)

#set colour of screen background
screen.fill ((255,255,255))

from pygame.locals import *

x=0


while x<480:

    pygame.draw.circle(screen,(0,255,0),(320,240),x)
    time.sleep(0.1)  # wait .1 seconds
    x=x+10

    pygame.display.update()

#code to control using x
while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.display.quit()
        sys.exit()