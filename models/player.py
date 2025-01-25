import math
from typing import List
import pygame
from models.bubble import Bubble
import consts
from weapons import Weapon, Gun, Gun2


class Player:
    def __init__(
        self,
        gamestate,
        dir: consts.Direction,
        x,
        is_player_one=True,
    ):
        self.gamestate = gamestate
        self.player_bubble: Bubble | None = None
        self.dir = dir
        self.y: int = consts.SCREEN_HEIGHT // 2 - consts.CANNON_HEIGHT // 2
        self.x: int = x
        self.is_player_one = is_player_one
        self.is_moving = False
        self.score = 0
        self.weapons: List[Weapon] = [Gun(), Gun2()]
        self.selected_weapon: int = 0
        self.select_weapon_toggle = False
        self.angle = 0
        self.rotation_direction = 1

    def move(self, dt):
        keys = pygame.key.get_pressed()
        up_key = pygame.K_w if self.is_player_one else pygame.K_UP
        down_key = pygame.K_s if self.is_player_one else pygame.K_DOWN

        was_moving = self.is_moving
        self.is_moving = keys[up_key] or keys[down_key]

        if self.is_moving and not was_moving:
            self.active_weapon().move()

        if keys[up_key]:
            self.y = max(0, self.y - self.active_weapon().vertical_speed() * dt)
        if keys[down_key]:
            self.y = min(
                consts.SCREEN_HEIGHT - 40,
                self.y + self.active_weapon().vertical_speed() * dt,
            )

    def rotate(self, dt: float):
        if self.angle > 45:
            self.rotation_direction = -1
        elif self.angle < -45:
            self.rotation_direction = 1

        self.angle = (
            self.angle
            + 1 * self.rotation_direction * self.active_weapon().rotational_speed() * dt
        )

    def shoot(self):
        keys = pygame.key.get_pressed()
        shoot_key = pygame.K_d if self.is_player_one else pygame.K_LEFT
        change_weapon_key = pygame.K_a if self.is_player_one else pygame.K_RIGHT
        bubble_spawn_pos = (
            consts.PADDING + consts.CANNON_WIDTH
            if self.is_player_one
            else consts.SCREEN_WIDTH - consts.PADDING - consts.CANNON_WIDTH
        )

        if keys[shoot_key]:
            if self.player_bubble is None:
                self.player_bubble = Bubble(
                    bubble_spawn_pos,
                    self.y + consts.CANNON_HEIGHT / 2,
                    0,
                    0,
                )
            else:
                self.player_bubble.increase_radius()
        else:
            if self.player_bubble is not None:
                self.player_bubble.vel.x = (
                    self.dir.value
                    * self.active_weapon().vertical_speed()
                    * math.cos(math.radians(self.angle))
                )
                self.player_bubble.vel.y = (
                    self.active_weapon().vertical_speed()
                    * math.sin(math.radians(self.angle))
                )
                self.gamestate.bubbles.append(self.player_bubble)
                self.active_weapon().shoot()
                self.player_bubble = None

        if keys[change_weapon_key]:
            if self.select_weapon_toggle:
                return
            self.select_weapon_toggle = True
            self.selected_weapon = (self.selected_weapon + 1) % len(self.weapons)
        else:
            self.select_weapon_toggle = False

    def update(self, dt):
        self.move(dt)
        self.rotate(dt)

    def active_weapon(self) -> Weapon:
        return self.weapons[self.selected_weapon]

    def draw(self, screen):
        self.shoot()
        self.active_weapon().draw(screen, self.x, self.y, self.dir)

        if self.player_bubble is not None:
            self.player_bubble.draw(screen)
