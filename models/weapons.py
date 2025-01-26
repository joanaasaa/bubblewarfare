from abc import ABC, abstractmethod
import pygame
from assets import assets

import consts


class Weapon(ABC):
    def __init__(self) -> None:
        self.image: pygame.Surface
        pass

    @abstractmethod
    def vertical_speed(self) -> int:
        pass

    @abstractmethod
    def rotational_speed(self) -> int:
        pass

    @abstractmethod
    def shoot(self) -> None:
        pass

    @abstractmethod
    def move(self) -> None:
        pass

    def draw(
        self,
        screen: pygame.Surface,
        x: int,
        y: int,
        dir: consts.Direction,
        angle: float,
    ):
        rotated = pygame.transform.rotate(self.image, -angle)
        new_rect = rotated.get_rect(center=self.image.get_rect(center=(x, y)).center)
        if dir == consts.Direction.LEFT:
            screen.blit(pygame.transform.flip(rotated, True, False), new_rect)
        else:
            screen.blit(rotated, new_rect)


class Gun(Weapon):
    def __init__(self) -> None:
        self.image: pygame.Surface = assets.images.water_gun_p1
        self.shoot_sound: pygame.mixer.Sound = assets.sounds.gun_shoot
        self.move_sound: pygame.mixer.Sound = assets.sounds.move

        self.v_speed: int = 300
        self.r_speed: int = 80

    def vertical_speed(self) -> int:
        return self.v_speed

    def rotational_speed(self) -> int:
        return self.r_speed

    def shoot(self) -> None:
        self.shoot_sound.set_volume(0.4)
        self.shoot_sound.play(0)

    def move(self) -> None:
        self.move_sound.set_volume(0.15)
        self.move_sound.play(0)


class Gun2(Weapon):
    def __init__(self) -> None:
        self.image: pygame.Surface = assets.images.water_gun_p2
        self.shoot_sound: pygame.mixer.Sound = assets.sounds.gun_shoot
        self.move_sound: pygame.mixer.Sound = assets.sounds.move

        self.v_speed = 600
        self.r_speed = 80

    def vertical_speed(self) -> int:
        return self.v_speed

    def rotational_speed(self) -> int:
        return self.r_speed

    def shoot(self) -> None:
        self.shoot_sound.set_volume(0.4)
        self.shoot_sound.play(0)

    def move(self) -> None:
        self.move_sound.set_volume(0.15)
        self.move_sound.play(0)
