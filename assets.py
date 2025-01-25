import pygame
from typing import List
from models.sprites import load_sprites


class Assets:
    def __init__(self) -> None:
        pygame.init()
        self.water_gun: pygame.Surface = pygame.transform.scale(
            pygame.image.load("assets/images/water_gun.png"), (80, 85)
        )
        self.shoot_sound: pygame.mixer.Sound = pygame.mixer.Sound(
            "assets/sounds/p2.wav"
        )
        self.move_sound: pygame.mixer.Sound = pygame.mixer.Sound(
            "assets/sounds/move_sound.mp3"
        )
        self.water_bubble_sprites: List[pygame.Surface] = load_sprites(
            "assets/images/water_bubble.png", 8, (100, 100)
        )
        self.grass_bubble_sprites: List[pygame.Surface] = load_sprites(
            "assets/images/grass_bubble.png", 8, (100, 100)
        )
        self.fire_bubble_sprites: List[pygame.Surface] = load_sprites(
            "assets/images/fire_bubble.png", 8, (100, 100)
        )
        self.water_bubble_pop_sound: pygame.mixer.Sound = pygame.mixer.Sound(
            "assets/sounds/bubble_pop.wav"
        )


assets = Assets()
