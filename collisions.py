import pygame

from bubble import Bubble
import math
from typing import List


def is_colliding(b1: Bubble, b2: Bubble) -> bool:
    distX = b1.player_pos.x - b2.player_pos.x
    distY = b1.player_pos.y - b2.player_pos.y
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
                radius_res = abs(bubbles[idx].radius - bubbles[idx2].radius)
                if radius_res < 5:
                    bubbles[idx].radius = 0
                    bubbles[idx2].radius = 0
                elif bubbles[idx].momentum().magnitude() > bubbles[idx2].momentum().magnitude():
                    print(bubbles[idx].momentum())
                    print(bubbles[idx2].momentum())
                    bubbles[idx].player_vel = (bubbles[idx].momentum() + bubbles[idx2].momentum()) / bubbles[idx].radius
                    print(bubbles[idx].player_vel)
                    bubbles[idx2].radius = 0
                elif bubbles[idx].momentum().magnitude() < bubbles[idx2].momentum().magnitude():
                    print(bubbles[idx].momentum())
                    print(bubbles[idx2].momentum())
                    bubbles[idx2].player_vel = (bubbles[idx2].momentum() + bubbles[idx].momentum()) / bubbles[
                        idx2].radius
                    bubbles[idx].radius = 0
                    print(bubbles[idx2].player_vel)
            idx2 += 1
        idx += 1


def is_out_of_bounds(bubble: Bubble, screen: pygame.Surface) -> bool:
    return (
            (bubble.player_pos.x > screen.get_width() + bubble.radius)
            or (bubble.player_pos.x < -bubble.radius)
            or (bubble.player_pos.y > screen.get_height() + bubble.radius)
            or (bubble.player_pos.y < -bubble.radius)
    )
