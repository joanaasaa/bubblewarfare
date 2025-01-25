import pygame
import consts
from physics_shit.collisions import render_collisions
from typing import List
from models.bubble import Bubble
from models.player import Player


class GameScreen:
    def __init__(
        self, py_screen, player1: Player, player2: Player, bubbles: List[Bubble]
    ):
        self.bubbles = bubbles
        self.py_screen = py_screen
        self.player1 = player1
        self.player2 = player2
        self.next_screen = consts.GAME_SCREEN

        background = pygame.image.load("assets/images/battle_arena.png")
        self.background = pygame.transform.scale(
            background, (consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT)
        )

        self.collision_sound = pygame.mixer.Sound("assets/sounds/collision.wav")

    def draw(self, dt):
        self.py_screen.blit(self.background, (0, 0))
        # Update entities
        self.player1.update(dt)
        self.player2.update(dt)
        for b in self.bubbles:
            b.update(dt)
        if render_collisions(self.bubbles, self.py_screen):
            self.collision_sound.play()

        # Draw entities
        self.player1.draw(self.py_screen)
        self.player2.draw(self.py_screen)
        for b in self.bubbles:
            b.draw(self.py_screen)

    def update(self):
        return self.next_screen
