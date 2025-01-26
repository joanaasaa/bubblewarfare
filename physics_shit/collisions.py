from models.bubble import Bubble

import math
import pygame
from typing import List, Tuple
import itertools
import consts


def is_colliding(b1: Bubble, b2: Bubble) -> bool:
    distX = b1.pos.x - b2.pos.x
    distY = b1.pos.y - b2.pos.y
    distance = math.sqrt((distX * distX) + (distY * distY))

    is_colliding = distance <= b1.radius + b2.radius
    return is_colliding


def render_collisions(bubbles: List[Bubble], screen: pygame.Surface) -> Tuple[int, int]:
    score_1 = 0
    score_2 = 0
    for b1, b2 in itertools.combinations(bubbles, 2):
        if not is_colliding(b1, b2):
            continue
        # colliding wall
        combined_mass = b1.mass() + b2.mass()
        if b1.direction() == b2.direction():
            new_mass = b1.mass() + b2.mass()
            b1.pos = pygame.Vector2(
                (b1.mass() * b1.pos.x + b2.mass() * b2.pos.x) / (new_mass),
                (b1.mass() * b1.pos.y + b2.mass() * b2.pos.y) / (new_mass),
            )
            b1.set_mass(new_mass)
            b1.set_vel(b2.vel, b2.mass(), combined_mass)
            bubbles.remove(b2)
        else:
            if abs(b1.momentum().magnitude() - b2.momentum().magnitude()) < 5:
                b1.pop()
                bubbles.remove(b1)
                b2.pop()
                bubbles.remove(b2)
            elif b1.momentum().magnitude() > b2.momentum().magnitude():
                b1.set_vel(b2.vel, b2.mass(), combined_mass)
                b1.pos = pygame.Vector2(
                    (b1.mass() * b1.pos.x + b2.mass() * b2.pos.x) / (combined_mass),
                    (b1.mass() * b1.pos.y + b2.mass() * b2.pos.y) / (combined_mass),
                )
                b1.set_mass(combined_mass)
                b2.pop()
                bubbles.remove(b2)
            else:
                b2.set_vel(b1.vel, b1.mass(), combined_mass)
                b2.pos = pygame.Vector2(
                    (b1.mass() * b1.pos.x + b2.mass() * b2.pos.x) / (combined_mass),
                    (b1.mass() * b1.pos.y + b2.mass() * b2.pos.y) / (combined_mass),
                )
                b2.set_mass(combined_mass)
                b1.pop()
                bubbles.remove(b1)

    i = 0
    while i < len(bubbles):
        b = bubbles[i]
        match is_out_of_bounds(b, screen):
            case consts.Bounds.RIGHT:
                score_1 += 1
                bubbles.remove(b)
                continue
            case consts.Bounds.LEFT:
                score_2 += 1
                bubbles.remove(b)
                continue
            case consts.Bounds.UP:
                b.vel.y = -b.vel.y
            case consts.Bounds.DOWN:
                b.vel.y = -b.vel.y
        i += 1

    return score_1, score_2


def check_score(bubble: Bubble, screen: pygame.Surface) -> int:
    if bubble.pos.x > screen.get_width() + bubble.radius:
        return 1
    elif bubble.pos.x < -bubble.radius:
        return -1
    return 0


def is_out_of_bounds(bubble: Bubble, screen: pygame.Surface) -> consts.Bounds:
    if bubble.pos.x > screen.get_width() + bubble.radius:
        return consts.Bounds.RIGHT
    elif bubble.pos.x < -bubble.radius:
        return consts.Bounds.LEFT
    elif bubble.pos.y + bubble.radius > screen.get_height():
        return consts.Bounds.DOWN
    elif bubble.pos.y - bubble.radius < 0:
        return consts.Bounds.UP
    return consts.Bounds.NONE
