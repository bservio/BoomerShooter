import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_WHITE, WINDOW_W, WINDOW_H, C_YELLOW, C_RED


class GameOverScreen:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/GameOverScreen.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./assets/Menu.wav')
        pygame.mixer_music.play(-1)
        pygame.mixer.music.set_volume(0.1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, 'GAME', C_RED, ((WINDOW_W / 2), 70), )
            self.menu_text(50, 'OVER', C_RED, ((WINDOW_W / 2), 120),  underline=True)
            self.menu_text(15, 'PRESS ANY KEY TO GO TO HOME SCREEN', C_YELLOW, ((WINDOW_W / 2), 200))
            self.menu_text(10, 'Desenvolvido por Bruno Sérvio [RA 4514699]', C_WHITE, ((WINDOW_W / 2), WINDOW_H - 10))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:  # Qualquer tecla pressionada
                    return  # Sai do menu (pode ir para o menu principal)

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, italic=False,
                  underline=False):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_font.set_italic(italic)
        text_font.set_underline(underline)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
