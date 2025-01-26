import pygame
from typing import List
from assets import assets

import math
import consts
from abc import ABC, abstractmethod


class Bubble(ABC):
    def __init__(self, init_x, init_y, vel_x, vel_y):
        self.pos = pygame.Vector2(init_x, init_y)
        self.vel = pygame.Vector2(vel_x, vel_y)
        self.radius: float = 1

        self.sprites: List[pygame.Surface]
        self.pop_sound = assets.sounds.watergrass_pop
        self.currentSprite: int = 0
        self.sprite_dt = 0

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

    def set_vel(self, vel_2: pygame.Vector2, m_2: int, combined):
        self.vel.x = (self.mass() * self.vel.x + m_2 * vel_2.x) / combined
        self.vel.y = (self.mass() * self.vel.y + m_2 * vel_2.y) / combined

    def direction(self) -> consts.Direction:
        if self.vel.x < 0:
            return consts.Direction.LEFT
        return consts.Direction.RIGHT

    @abstractmethod
    def increase_radius(self):
        self.radius += 10 / self.radius

    @abstractmethod
    def pop(self):
        self.pop_sound.play()


class WaterBubble(Bubble):
    def __init__(self, init_x, init_y, vel_x, vel_y):
        super().__init__(init_x, init_y, vel_x, vel_y)
        self.sprites: List[pygame.Surface] = assets.images.water_bubble_sprites
        self.pop_sound = assets.sounds.watergrass_pop

    def increase_radius(self):
        self.radius += 10 / self.radius

    def pop(self):
        return super().pop()


class GrassBubble(Bubble):
    def __init__(self, init_x, init_y, vel_x, vel_y):
        super().__init__(init_x, init_y, vel_x, vel_y)
        self.sprites: List[pygame.Surface] = assets.images.grass_bubble_sprites
        self.pop_sound = assets.sounds.watergrass_pop

    def increase_radius(self):
        self.radius += 10 / self.radius

    def pop(self):
        return super().pop()


class FireBubble(Bubble):
    def __init__(self, init_x, init_y, vel_x, vel_y):
        super().__init__(init_x, init_y, vel_x, vel_y)
        self.sprites: List[pygame.Surface] = assets.images.fire_bubble_sprites
        self.pop_sound = assets.sounds.watergrass_pop

    def increase_radius(self):
        self.radius += 10 / self.radius

    def pop(self):
        return super().pop()
