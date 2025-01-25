from bubble import Bubble
from typing import List, Tuple
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

        collision_sound = pygame.mixer.Sound("assets/sounds/collision.wav")

        self.player1: Player = Player(
            self,
            40,
            consts.SCREEN_HEIGHT,
            bubble_sounds,
            "assets/images/water_gun.png",
            pygame.mixer.Sound("assets/sounds/sound.mp3"),
            self.sprites.bubble,
            True,
            collision_sound
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
            collision_sound
        )
        self.bubbles: List[Bubble] = []

    def add_bubble(self, bubble: Bubble):
        self.bubbles.append(bubble)

    def render_match_data(self, screen):
        black = (0, 0, 0)
        myFont = pygame.font.SysFont("Times New Roman", 100)
        player_1_label = myFont.render('{}'.format(self.player1.score), 1, black)
        player_2_label = myFont.render('{}'.format(self.player2.score), 1, black)
        screen.blit(player_1_label, (15, 10))
        screen.blit(player_2_label, (consts.SCREEN_WIDTH - 100, 10))

    def update_scores(self, scores : Tuple[int, int]):
        self.player1.score += scores[0]
        self.player2.score += scores[1]
