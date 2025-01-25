import pygame
from typing import List
from assets import assets
import consts
import math
from abc import ABC


class Bubble(ABC):
    def __init__(self, init_x, init_y, vel_x, vel_y):
        self.pos = pygame.Vector2(init_x, init_y)
        self.vel = pygame.Vector2(vel_x, vel_y)
        self.radius: float = 1
        self.sprites: List[pygame.Surface] = assets.water_bubble_sprites
        self.currentSprite: int = 0
        self.sprite_dt = 0
        self.pop_sound = assets.water_bubble_pop_sound

    def draw(self, screen):
        surface = pygame.transform.scale_by(
            self.sprites[self.currentSprite], self.radius / 50
        )
        rect = surface.get_rect(center=(self.pos))
        screen.blit(surface, rect)

    def update(self, dt: float):
        self.pos += self.vel * dt
        self.sprite_dt += dt
        if self.sprite_dt > 0.05:
            self.sprite_dt = 0
            self.currentSprite = (self.currentSprite + 1) % len(self.sprites)

    def increase_radius(self):
        self.radius += 10 / self.radius

    def momentum(self):
        return self.vel * self.mass()

    def mass(self):
        return self.radius**2

    def set_mass(self, mass: float):
        self.radius = math.sqrt(mass)

    def set_momentum(self, momentum: float):
        self.vel = (
            momentum * self.momentum() / (self.mass() * self.momentum().magnitude())
        )

    def direction(self) -> consts.Direction:
        if self.vel.x < 0:
            return consts.Direction.LEFT
        return consts.Direction.RIGHT

    def pop(self):
        self.pop_sound.play()
