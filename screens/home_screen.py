import pygame
import consts
from assets import assets

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
        self.init_button()

    def init_button(self):
        # Create and draw button
        color = (50, 200, 50)
        width = 200
        height = 50
        x = (self.width - width) // 2
        y = self.height // 2
        text = "Start Game"
        # Create button rectangle
        # Add button text

        self.button = pygame.Rect(x, y, width, height)

        font = pygame.font.Font(None, 36)
        self.text_surface = font.render(text, True, (255, 255, 255))
        self.text_surface_rect = self.text_surface.get_rect(center=self.button.center)


    def start_game_button(self) -> bool:
        # Check for mouse click on button
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()[0]

        return self.text_surface_rect.collidepoint(mouse_pos) and mouse_clicked

    def draw(self, dt) -> None:
        self.py_screen.blit(self.background, (0, 0))
        pygame.draw.rect(self.py_screen, (50, 200, 50), self.button)

        if not self.is_playing:
            self.theme.play(-1)
            self.is_playing = True

        self.py_screen.blit(self.text_surface, self.text_surface_rect )

    def update(self):
        if self.start_game_button():
            self.theme.stop()
            return consts.GAME_SCREEN
        return consts.HOME_SCREEN
