from bubble import Bubble
import math
import pygame
from typing import List
import itertools


def is_colliding(b1: Bubble, b2: Bubble) -> bool:
    distX = b1.pos.x - b2.pos.x
    distY = b1.pos.y - b2.pos.y
    distance = math.sqrt((distX * distX) + (distY * distY))

    is_colliding = distance <= b1.radius + b2.radius
    return is_colliding


def render_collisions(bubbles: List[Bubble], screen: pygame.Surface) -> (int, int):
    score_1 = 0
    score_2 = 0
    for b1, b2 in itertools.combinations(bubbles, 2):
        if not is_colliding(b1, b2):
            continue
        if b1.direction() == b2.direction():
            new_mass = b1.mass() + b2.mass()
            new_momentum = b1.momentum().magnitude() + b2.momentum().magnitude()
            b1.pos = pygame.Vector2(
                (b1.mass() * b1.pos.x + b2.mass() * b2.pos.x) / (new_mass),
                (b1.mass() * b1.pos.y + b2.mass() * b2.pos.y) / (new_mass),
            )
            b1.set_mass(new_mass)
            b1.set_momentum(new_momentum)
            b2.set_mass(0)
        else:
            combined_mass = b1.mass() + b2.mass()
            if abs(b1.momentum().magnitude() - b2.momentum().magnitude()) < 10:
                b2.set_mass(0)
                b1.set_mass(0)
            elif b1.momentum().magnitude() > b2.momentum().magnitude():
                b1.set_momentum(b1.momentum().magnitude() - b2.momentum().magnitude())
                b1.pos = pygame.Vector2(
                    (b1.mass() * b1.pos.x + b2.mass() * b2.pos.x) / (combined_mass),
                    (b1.mass() * b1.pos.y + b2.mass() * b2.pos.y) / (combined_mass),
                )
                b2.set_mass(0)
            else:
                b2.set_momentum(b2.momentum().magnitude() - b1.momentum().magnitude())
                b2.pos = pygame.Vector2(
                    (b1.mass() * b1.pos.x + b2.mass() * b2.pos.x) / (combined_mass),
                    (b1.mass() * b1.pos.y + b2.mass() * b2.pos.y) / (combined_mass),
                )
                b1.set_mass(0)

    for b in bubbles:
        if is_out_of_bounds(b, screen):
            won = check_score(b, screen)
            if won > 0:
                score_1 += 1
            elif won < 0:
                score_2 += 1
            bubbles.remove(b)
            continue
        if b.radius < 5:
            b.pop()
            bubbles.remove(b)

    return score_1, score_2


def is_out_of_bounds(bubble: Bubble, screen: pygame.Surface) -> bool:
    return (
            (bubble.pos.x > screen.get_width() + bubble.radius)
            or (bubble.pos.x < -bubble.radius)
            or (bubble.pos.y > screen.get_height() + bubble.radius)
            or (bubble.pos.y < -bubble.radius)
    )


def check_score(bubble: Bubble, screen: pygame.Surface) -> int:
    if bubble.pos.x > screen.get_width() + bubble.radius:
        return 1
    elif bubble.pos.x < -bubble.radius:
        return -1
    return 0
