import pygame


# x
# 0
# +
# v
# 0
# x
# t
# +
# 1
# 2
# a
# x
# t
# 2
# v² = u² + 2as.
# s = ut

class Bubble:
    def __init__(self, init_x, init_y, vel_x, vel_y):
        self.player_pos = pygame.Vector2(init_x, init_y)
        self.player_vel = pygame.Vector2(vel_x, vel_y)
        self.radius = 1
        self.visible = False
        self.draw()

    def draw(self):
        if self.visible:
            pygame.draw.circle(screen, "orange", self.player_pos, self.radius)

    def tick(self):
        self.player_pos += self.player_vel * dt
        self.draw()

    def increase_radius(self):
        self.radius += 10/self.radius

    def set_visible(self):
        self.visible = True

    def set_x_vel(self, new_x_vel):
        self.player_vel.x = new_x_vel

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

padding = 20
player_speed = 300
cannon_height = 40
cannon_width = 40
dt = 0

# Player 1
player_1_y = screen.get_height() / 2 - cannon_height / 2
player_1_color = (255, 0, 0)

# Player 2
player_2_y = screen.get_height() / 2 - cannon_height / 2
player_2_color = (0, 255, 0)

b = Bubble(screen.get_width() / 2, screen.get_height() / 2, 100, 0)
pygame.key.set_repeat()

bubbles = [b]
player_1_bubble = None
player_2_bubble = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    pygame.draw.rect(screen, player_1_color, [padding, 10 + player_1_y, 40, cannon_height])
    pygame.draw.rect(screen, player_2_color, [screen.get_width() - padding - cannon_width, 10 + player_2_y, 40, cannon_height])

    keys = pygame.key.get_pressed()

    if player_1_bubble is None:
        if keys[pygame.K_w]:
            player_1_y = max(0, player_1_y - player_speed * dt)
        if keys[pygame.K_s]:
            player_1_y = min(screen.get_height() - cannon_height - padding, player_1_y + player_speed * dt)

    if player_2_bubble is None:
        if keys[pygame.K_UP]:
            player_2_y = max(0, player_2_y - player_speed * dt)
        if keys[pygame.K_DOWN]:
            player_2_y = min(screen.get_height() - cannon_height - padding, player_2_y + player_speed * dt)

    if keys[pygame.K_d]:
        if player_1_bubble is None:
            player_1_bubble = Bubble(padding, player_1_y, 0, 0)
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
            player_2_bubble = Bubble(screen.get_width() - padding, player_2_y, 0, 0)
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

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
