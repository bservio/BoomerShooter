import pygame

# C

C_WHITE: tuple[int, int, int] = (255,255,255)
C_YELLOW = (201, 220, 72)

# E

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Player1': 100,
    'Enemy1': 100,
    'Enemy2': 100,
    'Asteroid': 50,
    'Asteroid2': 70,
    'Player1Shot': 1,
    'Enemy1Shot': 50,
    'Enemy2Shot': 60,
    'PowerUp': 1
}

ENTITY_SPEED = {
    'Level1Bg0': 1,
    'Level1Bg1': 0,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Player1': 3,
    'Enemy1': 2,
    'Enemy2': 3,
    'Asteroid': 7,
    'Asteroid2': 4,
    'Player1Shot': 4,
    'PowerUp': 1
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Enemy1': 100,
    'Enemy2': 200,
}

EVENT_ENEMY = pygame.USEREVENT + 1

EVENT_POWERUP = pygame.USEREVENT + 2

# M
MENU_MOV = {
    "up": pygame.K_UP,
    "down": pygame.K_DOWN
}


MENU_OPT = ('NEW GAME',
            'HALL OF FAME',
            'EXIT')


# P

PLAYER_KEY_UP = {
    'Player1': pygame.K_w,
}
PLAYER_KEY_DOWN = {
    'Player1': pygame.K_s,
}
PLAYER_KEY_LEFT = {
    'Player1': pygame.K_a,
}
PLAYER_KEY_RIGHT = {
    'Player1': pygame.K_d,
}
PLAYER_KEY_SHOOT = {
    'Player1': pygame.K_SPACE
}

POWERUP_SPAWN_TIME = 1000

# S

SPAWN_TIME = 3000


# W

WINDOW_W = 576
WINDOW_H = 324