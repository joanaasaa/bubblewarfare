import pygame
import consts
from physics_shit.collisions import render_collisions
from typing import List, Tuple
from models.bubble import Bubble
from models.player import Player


class GameScreen:
    def __init__(
            self, py_screen, player1: Player, player2: Player, bubbles: List[Bubble]
    ):
        self.match_scores: List[int] = [0, 0]
        self.bubbles = bubbles
        self.py_screen = py_screen
        self.player1 = player1
        self.player2 = player2
        self.next_screen = consts.GAME_SCREEN

        background = pygame.image.load("assets/images/battle_arena.png")
        self.background = pygame.transform.scale(
            background, (consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT)
        )

    def draw(self, dt):
        self.py_screen.blit(self.background, (0, 0))
        # Update entities
        self.player1.update(dt)
        self.player2.update(dt)
        for b in self.bubbles:
            b.update(dt)
        scores = render_collisions(self.bubbles, self.py_screen)

        self.calculate_scoring(scores)

        # Draw entities
        self.player1.draw(self.py_screen)
        self.player2.draw(self.py_screen)
        for b in self.bubbles:
            b.draw(self.py_screen)
        self.render_match_data()

    def update(self):
        return self.next_screen

    def render_match_data(self):
        myFont = pygame.font.Font("assets/fonts/PixelifySans-Regular.ttf", 100)
        player_1_label = myFont.render('{}'.format(self.player1.score), 1, (255, 0, 0))
        player_2_label = myFont.render('{}'.format(self.player2.score), 1, (255, 0, 0))
        player_1_match_score_label = myFont.render('{}'.format(self.match_scores[0]), 1, (255, 0, 0))
        player_2_match_score_label = myFont.render('{}'.format(self.match_scores[1]), 1, (255, 0, 0))
        self.py_screen.blit(player_1_label, (consts.SCREEN_WIDTH / 2 - 85, 10))
        self.py_screen.blit(player_2_label, (consts.SCREEN_WIDTH / 2 + 40, 10))

        self.py_screen.blit(player_1_match_score_label, (0 / 2 + 45, 10))
        self.py_screen.blit(player_2_match_score_label, (consts.SCREEN_WIDTH - 100, 10))

    def calculate_scoring(self, scores: Tuple[int, int]):
        self.player1.score += scores[0]
        self.player2.score += scores[1]
        if self.player1.score >= consts.MATH_THRESHOLD or self.player2.score >= consts.MATH_THRESHOLD:
            if self.player1.score >= consts.MATH_THRESHOLD:
                self.match_scores[0] += 1
            if self.player2.score >= consts.MATH_THRESHOLD:
                self.match_scores[1] += 1
            self.player1.score = 0
            self.player2.score = 0
