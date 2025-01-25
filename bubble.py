import pygame


class Bubble:
    def __init__(self, x, y, vel_x, vel_y):
        self.pos = pygame.Vector2(x, y)
        self.vel = pygame.Vector2(vel_x, vel_y)
        self.radius: float = 1

    def draw(self, screen):
        pygame.draw.circle(screen, "cyan", self.pos, self.radius)

    def tick(self, screen: pygame.Surface, dt: float):
        self.pos += self.vel * dt
        self.draw(screen)

    def increase_radius(self):
        self.radius += 10 / self.radius

    def set_x_vel(self, new_x_vel):
        self.vel.x = new_x_vel

    def momentum(self):
        return self.vel * self.mass()

    def mass(self):
        return self.radius ** 2 
