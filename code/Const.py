import pygame

# C

C_WHITE: tuple[int, int, int] = (255,255,255)
C_YELLOW = (201, 220, 72)

# E

ENTITY_SPEED = {
    'Level1Bg0': 1,
    'Level1Bg1': 0,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
}

# M
MENU_MOV = {
    "up": pygame.K_UP,
    "down": pygame.K_DOWN
}


MENU_OPT = ('NEW GAME',
            'HALL OF FAME',
            'EXIT')


# W

WINDOW_W = 576
WINDOW_H = 324