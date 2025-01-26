import pygame
import consts
from warfare import Warfare

# pygame setup
pygame.init()
py_screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
pygame.display.set_caption("Bubble Warfare")

clock = pygame.time.Clock()
running: bool = True

dt: float = 0

game = Warfare(py_screen, consts.HOME_SCREEN, consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    game.update()
    game.draw(dt)

    # flip() the display to put your work on screen
    pygame.display.flip()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
