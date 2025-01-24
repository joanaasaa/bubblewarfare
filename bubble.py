import pygame

class Bubble:
    def __init__(self, init_x, init_y, vel_x, vel_y):
        self.player_pos = pygame.Vector2(init_x, init_y)
        self.player_vel = pygame.Vector2(vel_x, vel_y)
        self.radius: float = 1
        self.visible = False

    def draw(self, screen):
        if self.visible:
            pygame.draw.circle(screen, "cyan", self.player_pos, self.radius)

    def tick(self, screen : pygame.Surface, dt : float):
        self.player_pos += self.player_vel * dt
        self.draw(screen)

    def increase_radius(self):
        self.radius += 10 / self.radius

    def set_visible(self):
        self.visible = True

    def set_x_vel(self, new_x_vel):
        self.player_vel.x = new_x_vel

    def momentum(self):
        return self.player_vel * self.mass()

    def mass(self):
        return self.radius ** 2
