from typing import List
from screens.home_screen import HomeScreen
from screens.game_screen import GameScreen
from screens.pause_screen import PauseScreen
from screens.game_over_screen import GameOverScreen
from screens.round_over_screen import RoundOverScreen
from models.player import Player
from models.bubble import Bubble
import consts


class Warfare:
    def __init__(self, py_screen, start_screen: str, width: int, height: int):
        self.py_screen = py_screen
        self.start_screen = start_screen
        self.width = width
        self.height = height

        self.player1: Player = Player(self, consts.Direction.RIGHT, 40, True)
        self.player2 = Player(
            self, consts.Direction.LEFT, consts.SCREEN_WIDTH - 100, False
        )

        self.bubbles: List[Bubble] = []

        self.screens_map = {
            consts.HOME_SCREEN: HomeScreen(self.py_screen, self.width, self.height),
            consts.GAME_SCREEN: GameScreen(
                self.py_screen, self.player1, self.player2, self.bubbles
            ),
            consts.PAUSE_SCREEN: PauseScreen(self.py_screen, self.width, self.height),
            consts.GAME_OVER_SCREEN: GameOverScreen(
                self.py_screen, self.width, self.height
            ),
            consts.ROUND_OVER_SCREEN: RoundOverScreen(self.py_screen, self.width, self.height),
        }
        self.current_screen = self.screens_map[self.start_screen]

    def draw(self, dt):
        self.current_screen.draw(dt)

    def update(self):
        self.current_screen = self.screens_map[self.current_screen.update()]
