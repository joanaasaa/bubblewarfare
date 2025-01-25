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

        self.player1: Player = Player(
            self,
            consts.Direction.RIGHT,
            40,
            self.sprites.bubble,
            True,
        )
        self.player2 = Player(
            self,
            consts.Direction.LEFT,
            consts.SCREEN_WIDTH - 100,
            self.sprites.bubble,
            False,
        )
        self.bubbles: List[Bubble] = []
        self.match_scores: List[int] = [0, 0]

    def add_bubble(self, bubble: Bubble):
        self.bubbles.append(bubble)

    def render_match_data(self, screen):
        myFont = pygame.font.Font("assets/fonts/PixelifySans-Regular.ttf", 100)
        player_1_label = myFont.render("{}".format(self.player1.score), 1, (255, 0, 0))
        player_2_label = myFont.render("{}".format(self.player2.score), 1, (255, 0, 0))
        player_1_match_score_label = myFont.render(
            "{}".format(self.match_scores[0]), 1, (255, 0, 0)
        )
        player_2_match_score_label = myFont.render(
            "{}".format(self.match_scores[1]), 1, (255, 0, 0)
        )
        screen.blit(player_1_label, (consts.SCREEN_WIDTH / 2 - 85, 10))
        screen.blit(player_2_label, (consts.SCREEN_WIDTH / 2 + 40, 10))

        screen.blit(player_1_match_score_label, (0 / 2 + 45, 10))
        screen.blit(player_2_match_score_label, (consts.SCREEN_WIDTH - 100, 10))

    def calculate_scoring(self, scores: Tuple[int, int]):
        self.player1.score += scores[0]
        self.player2.score += scores[1]
        if (
            self.player1.score >= consts.MATH_THRESHOLD
            or self.player2.score >= consts.MATH_THRESHOLD
        ):
            if self.player1.score >= consts.MATH_THRESHOLD:
                self.match_scores[0] += 1
            if self.player2.score >= consts.MATH_THRESHOLD:
                self.match_scores[1] += 1
            self.player1.score = 0
            self.player2.score = 0
