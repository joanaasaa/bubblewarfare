from enum import Enum

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
CANNON_WIDTH = 40
CANNON_HEIGHT = 40
PADDING = 20
MATH_THRESHOLD = 25
WIN_SCORE = 2


class Direction(Enum):
    RIGHT = 1
    LEFT = -1


class Bounds(Enum):
    NONE = 0
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


# switch it up like nintendo ;)
HOME_SCREEN = "home_screen"
GAME_SCREEN = "game_screen"
PAUSE_SCREEN = "pause_screen"
GAME_OVER_SCREEN = "game_over_screen"
GAME_SELECTION_SCREEN = "game_selection_screen"
ROUND_OVER_SCREEN = "round_over_screen"

WINNER = ""


current_arena = 0
