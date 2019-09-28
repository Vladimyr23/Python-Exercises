#-------------------------------------------------------------------------------
# Name:        Christmass
# Purpose:
#
# Author:      Vlad
#
# Created:     30/11/2015
# Copyright:   (c) Vlad 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#import modules
import sys
import pygame

# initiate pygame
pygame.init()

#set size and position of screen
screen=pygame.display.set_mode ((640,480),0,32)

#set colour of screen background
screen.fill ((255,255,255))



#code to control using x
while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.display.quit()
        sys.exit()