from random import randint

from code.Asteroid import Asteroid
from code.Backgroung import Background
from code.Const import WINDOW_W, WINDOW_H
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'Level1Bg{i}', (0,0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WINDOW_W,0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, (WINDOW_H/2)))

            case 'Enemy1':
                return  Enemy('Enemy1', (WINDOW_W + 10, randint(40, WINDOW_H)-40))

            case 'Enemy2':
                return Enemy('Enemy2', (WINDOW_W + 10, randint(40, WINDOW_H) - 40))

            case 'Asteroid':
                return Asteroid('Asteroid', (WINDOW_W + 10, randint(40, WINDOW_H) - 40))

            case 'Asteroid2':
                return Asteroid('Asteroid2', (WINDOW_W + 10, randint(40, WINDOW_H) - 40))