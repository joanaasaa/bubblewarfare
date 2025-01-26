import pygame
import consts
from physics_shit.collisions import render_collisions
from typing import List, Tuple
from models.bubble import Bubble
from models.player import Player
from assets import assets


class GameScreen:
    def __init__(
        self,
        py_screen,
        player1: Player,
        player2: Player,
        bubbles: List[Bubble],
    ):
        self.next_screen = consts.GAME_SCREEN
        self.match_scores: List[int] = [0, 0]
        self.bubbles = bubbles
        self.py_screen = py_screen
        self.player1 = player1
        self.player2 = player2
        self.text_colour = (168, 50, 62)

    def draw(self, dt):
        self.py_screen.blit(assets.images.arenas[consts.current_arena], (0, 0))

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
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            return consts.PAUSE_SCREEN

        if self.next_screen is not consts.GAME_SCREEN:
            currScreen = self.next_screen
            self.next_screen = consts.GAME_SCREEN
            return currScreen
        return consts.GAME_SCREEN

    def render_match_data(self):
        myFont = pygame.font.Font("assets/fonts/PixelifySans-Regular.ttf", 100)
        player_1_label = myFont.render(
            "{}".format(self.player1.score), 1, self.text_colour
        )
        player_2_label = myFont.render(
            "{}".format(self.player2.score), 1, self.text_colour
        )
        player_1_match_score_label = myFont.render(
            "{}".format(self.match_scores[0]), 1, self.text_colour
        )
        player_2_match_score_label = myFont.render(
            "{}".format(self.match_scores[1]), 1, self.text_colour
        )

        self.py_screen.blit(player_1_label, (consts.SCREEN_WIDTH / 2 - 85, 10))
        self.py_screen.blit(player_2_label, (consts.SCREEN_WIDTH / 2 + 40, 10))

        self.py_screen.blit(player_1_match_score_label, (0 / 2 + 45, 10))
        self.py_screen.blit(player_2_match_score_label, (consts.SCREEN_WIDTH - 100, 10))

    def end_round(self):
        self.bubbles.clear()
        self.player1.score = 0
        self.player2.score = 0

    def end_match(self):
        self.end_round()
        self.match_scores = [0, 0]

    def is_round_over(self):
        return (
            self.player1.score >= consts.MATH_THRESHOLD
            or self.player2.score >= consts.MATH_THRESHOLD
        )

    def is_game_over(self):
        return (
            self.match_scores[0] == consts.WIN_SCORE
            or self.match_scores[1] == consts.WIN_SCORE
        )

    def calculate_scoring(self, scores: Tuple[int, int]):
        self.player1.score += scores[0]
        self.player2.score += scores[1]

        if self.is_round_over():
            if self.player1.score >= consts.MATH_THRESHOLD:
                self.match_scores[0] += 1
            if self.player2.score >= consts.MATH_THRESHOLD:
                self.match_scores[1] += 1
            self.end_round()
            self.next_screen = consts.ROUND_OVER_SCREEN
        if self.is_game_over():
            if self.match_scores[0] > self.match_scores[1]:
                consts.WINNER = "PLAYER 1"
            else:
                consts.WINNER = "PLAYER 2"
            self.end_match()
            self.next_screen = consts.GAME_OVER_SCREEN
