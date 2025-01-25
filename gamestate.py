from bubble import Bubble
from typing import List
from player import Player
from sprites import Sprites
import consts
import pygame


class Gamestate:
    def __init__(self) -> None:
        # Load sprites
        self.sprites: Sprites = Sprites()

        # Load sounds
        bubble_sounds: List[pygame.mixer.Sound] = [
            pygame.mixer.Sound("assets/sounds/p2.wav"),
            pygame.mixer.Sound("assets/sounds/p2.wav"),
        ]

        self.player1: Player = Player(
            self,
            40,
            consts.SCREEN_HEIGHT,
            bubble_sounds,
            "assets/images/water_gun.png",
            pygame.mixer.Sound("assets/sounds/sound.mp3"),
            self.sprites.bubble,
            True,
        )
        self.player2 = Player(
            self,
            consts.SCREEN_WIDTH - 100,
            consts.SCREEN_HEIGHT,
            bubble_sounds,
            "assets/images/water_gun_reflected.png",
            pygame.mixer.Sound("assets/sounds/sound.mp3"),
            self.sprites.bubble,
            False,
        )
        self.bubbles: List[Bubble] = []

    def add_bubble(self, bubble: Bubble):
        self.bubbles.append(bubble)
