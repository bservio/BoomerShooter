import pygame

# C

C_WHITE = (255,255,255)
C_YELLOW = (201, 220, 72)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)
C_RED = (255, 102, 102)
C_BLACK = (0,0,0)
C_GRAY = (64,64,64)

# E

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Player1': 999,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 25,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 20,
    'Asteroid': 30,
    'Asteroid2': 60,
    'PowerUp': 0,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Player1': 100,
    'Enemy1': 100,
    'Enemy2': 100,
    'Asteroid': 40,
    'Asteroid2': 70,
    'Player1Shot': 1,
    'Enemy1Shot': 50,
    'Enemy2Shot': 60,
    'PowerUp': 1
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Asteroid': 50,
    'Asteroid2': 75,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 100,
    'Enemy2Shot': 0,
    'PowerUp': 0,

}

ENTITY_SPEED = {
    'Level1Bg0': 1,
    'Level1Bg1': 0,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Player1': 3,
    'Enemy1': 2,
    'Enemy1Shot': 6,
    'Enemy2': 3,
    'Asteroid': 7,
    'Asteroid2': 4,
    'Player1Shot': 4,
    'PowerUp': 1
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Enemy1': 50,
    'Enemy2': 35,
}

EVENT_ENEMY = pygame.USEREVENT + 1

EVENT_POWERUP = pygame.USEREVENT + 2

EVENT_TIMEOUT = pygame.USEREVENT + 3

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

SPAWN_TIME = 2500

# T
TIMEOUT_LEVEL = 30000
TIMEOUT_STEP = 100


# W

WINDOW_W = 576
WINDOW_H = 324

SCORE_POS = {'Title': (WINDOW_W / 2, 50),
             'EnterName': (WINDOW_W / 2, 80),
             'Label': (WINDOW_W / 2, 90),
             'Name': (WINDOW_W / 2, 130),
             0: (WINDOW_W / 2, 110),
             1: (WINDOW_W / 2, 130),
             2: (WINDOW_W / 2, 150),
             3: (WINDOW_W / 2, 170),
             4: (WINDOW_W / 2, 190),
             5: (WINDOW_W / 2, 210),
             6: (WINDOW_W / 2, 230),
             7: (WINDOW_W / 2, 250),
             8: (WINDOW_W / 2, 270),
             9: (WINDOW_W / 2, 290),
             }