import pygame
from typing import List


class Bubble:
    def __init__(self, init_x, init_y, vel_x, vel_y, sprite: List[pygame.Surface]):
        self.pos = pygame.Vector2(init_x, init_y)
        self.vel = pygame.Vector2(vel_x, vel_y)
        self.radius: float = 1
        self.visible = False
        self.sprites: List[pygame.Surface] = sprite
        self.currentSprite: int = 0
        self.sprite_dt = 0

    def draw(self, screen):
        if self.visible:
            surface = pygame.transform.scale_by(
                self.sprites[self.currentSprite], self.radius / 50
            )
            rect = surface.get_rect(center=(self.pos))
            screen.blit(surface, rect)
            # pygame.draw.circle(screen, "black", self.player_pos, self.radius)

    def tick(self, dt: float):
        self.pos += self.vel * dt
        self.sprite_dt += dt
        if self.sprite_dt > 0.05:
            self.sprite_dt = 0
            self.currentSprite = (self.currentSprite + 1) % len(self.sprites)

    def increase_radius(self):
        self.radius += 10 / self.radius

    def set_visible(self):
        self.visible = True

    def set_x_vel(self, new_x_vel):
        self.vel.x = new_x_vel

    def momentum(self):
        return self.vel * self.mass()

    def mass(self):
        return self.radius**2
