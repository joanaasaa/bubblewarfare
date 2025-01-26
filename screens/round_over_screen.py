import pygame
import consts
from assets import assets


class RoundOverScreen:
    def __init__(self, py_screen, width, height) -> None:
        self.width = width
        self.height = height
        self.py_screen = py_screen
        self.theme = assets.sounds.pause_theme
        self.is_playing = False

    def draw(self, dt) -> None:
        if not self.is_playing:
            self.theme.play(-1)
            self.is_playing = True

        myFont = pygame.font.Font("assets/fonts/PixelifySans-Regular.ttf", 180)
        player_1_label = myFont.render('{}'.format("ROUND OVER"), 1, (168, 50, 62))
        self.py_screen.blit(player_1_label, (130, consts.SCREEN_HEIGHT / 2 - 130))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_n]:
            self.theme.stop()
            self.is_playing = False
            return consts.GAME_SCREEN

        return consts.ROUND_OVER_SCREEN
