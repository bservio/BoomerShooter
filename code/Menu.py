import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import MENU_OPT, C_WHITE, WINDOW_W


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/MainBG.png')
        self.rect = self.surf.get_rect(left=0, top=0)


    def run(self):
        pygame.mixer_music.load('./assets/Menu.wav')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            for i in range(len(MENU_OPT)):
                self.menu_text(25, MENU_OPT[i], C_WHITE, ((WINDOW_W / 2), 120 + 40 * i))


            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, italic=False,
                  set_bold=False):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_font.set_italic(italic)
        text_font.set_underline(set_bold)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)