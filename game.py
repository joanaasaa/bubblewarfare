import pygame
from gamestate import Gamestate
from collisions import render_collisions

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running: bool = True

# Load background image
background = pygame.image.load("assets/images/battle_arena.png")
background = pygame.transform.scale(background, (1280, 720))

gamestate = Gamestate()
collision_sound = pygame.mixer.Sound("assets/sounds/collision.wav")

dt: float = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background instead of filling with gray
    screen.blit(background, (0, 0))

    keys = pygame.key.get_pressed()

    # Update entities
    gamestate.player1.tick(dt)
    gamestate.player2.tick(dt)
    for b in gamestate.bubbles:
        b.tick(dt)

    if render_collisions(gamestate.bubbles, screen):
        collision_sound.play()

    # Draw entities
    gamestate.player1.draw(screen)
    gamestate.player2.draw(screen)
    for b in gamestate.bubbles:
        b.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
