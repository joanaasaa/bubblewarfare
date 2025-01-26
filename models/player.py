import math
from typing import List, Type
import pygame
import models.bubble as bubble
import consts
from models.weapons import Weapon, BubbleGun, DuckGun, FutureGun, BoatGun


class Player:
    def __init__(
            self, gamestate, dir: consts.Direction, x, is_player_one=True, start_angle=0
    ):
        self.gamestate = gamestate
        self.player_bubble: bubble.Bubble | None = None
        self.dir = dir
        self.y: int = consts.SCREEN_HEIGHT // 2 - consts.CANNON_HEIGHT // 2
        self.x: int = x
        self.is_player_one = is_player_one
        self.is_moving = False
        self.score = 0

        self.angle = 0
        self.rotation_direction = 1
        # Weapon
        self.weapons: List[Weapon] = [BubbleGun(), DuckGun(), FutureGun(), BoatGun()]
        self.selected_weapon: int = 0
        self.angle = start_angle
        self.rotation_direction = 1

        # Bubble
        self.bubbles: List[Type[bubble.Bubble]] = [
            bubble.WaterBubble,
            bubble.GrassBubble,
            bubble.FireBubble,
        ]
        self.selected_bubble: int = 0
        self.select_bubble_toggle = False

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
        keys = pygame.key.get_pressed()
        up_key = pygame.K_e if self.is_player_one else pygame.K_l
        down_key = pygame.K_r if self.is_player_one else pygame.K_o

        if keys[up_key]:
            self.rotation_direction = 1
            self.angle = min(45,
                             self.angle
                             + 1 * self.rotation_direction * self.active_weapon().rotational_speed() * dt)
        if keys[down_key]:
            self.rotation_direction = -1
            self.angle = max(-45,
                             self.angle
                             + 1 * self.rotation_direction * self.active_weapon().rotational_speed() * dt)

    def shoot(self):
        keys = pygame.key.get_pressed()
        shoot_key = pygame.K_d if self.is_player_one else pygame.K_LEFT
        change_bubble_key = pygame.K_q if self.is_player_one else pygame.K_l
        bubble_spawn_pos = (
            consts.PADDING + consts.CANNON_WIDTH
            if self.is_player_one
            else consts.SCREEN_WIDTH - consts.PADDING - consts.CANNON_WIDTH
        )

        if keys[shoot_key]:
            if self.player_bubble is None:
                self.player_bubble = self.bubbles[self.selected_bubble](
                    bubble_spawn_pos, self.y + consts.CANNON_HEIGHT / 2, 0, 0
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


        if keys[change_bubble_key]:
            if self.select_bubble_toggle:
                return
            self.select_bubble_toggle = True
            self.selected_bubble = (self.selected_bubble + 1) % len(self.bubbles)
        else:
            self.select_bubble_toggle = False

    def update(self, dt):
        self.move(dt)
        self.rotate(dt)

    def active_weapon(self) -> Weapon:
        return self.weapons[self.selected_weapon]

    def draw(self, screen):
        self.shoot()
        self.active_weapon().draw(screen, self.x, self.y, self.dir, self.angle)

        if self.player_bubble is not None:
            self.player_bubble.draw(screen)

    def change_weapon(self, change_direction: consts.Direction):
        self.selected_weapon = (self.selected_weapon + change_direction.value) % len(self.weapons)


    def next_weapon(self):
        return self.weapons[(self.selected_weapon + consts.Direction.RIGHT.value) % len(self.weapons)]

    def prev_weapon(self):
        return self.weapons[(self.selected_weapon + consts.Direction.LEFT.value) % len(self.weapons)]   
