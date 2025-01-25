import pygame

from bubble import Bubble
import math
from typing import List


def is_colliding(b1: Bubble, b2: Bubble) -> bool:
    distX = b1.pos.x - b2.pos.x
    distY = b1.pos.y - b2.pos.y
    distance = math.sqrt((distX * distX) + (distY * distY))

    return distance <= b1.radius + b2.radius


def render_collisions(bubbles: List[Bubble], screen: pygame.Surface):
    idx = 0
    while idx < len(bubbles):
        idx2 = idx + 1
        if is_out_of_bounds(bubbles[idx], screen):
            print("OUT OF BOUNDS CARALHO")
            bubbles.remove(bubbles[idx])
            continue
        while idx2 < len(bubbles):
            if is_colliding(bubbles[idx], bubbles[idx2]):
                print("COLLIDING CARALHO")

                if bubbles[idx].momentum().magnitude() > bubbles[idx2].momentum().magnitude():
                    print(bubbles[idx].momentum())
                    print(bubbles[idx2].momentum())
                    bubbles[idx].vel = (bubbles[idx].momentum() + bubbles[idx2].momentum()) / bubbles[idx].mass()
                    print(bubbles[idx].vel)
                    if bubbles[idx].vel.x * bubbles[idx2].vel.x < 0:
                        new_radius = math.sqrt(abs(bubbles[idx].mass() - bubbles[idx2].mass()))
                    else:
                        new_radius = math.sqrt(bubbles[idx].mass() + bubbles[idx2].mass())
                    bubbles[idx].radius = new_radius
                    bubbles[idx2].radius = 0
                elif bubbles[idx].momentum().magnitude() < bubbles[idx2].momentum().magnitude():
                    print(bubbles[idx].momentum())
                    print(bubbles[idx2].momentum())
                    bubbles[idx2].vel = (bubbles[idx2].momentum() + bubbles[idx].momentum()) / bubbles[
                        idx2].mass()

                    if bubbles[idx].vel.x * bubbles[idx2].vel.x < 0:
                        new_radius = math.sqrt(abs(bubbles[idx].mass() - bubbles[idx2].mass()))
                    else:
                        new_radius = math.sqrt(bubbles[idx].mass() + bubbles[idx2].mass())
                    bubbles[idx2].radius = new_radius
                    bubbles[idx].radius = 0
                    print(bubbles[idx2].vel)
            idx2 += 1
        idx += 1
    for b in bubbles:
        if b.radius < 5:
            bubbles.remove(b)


def is_out_of_bounds(bubble: Bubble, screen: pygame.Surface) -> bool:
    return (
            (bubble.pos.x > screen.get_width() + bubble.radius)
            or (bubble.pos.x < -bubble.radius)
            or (bubble.pos.y > screen.get_height() + bubble.radius)
            or (bubble.pos.y < -bubble.radius)
    )
