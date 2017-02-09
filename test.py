import sys

import pygame
from pygame.constants import QUIT, K_ESCAPE, KEYDOWN


def sprite( frameWidth, frameHeight ):
    animation_frames = []
    timer = pygame.time.Clock()
    screen = pygame.display.set_mode( ( 400, 400 ), 0, 32 )
    image = pygame.image.load( "./assets/Explosion-21.png" )
    width, height = image.get_size()

    for i in range( int( width / frameWidth ) ):
        animation_frames.append( image.subsurface( ( i * frameWidth, 0, frameWidth, frameHeight ) ) )
    counter = 0

    while True:
        for evt in pygame.event.get():
            if evt.type == QUIT or ( evt.type == KEYDOWN and evt.key == K_ESCAPE ) :
                sys.exit()

        screen.fill( ( 46, 64, 83 ) )
        screen.blit( animation_frames[counter], ( 100, 100 ) )
        counter = ( counter + 1 ) % 20
        pygame.display.update()
        timer.tick( 60 )

if __name__ == "__main__":
    sprite( 250, 250 )