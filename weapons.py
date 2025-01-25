from abc import ABC, abstractmethod
import pygame

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

    def draw(self, screen: pygame.Surface, x: int, y: int, dir: consts.Direction):
        if dir == consts.Direction.LEFT:
            screen.blit(pygame.transform.flip(self.image, True, False), (x, y))
        else:
            screen.blit(self.image, (x, y))


class Gun(Weapon):
    def __init__(self) -> None:
        self.image = pygame.transform.scale(
            pygame.image.load("assets/images/water_gun.png"), (80, 85)
        )

        self.v_speed = 300
        self.r_speed = 30

    def vertical_speed(self) -> int:
        return self.v_speed

    def rotational_speed(self) -> int:
        return self.r_speed


class Gun2(Weapon):
    def __init__(self) -> None:
        self.image = pygame.transform.scale(
            pygame.image.load("assets/images/water_gun.png"), (80, 85)
        )

        self.v_speed = 600
        self.r_speed = 20

    def vertical_speed(self) -> int:
        return self.v_speed

    def rotational_speed(self) -> int:
        return self.r_speed
