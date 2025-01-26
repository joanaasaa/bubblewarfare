import pygame
import consts
from assets import assets

class PauseScreen:
    def __init__(self, py_screen, width, height) -> None:
        self.width = width
        self.height = height
        self.background = assets.images.pause_background
        self.py_screen = py_screen
        self.theme = assets.sounds.pause_theme
        self.is_playing = False



    def draw(self, dt) -> None:
        if not self.is_playing:
            self.theme.play(-1)
            self.is_playing = True

        # Calculate center position
        bg_width = self.background.get_width()
        bg_height = self.background.get_height()
        x = (self.width - bg_width) // 2
        y = (self.height - bg_height) // 2
        self.py_screen.blit(self.background, (x, y))
        
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_n]:
            self.theme.stop()
            self.is_playing = False
            return consts.GAME_SCREEN
        
        return consts.PAUSE_SCREEN

