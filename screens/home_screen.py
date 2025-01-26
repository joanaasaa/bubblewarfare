import pygame
import consts
from assets import assets


def start_game_button() -> bool:
    keys = pygame.key.get_pressed()
    return keys[pygame.K_SPACE]


class HomeScreen:
    def __init__(self, py_screen, width, height) -> None:
        self.text_surface_rect = None
        self.button = None
        self.text_surface = None
        self.width = width
        self.height = height
        self.background = assets.images.bubble_warfare_background
        self.py_screen = py_screen
        self.next_screen = consts.HOME_SCREEN
        self.theme = assets.sounds.home_theme
        self.is_playing = False

    def draw(self, dt) -> None:
        self.py_screen.blit(self.background, (0, 0))

        myFont = pygame.font.Font("assets/fonts/PixelifySans-Bold.ttf", 90)
        start_label = myFont.render("Press Space to Start!", 1, (255,255,255))
        self.py_screen.blit(start_label, (130, consts.SCREEN_HEIGHT / 2 + 130))
        if not self.is_playing:
            self.theme.play(-1)
            self.is_playing = True

    def update(self):
        if start_game_button():
            self.theme.stop()
            return consts.GAME_SELECTION_SCREEN
        return consts.HOME_SCREEN
