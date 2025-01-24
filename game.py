import math
import pygame
from typing import List


class Bubble:
    def __init__(self, init_x, init_y, vel_x, vel_y):
        self.player_pos = pygame.Vector2(init_x, init_y)
        self.player_vel = pygame.Vector2(vel_x, vel_y)
        self.radius: float = 1
        self.visible = False
        self.draw()

    def draw(self):
        if self.visible:
            pygame.draw.circle(screen, "cyan", self.player_pos, self.radius)

    def tick(self):
        self.player_pos += self.player_vel * dt
        self.draw()

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

def is_colliding(b1: Bubble, b2: Bubble) -> bool:
    distX = b1.player_pos.x - b2.player_pos.x
    distY = b1.player_pos.y - b2.player_pos.y
    distance = math.sqrt((distX * distX) + (distY * distY))

    return distance <= b1.radius + b2.radius


def render_collisions(bubbles: List[Bubble]):
    idx = 0
    while idx < len(bubbles):
        idx2 = idx + 1
        if is_out_of_bounds(bubbles[idx]):
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
                    bubbles[idx2].player_vel = (bubbles[idx2].momentum() + bubbles[idx].momentum()) / bubbles[idx2].radius
                    bubbles[idx].radius = 0
                    print(bubbles[idx2].player_vel)
            idx2 += 1
        idx += 1


def is_out_of_bounds(bubble: Bubble) -> bool:
    return (
        (bubble.player_pos.x > screen.get_width() + bubble.radius)
        or (bubble.player_pos.x < -bubble.radius)
        or (bubble.player_pos.y > screen.get_height() + bubble.radius)
        or (bubble.player_pos.y < -bubble.radius)
    )


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running: bool = True

padding: int = 20
player_speed: int = 300
cannon_height: int = 40
cannon_width: int = 40
dt: float = 0

# Player 1
player_1_y: int = screen.get_height() // 2 - cannon_height // 2
player_1_color: pygame.Color = pygame.Color("darkgoldenrod")

# Player 2
player_2_y: int = screen.get_height() // 2 - cannon_height // 2
player_2_color: pygame.Color = pygame.Color("darkolivegreen")

pygame.key.set_repeat()

bubbles: List[Bubble] = []
player_1_bubble: Bubble | None = None
player_2_bubble: Bubble | None = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("gray36")

    pygame.draw.rect(
        screen, player_1_color, [padding, 10 + player_1_y, 40, cannon_height]
    )
    pygame.draw.rect(
        screen,
        player_2_color,
        [
            screen.get_width() - padding - cannon_width,
            10 + player_2_y,
            40,
            cannon_height,
        ],
    )

    keys = pygame.key.get_pressed()

    if player_1_bubble is None:
        if keys[pygame.K_w]:
            player_1_y = max(0, int(player_1_y - player_speed * dt))
        if keys[pygame.K_s]:
            player_1_y = min(
                screen.get_height() - cannon_height - padding,
                int(player_1_y + player_speed * dt),
            )

    if player_2_bubble is None:
        if keys[pygame.K_UP]:
            player_2_y = max(0, int(player_2_y - player_speed * dt))
        if keys[pygame.K_DOWN]:
            player_2_y = min(
                screen.get_height() - cannon_height - padding,
                int(player_2_y + player_speed * dt),
            )

    if keys[pygame.K_d]:
        if player_1_bubble is None:
            player_1_bubble = Bubble(
                padding + cannon_width, player_1_y + cannon_height / 2, 0, 0
            )
        else:
            player_1_bubble.set_visible()
            player_1_bubble.increase_radius()
            player_1_bubble.draw()
    else:
        if player_1_bubble is not None:
            player_1_bubble.set_x_vel(100)
            bubbles.append(player_1_bubble)
            player_1_bubble = None

    if keys[pygame.K_LEFT]:
        if player_2_bubble is None:
            player_2_bubble = Bubble(
                screen.get_width() - padding - cannon_width,
                player_2_y + cannon_height / 2,
                0,
                0,
            )
        else:
            player_2_bubble.set_visible()
            player_2_bubble.increase_radius()
            player_2_bubble.draw()
    else:
        if player_2_bubble is not None:
            player_2_bubble.set_x_vel(-100)
            bubbles.append(player_2_bubble)
            player_2_bubble = None

    for b in bubbles:
        b.tick()
    # flip() the display to put your work on screen
    pygame.display.flip()
    render_collisions(bubbles)
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
