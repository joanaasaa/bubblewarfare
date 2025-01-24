import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
cannon_height = 40
dt = 0

player_1_y = screen.get_height() / 2 - cannon_height / 2
player_2_y = screen.get_height() / 2 - cannon_height / 2

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    pygame.draw.rect(screen, (0, 0, 0), [30, 10 + player_1_y, 40, cannon_height])
    pygame.draw.rect(screen, (0, 0, 0), [screen.get_width() - 50, 10 + player_2_y, 40, cannon_height])

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_1_y = max(0, player_1_y - 300 * dt)
    if keys[pygame.K_s]:
        player_1_y = min(screen.get_height() - cannon_height, player_1_y + 300 * dt)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_2_y = max(0, player_2_y - 300 * dt)
    if keys[pygame.K_DOWN]:
        player_2_y = min(screen.get_height() - cannon_height, player_2_y + 300 * dt)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
