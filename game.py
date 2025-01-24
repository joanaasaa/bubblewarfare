import pygame
from typing import List
from bubble import Bubble
import collisions

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
            player_1_bubble.draw(screen)
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
            player_2_bubble.draw(screen)
    else:
        if player_2_bubble is not None:
            player_2_bubble.set_x_vel(-100)
            bubbles.append(player_2_bubble)
            player_2_bubble = None

    for b in bubbles:
        b.tick(screen, dt)
    # flip() the display to put your work on screen
    pygame.display.flip()
    collisions.render_collisions(bubbles, screen)
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
