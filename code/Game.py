import pygame

from code.Const import WINDOW_W, WINDOW_H, MENU_OPT
from code.Level import Level
from code.Menu import Menu
from code.WelcomeScreen import WelcomeScreen


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOW_W, WINDOW_H))

    def run(self):
        while True:
            welcome_screen = WelcomeScreen(self.window)
            welcome_screen.run()
            main_menu = Menu(self.window)
            menu_return = main_menu.run()

            if menu_return == MENU_OPT[0]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPT[2]:
                pygame.quit()
                quit()

            pass