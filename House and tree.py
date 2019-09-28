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

# initiate pygame
pygame.init()

#set size and position of screen
screen=pygame.display.set_mode ((640,480),0,32)

#set colour of screen background
screen.fill ((255,255,255))

from pygame.locals import *

#House
pygame.draw.rect(screen,(0,0,0),Rect(50,150,450,250))
pygame.display.update()

#House roof
#pygame.draw.triangle

#Tree trunk
pygame.draw.rect(screen,(200,200,0),Rect(530,340,50,100))
pygame.display.update()

#Windows
pygame.draw.rect(screen,(0,0,100),Rect(80,180,50,50))
pygame.display.update()

pygame.draw.rect(screen,(0,0,100),Rect(210,180,50,50))
pygame.display.update()

pygame.draw.rect(screen,(0,0,100),Rect(420,180,50,50))
pygame.display.update()

#Door
pygame.draw.rect(screen,(100,100,0),Rect(320,280,70,120))
pygame.display.update()

#Tree leafs
pygame.draw.circle(screen,(0,255,0),(555,300),60)
pygame.display.update()

#code to control using x
while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.display.quit()
        sys.exit()