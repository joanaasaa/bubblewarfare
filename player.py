from typing import List
import pygame
from bubble import Bubble
from consts import SCREEN_HEIGHT, SCREEN_WIDTH, CANNON_WIDTH, CANNON_HEIGHT, PADDING


class Player:
    def __init__(
        self,
        gamestate,
        x,
        screen_height,
        bubble_sounds: List[pygame.mixer.Sound],
        image_path,
        move_sound,
        sprites: List[pygame.Surface],
        is_player_one=True,
    ):
        self.gamestate = gamestate
        self.bubble_sounds = bubble_sounds
        self.player_bubble: Bubble | None = None
        self.y = screen_height / 2 - 40 / 2  # 40 is cannon_height
        self.x = x
        self.speed = 300
        self.image = pygame.transform.scale(pygame.image.load(image_path), (80, 85))
        self.move_sound = move_sound
        self.is_player_one = is_player_one
        self.move_sound.set_volume(0.15)  # Adjust volume (0.0 to 1.0)
        self.sprites: List[pygame.Surface] = sprites
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
        keys = pygame.key.get_pressed()
        shoot_key = pygame.K_d if self.is_player_one else pygame.K_LEFT
        bubble_spawn_pos = (
            PADDING + CANNON_WIDTH
            if self.is_player_one
            else SCREEN_WIDTH - PADDING - CANNON_WIDTH
        )
        bubble_speed = 100 if self.is_player_one else -100

        if keys[shoot_key]:
            if self.player_bubble is None:
                self.player_bubble = Bubble(
                    bubble_spawn_pos,
                    self.get_y() + CANNON_HEIGHT / 2,
                    0,
                    0,
                    self.sprites,
                )
            else:
                self.player_bubble.set_visible()
                self.player_bubble.increase_radius()
        else:
            if self.player_bubble is not None:
                self.player_bubble.set_x_vel(bubble_speed)
                self.gamestate.bubbles.append(self.player_bubble)
                sound = self.bubble_sounds[0]
                sound.set_volume(0.4)
                sound.play(0)
                self.player_bubble = None

    def tick(self, dt):
        self.move(dt, SCREEN_HEIGHT)

    def draw(self, screen):
        self.shoot()
        if self.player_bubble is not None:
            self.player_bubble.draw(screen)
        screen.blit(self.image, (self.x, self.y))
