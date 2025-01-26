import pygame
import consts
from physics_shit.collisions import render_collisions
from typing import List, Tuple
from models.bubble import Bubble
from models.player import Player


class GameOverScreen:
    def __init__(self, py_screen, width, height) -> None:
        self.text_surface_rect = None
        self.button = None
        self.text_surface = None
        self.width = width
        self.height = height
        self.background = pygame.transform.scale(
            pygame.image.load("assets/images/bubble_warfare.png"),
            (self.width, self.height),
        )
        self.py_screen = py_screen
        self.init_button()

    def init_button(self):
        # Create and draw button
        color = (50, 200, 50)
        width = 200
        height = 50
        x = (self.width - width) // 2
        y = self.height // 2
        text = "End Game"
        # Create button rectangle
        # Add button text

        self.button = pygame.Rect(x, y, width, height)

        font = pygame.font.Font(None, 36)
        self.text_surface = font.render(text, True, (255, 255, 255))
        self.text_surface_rect = self.text_surface.get_rect(center=self.button.center)


    def start_game_button(self) -> bool:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            return True
        return False

    def draw(self, dt) -> None:
        self.py_screen.blit(self.background, (0, 0))
        pygame.draw.rect(self.py_screen, (50, 200, 50), self.button)

        self.py_screen.blit(self.text_surface, self.text_surface_rect )


    def update(self):
        if self.start_game_button():
            return consts.HOME_SCREEN
        return consts.GAME_OVER_SCREEN
