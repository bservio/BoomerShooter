from code.Backgroung import Background
from code.Const import WINDOW_W, WINDOW_H
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
