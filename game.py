import math
import pygame
from typing import List
from gamestate import Gamestate
from sprites import Sprites
from bubble import Bubble
from player import Player


def is_colliding(b1: Bubble, b2: Bubble) -> bool:
    distX = b1.pos.x - b2.pos.x
    distY = b1.pos.y - b2.pos.y
    distance = math.sqrt((distX * distX) + (distY * distY))

    is_colliding = distance <= b1.radius + b2.radius
    if is_colliding:
        collision_sound.play()

    return is_colliding


def render_collisions(bubbles: List[Bubble], screen: pygame.Surface):
    idx = 0
    while idx < len(bubbles):
        idx2 = idx + 1
        if is_out_of_bounds(bubbles[idx], screen):
            bubbles.remove(bubbles[idx])
            continue
        while idx2 < len(bubbles):
            if is_colliding(bubbles[idx], bubbles[idx2]):
                if (
                    bubbles[idx].momentum().magnitude()
                    > bubbles[idx2].momentum().magnitude()
                ):
                    bubbles[idx].vel = (
                        bubbles[idx].momentum() + bubbles[idx2].momentum()
                    ) / bubbles[idx].mass()
                    if bubbles[idx].vel.x * bubbles[idx2].vel.x < 0:
                        new_radius = math.sqrt(
                            abs(bubbles[idx].mass() - bubbles[idx2].mass())
                        )
                    else:
                        new_radius = math.sqrt(
                            bubbles[idx].mass() + bubbles[idx2].mass()
                        )
                    bubbles[idx].radius = new_radius
                    bubbles[idx2].radius = 0
                elif (
                    bubbles[idx].momentum().magnitude()
                    < bubbles[idx2].momentum().magnitude()
                ):
                    bubbles[idx2].vel = (
                        bubbles[idx2].momentum() + bubbles[idx].momentum()
                    ) / bubbles[idx2].mass()

                    if bubbles[idx].vel.x * bubbles[idx2].vel.x < 0:
                        new_radius = math.sqrt(
                            abs(bubbles[idx].mass() - bubbles[idx2].mass())
                        )
                    else:
                        new_radius = math.sqrt(
                            bubbles[idx].mass() + bubbles[idx2].mass()
                        )
                    bubbles[idx2].radius = new_radius
                    bubbles[idx].radius = 0
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


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running: bool = True

# Load background image
background = pygame.image.load("assets/images/battle_arena.png")
background = pygame.transform.scale(background, (1280, 720))

padding: int = 20
cannon_height: int = 40
cannon_width: int = 40
dt: float = 0

# Load sprites
sprites: Sprites = Sprites()


bubble_sounds: List[pygame.mixer.Sound] = [
    pygame.mixer.Sound("assets/sounds/p2.wav"),
    pygame.mixer.Sound("assets/sounds/p2.wav"),
]

collision_sound = pygame.mixer.Sound("assets/sounds/collision.wav")

gamestate = Gamestate()

player1 = Player(
    gamestate,
    40,
    screen.get_height(),
    bubble_sounds,
    "assets/images/water_gun.png",
    pygame.mixer.Sound("assets/sounds/sound.mp3"),
    sprites.bubble,
    True,
)
player2 = Player(
    gamestate,
    screen.get_width() - 100,
    screen.get_height(),
    bubble_sounds,
    "assets/images/water_gun_reflected.png",
    pygame.mixer.Sound("assets/sounds/sound.mp3"),
    sprites.bubble,
    False,
)

pygame.key.set_repeat()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background instead of filling with gray
    screen.blit(background, (0, 0))

    keys = pygame.key.get_pressed()

    # Update entities
    player1.tick(dt)
    player2.tick(dt)
    for b in gamestate.bubbles:
        b.tick(dt)

    # Draw entities
    player1.draw(screen)
    player2.draw(screen)
    for b in gamestate.bubbles:
        b.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()
    render_collisions(gamestate.bubbles, screen)
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
