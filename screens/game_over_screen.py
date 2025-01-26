import pygame
import consts
from assets import assets
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
        self.button_text_colour = (255, 255, 255)
        self.button_background_colour = (38, 38, 38)
        self.text_surface = None
        self.width = width
        self.height = height

        self.py_screen = py_screen
        self.init_home_button()
        self.init_winner_label()
        self.player_1_wins_sound: pygame.mixer.Sound = assets.sounds.player_1_wins
        self.player_2_wins_sound: pygame.mixer.Sound = assets.sounds.player_2_wins
        self.winner_declared = False

    def init_winner_label(self):
        # Create and draw button
        width = 200
        height = 50
        x = consts.SCREEN_WIDTH * 3/4 - (200)
        y = self.height * 3 / 4
        text = "Restart"
        # Create button rectangle
        # Add button text

        self.winner = pygame.Rect(x, y, width, height)

        font = pygame.font.Font(None, 36)
        self.winner_surface = font.render(text, True, self.button_text_colour)
        self.winner_surface_rect = self.winner_surface.get_rect(center=self.winner.center)

    def init_home_button(self):
        # Create and draw button
        color = (50, 200, 50)
        width = 200
        height = 50
        x = consts.SCREEN_WIDTH * 1/4
        y = self.height * 3 / 4
        text = "Home"
        # Create button rectangle
        # Add button text

        self.button = pygame.Rect(x, y, width, height)

        font = pygame.font.Font(None, 36)
        self.text_surface = font.render(text, True, (255, 255, 255))
        self.text_surface_rect = self.text_surface.get_rect(center=self.button.center)

    def home_screen_clicked(self) -> bool:
        # Check for mouse click on button
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()[0]

        return self.text_surface_rect.collidepoint(mouse_pos) and mouse_clicked
    def restart_screen_clicked(self) -> bool:
        # Check for mouse click on button
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()[0]

        return self.winner_surface_rect.collidepoint(mouse_pos) and mouse_clicked

    def declare_winner(self):
        if not self.winner_declared:
            if consts.WINNER == "PLAYER 1":
                self.player_1_wins_sound.play()
            else:
                self.player_2_wins_sound.play()
        self.winner_declared = True

    def draw(self, dt) -> None:
        self.declare_winner()
        self.init_winner_label()
        # self.py_screen.blit(self.background, (0, 0))
        pygame.draw.rect(self.py_screen, self.button_background_colour, self.button)
        pygame.draw.rect(self.py_screen, self.button_background_colour, self.winner)

        self.py_screen.blit(self.text_surface, self.text_surface_rect)
        self.py_screen.blit(self.winner_surface, self.winner_surface_rect)
        myFont = pygame.font.Font("assets/fonts/PixelifySans-Regular.ttf", 140)
        player_1_label = myFont.render('{} WINS!'.format(consts.WINNER), 1, (38, 38, 38))
        self.py_screen.blit(player_1_label, (140, consts.SCREEN_HEIGHT / 2 - 100))

    def update(self):
        if self.home_screen_clicked():
            self.winner_declared = False
            return consts.HOME_SCREEN
        elif self.restart_screen_clicked():
            self.winner_declared = False
            return consts.GAME_SELECTION_SCREEN
        return consts.GAME_OVER_SCREEN
