import os
import pygame, sys

from pygame.locals import *
import pygame.camera

width = 1280
height = 720

pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0", (width, height))
cam.start()

windowSurfaceObj = pygame.display.set_mode((width, height), 1, 16)
pygame.display.set_caption('Camera')

image = cam.get_image()
cam.stop()

catSurfaceObj = image
windowSurfaceObj.blit(catSurfaceObj, (0,0))
pygame.display.update()

pygame.image.save(windowSurfaceObj, 'picture.jpg')

raw_input("press to quit")
