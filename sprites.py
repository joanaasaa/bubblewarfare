import pygame as pg
from typing import List


class Sprites:
    def __init__(self) -> None:
        # Load bubble sprites
        bubbleSprites: pg.Surface = pg.image.load("assets/images/bubble.png")
        bubbleSprite1: pg.Surface = clip(bubbleSprites, 0, 0, 100, 100)
        bubbleSprite2: pg.Surface = clip(bubbleSprites, 100, 0, 100, 100)
        bubbleSprite3: pg.Surface = clip(bubbleSprites, 200, 0, 100, 100)
        bubbleSprite4: pg.Surface = clip(bubbleSprites, 300, 0, 100, 100)
        bubbleSprite5: pg.Surface = clip(bubbleSprites, 400, 0, 100, 100)
        bubbleSprite6: pg.Surface = clip(bubbleSprites, 500, 0, 100, 100)
        bubbleSprite7: pg.Surface = clip(bubbleSprites, 600, 0, 100, 100)
        bubbleSprite8: pg.Surface = clip(bubbleSprites, 600, 0, 100, 100)
        self.bubble: List[pg.Surface] = [
            bubbleSprite1,
            bubbleSprite2,
            bubbleSprite3,
            bubbleSprite4,
            bubbleSprite5,
            bubbleSprite6,
            bubbleSprite7,
            bubbleSprite8,
        ]


def clip(surface: pg.Surface, x: int, y: int, x_size: int, y_size: int) -> pg.Surface:
    handle_surface = surface.copy()
    clipRect = pg.Rect(x, y, x_size, y_size)
    handle_surface.set_clip(clipRect)
    image = surface.subsurface(handle_surface.get_clip())
    return image.copy()
