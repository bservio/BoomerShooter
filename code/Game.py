import pygame

from code.Const import WINDOW_W, WINDOW_H
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
            main_menu.run()

            pass