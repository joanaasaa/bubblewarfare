from bubble import Bubble
from typing import List


class Gamestate:
    def __init__(self) -> None:
        self.bubbles: List[Bubble] = []

    def add_bubble(self, bubble: Bubble):
        self.bubbles.append(bubble)
