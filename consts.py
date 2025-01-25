from enum import Enum

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
CANNON_WIDTH = 40
CANNON_HEIGHT = 40
PADDING = 20
MATH_THRESHOLD = 10


class Direction(Enum):
    RIGHT = 1
    LEFT = -1


HOME_SCREEN = "home_screen"
GAME_SCREEN = "game_screen"
