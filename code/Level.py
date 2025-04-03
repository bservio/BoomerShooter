import sys
import random

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_WHITE, WINDOW_H, EVENT_ENEMY, SPAWN_TIME, EVENT_POWERUP, POWERUP_SPAWN_TIME, C_GREEN, \
    TIMEOUT_LEVEL, EVENT_TIMEOUT, TIMEOUT_STEP
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player
from code.PowerUp import PowerUp


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: int):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        player = EntityFactory.get_entity('Player1')
        player.score = player_score
        self.entity_list.append(player)
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_POWERUP, POWERUP_SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: int):
        pygame.mixer_music.load(f'./assets/{self.name}.wav')
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.1)
        clock = pygame.time.Clock()
        power_up_in_screen = 0
        while True:
            clock.tick(60)
            events = pygame.event.get()
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot(events)
                    if shoot is not None:
                        self.entity_list.append(shoot)

                if ent.name == 'Player1':
                    self.level_text(14, f'Player1 - Health: {ent.health} | Score: {ent.score}', C_GREEN, (10, 25))

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    enemy_list = ('Asteroid', 'Asteroid2', 'Enemy1')
                    random_enemy = random.choices(enemy_list, weights=[33, 33, 33])[0]
                    self.entity_list.append(EntityFactory.get_entity(random_enemy))
                if event.type == EVENT_POWERUP and power_up_in_screen == 0:
                    self.entity_list.append((EntityFactory.get_entity('PowerUp')))
                    power_up_in_screen += 1
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player):
                                player_score = ent.score
                        return True
                player_found = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        player_found = True
                if not player_found:
                    return False

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', C_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps() :.0f}', C_WHITE, (10, WINDOW_H - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WINDOW_H - 20))
            pygame.display.flip()

            # Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
