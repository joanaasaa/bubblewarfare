import pygame as pg
from typing import List, Tuple


def load_sprites(path: str, length: int, size: Tuple[int, int]) -> List[pg.Surface]:
    img: pg.Surface = pg.image.load(path)
    sprites: List[pg.Surface] = []
    for i in range(length):
        sprites.append(clip(img, i * size[0], 0, size[0], size[1]))
    return sprites


def clip(surface: pg.Surface, x: int, y: int, x_size: int, y_size: int) -> pg.Surface:
    handle_surface = surface.copy()
    clipRect = pg.Rect(x, y, x_size, y_size)
    handle_surface.set_clip(clipRect)
    image = surface.subsurface(handle_surface.get_clip())
    return image.copy()
