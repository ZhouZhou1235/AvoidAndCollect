import pygame

pygame.display.init()
gotScreen = pygame.display.Info()
SCREEN_WIDTH = gotScreen.current_w
SCREEN_HEIGHT = gotScreen.current_h
GAME_TITLE = "躲避与收集"
FPS = 60

border = 25
EDGE = [[0,0,SCREEN_WIDTH,border],
        [0,0,border,SCREEN_HEIGHT],
        [0,SCREEN_HEIGHT-border,SCREEN_WIDTH,border],
        [SCREEN_WIDTH-border,0,border,SCREEN_HEIGHT]]