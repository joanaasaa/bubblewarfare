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

dt: float = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background instead of filling with gray
    screen.blit(background, (0, 0))

    # General game info
    gamestate.render_match_data(screen)
    # Update entities
    gamestate.player1.update(dt)
    gamestate.player2.update(dt)
    for b in gamestate.bubbles:
        b.update(dt)

    score = render_collisions(gamestate.bubbles, screen)
    gamestate.calculate_scoring(score)
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
