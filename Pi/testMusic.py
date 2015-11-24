import pygame

pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('MrBrightside.mp3')
pygame.mixer.music.play()
playing = True
pygame.time.Clock().tick(10)
while pygame.mixer.get_busy():
    print 'hi'


print 'done'
