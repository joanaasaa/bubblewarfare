from typing import List
import pygame
from bubble import Bubble
import consts
from weapons import Weapon, Gun, Gun2


class Player:
    def __init__(
        self,
        gamestate,
        dir: consts.Direction,
        x,
        bubble_sounds: List[pygame.mixer.Sound],
        move_sound,
        sprites: List[pygame.Surface],
        is_player_one=True,
        pop_sound = None
    ):
        self.gamestate = gamestate
        self.bubble_sounds = bubble_sounds
        self.player_bubble: Bubble | None = None
        self.dir = dir
        self.y: int = consts.SCREEN_HEIGHT // 2 - consts.CANNON_HEIGHT // 2
        self.x: int = x
        self.move_sound = move_sound
        self.is_player_one = is_player_one
        self.move_sound.set_volume(0.15)  # Adjust volume (0.0 to 1.0)
        self.sprites: List[pygame.Surface] = sprites
        self.is_moving = False
        self.score = 0
        self.pop_sound = pop_sound
        self.weapons: List[Weapon] = [Gun(), Gun2()]
        self.selected_weapon: int = 0
        self.select_weapon_toggle = False

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
            self.y = max(0, self.y - self.active_weapon().vertical_speed() * dt)
        if keys[down_key]:
            self.y = min(
                screen_height - 40, self.y + self.active_weapon().vertical_speed() * dt
            )

    def shoot(self):
        print(self.selected_weapon)
        keys = pygame.key.get_pressed()
        shoot_key = pygame.K_d if self.is_player_one else pygame.K_LEFT
        change_weapon_key = pygame.K_a if self.is_player_one else pygame.K_RIGHT
        bubble_spawn_pos = (
            consts.PADDING + consts.CANNON_WIDTH
            if self.is_player_one
            else consts.SCREEN_WIDTH - consts.PADDING - consts.CANNON_WIDTH
        )
        bubble_speed = 100 if self.is_player_one else -100

        if keys[shoot_key]:
            if self.player_bubble is None:
                self.player_bubble = Bubble(
                    bubble_spawn_pos,
                    self.y + consts.CANNON_HEIGHT / 2,
                    0,
                    0,
                    self.sprites,
                    self.pop_sound,
                )
            else:
                self.player_bubble.set_visible()
                self.player_bubble.increase_radius()
        else:
            if self.player_bubble is not None:
                self.player_bubble.vel.x = bubble_speed
                self.gamestate.bubbles.append(self.player_bubble)
                sound = self.bubble_sounds[0]
                sound.set_volume(0.4)
                sound.play(0)
                self.player_bubble = None

        if keys[change_weapon_key]:
            if self.select_weapon_toggle:
                return
            self.select_weapon_toggle = True
            self.selected_weapon = (self.selected_weapon + 1) % len(self.weapons)
        else:
            self.select_weapon_toggle = False

    def tick(self, dt):
        self.move(dt, consts.SCREEN_HEIGHT)

    def active_weapon(self) -> Weapon:
        return self.weapons[self.selected_weapon]

    def draw(self, screen):
        self.shoot()
        self.active_weapon().draw(screen, self.x, self.y, self.dir)

        if self.player_bubble is not None:
            self.player_bubble.draw(screen)
