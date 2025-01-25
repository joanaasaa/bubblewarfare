import math
import pygame
from typing import List


class Bubble:
    def __init__(self, init_x, init_y, vel_x, vel_y):
        self.pos = pygame.Vector2(init_x, init_y)
        self.vel = pygame.Vector2(vel_x, vel_y)
        self.radius: float = 1
        self.visible = False
        self.draw()

    def draw(self):
        if self.visible:
            pygame.draw.circle(screen, "cyan", self.pos, self.radius)

    def tick(self):
        self.pos += self.vel * dt
        self.draw()

    def increase_radius(self):
        self.radius += 10 / self.radius

    def set_visible(self):
        self.visible = True

    def set_x_vel(self, new_x_vel):
        self.vel.x = new_x_vel

    def momentum(self):
        return self.vel * self.mass()

    def mass(self):
        return self.radius ** 2 


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
            print("OUT OF BOUNDS CARALHO")
            bubbles.remove(bubbles[idx])
            continue
        while idx2 < len(bubbles):
            if is_colliding(bubbles[idx], bubbles[idx2]):
                print("COLLIDING CARALHO")

                if bubbles[idx].momentum().magnitude() > bubbles[idx2].momentum().magnitude():
                    print(bubbles[idx].momentum())
                    print(bubbles[idx2].momentum())
                    bubbles[idx].vel = (bubbles[idx].momentum() + bubbles[idx2].momentum()) / bubbles[idx].mass()
                    print(bubbles[idx].vel)
                    if bubbles[idx].vel.x * bubbles[idx2].vel.x < 0:
                        new_radius = math.sqrt(abs(bubbles[idx].mass() - bubbles[idx2].mass()))
                    else:
                        new_radius = math.sqrt(bubbles[idx].mass() + bubbles[idx2].mass())
                    bubbles[idx].radius = new_radius
                    bubbles[idx2].radius = 0
                elif bubbles[idx].momentum().magnitude() < bubbles[idx2].momentum().magnitude():
                    print(bubbles[idx].momentum())
                    print(bubbles[idx2].momentum())
                    bubbles[idx2].vel = (bubbles[idx2].momentum() + bubbles[idx].momentum()) / bubbles[
                        idx2].mass()

                    if bubbles[idx].vel.x * bubbles[idx2].vel.x < 0:
                        new_radius = math.sqrt(abs(bubbles[idx].mass() - bubbles[idx2].mass()))
                    else:
                        new_radius = math.sqrt(bubbles[idx].mass() + bubbles[idx2].mass())
                    bubbles[idx2].radius = new_radius
                    bubbles[idx].radius = 0
                    print(bubbles[idx2].vel)
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




class Player:
    def __init__(self, x, screen_height, 
                    game_bubbles_state: List[Bubble],
                    player_bubble: Bubble | None,
                    bubble_sounds: List[pygame.mixer.Sound],
                    image_path, move_sound,
                    is_player_one=True):
        
        self.bubble_sounds = bubble_sounds
        self.game_bubbles_state = game_bubbles_state
        self.player_bubble = player_bubble
        self.y = screen_height / 2 - 40 / 2  # 40 is cannon_height
        self.x = x
        self.speed = 300
        self.image = pygame.transform.scale(
            pygame.image.load(image_path),
            (80, 85)
        )
        self.move_sound = move_sound
        self.is_player_one = is_player_one
        self.move_sound.set_volume(0.15)  # Adjust volume (0.0 to 1.0)
        self.is_moving = False
    
    def move(self, dt, screen_height):
        keys = pygame.key.get_pressed()
        up_key = pygame.K_w if self.is_player_one else pygame.K_UP
        down_key = pygame.K_s if self.is_player_one else pygame.K_DOWN
        
        was_moving = self.is_moving
        self.is_moving = keys[up_key] or keys[down_key]
        
        if self.is_moving and not was_moving:
            self.move_sound.play(-1)
        elif not self.is_moving and was_moving:
            self.move_sound.stop()
            
        if keys[up_key]:
            self.y = max(0, self.y - self.speed * dt)
        if keys[down_key]:
            self.y = min(screen_height - 40, self.y + self.speed * dt)


    def get_y(self):
        return self.y

    def shoot(self):
        shoot_key = pygame.K_d if self.is_player_one else pygame.K_LEFT
        bubble_spawn_pos = padding + cannon_width if self.is_player_one else screen.get_width() - padding - cannon_width
        bubble_speed = 100 if self.is_player_one else -100

        if keys[shoot_key]:
            if self.player_bubble is None:
                self.player_bubble = Bubble(
                    bubble_spawn_pos, self.get_y() + cannon_height / 2, 0, 0
                )
            else:
                self.player_bubble.set_visible()
                self.player_bubble.increase_radius()
                self.player_bubble.draw()
        else:
            if self.player_bubble is not None:
                self.player_bubble.set_x_vel(bubble_speed)
                game_bubbles_state.append(self.player_bubble)
                sound = self.bubble_sounds[0]
                sound.set_volume(0.4)  
                sound.play(0)
                self.player_bubble = None

    
    def draw(self, dt,screen):
        self.move(dt,screen.get_height())
        self.shoot()
        screen.blit(self.image, (self.x, self.y))

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running: bool = True

# Load background image
background = pygame.image.load('assets/images/battle_arena.png')
background = pygame.transform.scale(background, (1280, 720))

padding: int = 20
player_speed: int = 300
cannon_height: int = 40
cannon_width: int = 40
dt: float = 0



bubble_sounds: List[pygame.mixer.Sound] = [
                 pygame.mixer.Sound('assets/sounds/p2.wav'),
                 pygame.mixer.Sound('assets/sounds/p2.wav'),
]

collision_sound = pygame.mixer.Sound('assets/sounds/collision.wav')

game_bubbles_state: List[Bubble] = []
player_1_bubble: Bubble | None = None
player_2_bubble: Bubble | None = None

player1 = Player(40, screen.get_height(), game_bubbles_state, player_1_bubble, bubble_sounds, 
                 "assets/images/water_gun.png",
                 pygame.mixer.Sound('assets/sounds/sound.mp3'),
                 True)
player2 = Player(screen.get_width() - 100, screen.get_height(), game_bubbles_state, player_2_bubble, bubble_sounds,
                 "assets/images/water_gun_reflected.png",
                 pygame.mixer.Sound('assets/sounds/sound.mp3'),
                 False)

pygame.key.set_repeat()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background instead of filling with gray
    screen.blit(background, (0, 0))

    keys = pygame.key.get_pressed()


    player1.draw(dt,screen)
    player2.draw(dt,screen)

    for b in game_bubbles_state:
        b.tick()
    # flip() the display to put your work on screen
    pygame.display.flip()
    render_collisions(game_bubbles_state, screen)
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
