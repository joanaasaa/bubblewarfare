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


def render_collisions(bubbles: List[Bubble], screen: pygame.Surface) -> bool:
    has_collision = False
    for b1, b2 in itertools.combinations(bubbles, 2):
        if not is_colliding(b1, b2):
            continue

        has_collision = True
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
            if b1.momentum().magnitude() > b2.momentum().magnitude():
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
            bubbles.remove(b)
            continue
        if b.radius < 5:
            bubbles.remove(b)
    return has_collision


def is_out_of_bounds(bubble: Bubble, screen: pygame.Surface) -> bool:
    return (
        (bubble.pos.x > screen.get_width() + bubble.radius)
        or (bubble.pos.x < -bubble.radius)
        or (bubble.pos.y > screen.get_height() + bubble.radius)
        or (bubble.pos.y < -bubble.radius)
    )
