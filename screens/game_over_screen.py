import pygame
import consts
from physics_shit.collisions import render_collisions
from typing import List, Tuple
from models.bubble import Bubble
from models.player import Player


class GameOverScreen:
    def __init__(self, py_screen, width, height) -> None:
        self.winner_surface_rect = None
        self.winner_surface = None
        self.winner = None
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
        self.init_winner_label("")

    def init_winner_label(self, winner : str):
        # Create and draw button
        color = (50, 200, 50)
        width = 200
        height = 50
        x = (self.width - width) // 2
        y = self.height * 1 / 4
        text = consts.WINNER
        # Create button rectangle
        # Add button text

        self.winner = pygame.Rect(x, y, width, height)

        font = pygame.font.Font(None, 36)
        self.winner_surface = font.render(text, True, (255, 255, 255))
        self.winner_surface_rect = self.winner_surface.get_rect(center=self.winner.center)

    def init_button(self):
        # Create and draw button
        color = (50, 200, 50)
        width = 200
        height = 50
        x = (self.width - width) // 2
        y = self.height * 3 / 4
        text = "End Game"
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
        self.init_winner_label(consts.WINNER)
        self.py_screen.blit(self.background, (0, 0))
        pygame.draw.rect(self.py_screen, (50, 200, 50), self.button)
        pygame.draw.rect(self.py_screen, (50, 200, 50), self.winner)

        self.py_screen.blit(self.text_surface, self.text_surface_rect)
        self.py_screen.blit(self.winner_surface, self.winner_surface_rect)

    def update(self):
        if self.start_game_button():
            return consts.HOME_SCREEN
        return consts.GAME_OVER_SCREEN
