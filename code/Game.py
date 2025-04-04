import pygame

from code.Const import WINDOW_W, WINDOW_H, MENU_OPT
from code.GameOverScreen import GameOverScreen
from code.Level import Level
from code.Menu import Menu
from code.Score import Score
from code.WelcomeScreen import WelcomeScreen


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOW_W, WINDOW_H))

    def run(self):
        while True:
            score = Score(self.window)
            welcome_screen = WelcomeScreen(self.window)
            welcome_screen.run()
            main_menu = Menu(self.window)
            menu_return = main_menu.run()

            if menu_return == MENU_OPT[0]:
                player_score = 0
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return, player_score = level.run()

                if level_return:
                    score.save(menu_return, player_score)

                else:
                    game_over_screen = GameOverScreen(self.window)
                    game_over_screen.run()

            elif menu_return == MENU_OPT[1]:
                score.show()

            elif menu_return == MENU_OPT[2]:
                pygame.quit()
                quit()

            pass