import pygame
from typing import List
from models.sprites import load_sprites
import consts


class Sounds:
    def __init__(self) -> None:
        self.move = pygame.mixer.Sound("assets/sounds/moving.wav")

        # bubble pops
        self.water_fire_pop = pygame.mixer.Sound("assets/sounds/waterfire.wav")
        self.fire_grass_pop = pygame.mixer.Sound("assets/sounds/firegrass.wav")
        self.water_grass_pop = pygame.mixer.Sound("assets/sounds/watergrass2.wav")
        self.ball_on_ball_pop = pygame.mixer.Sound("assets/sounds/ballonball.wav")

        # shoot sounds
        self.gun_shoot = pygame.mixer.Sound("assets/sounds/gunshooting.wav")
        self.gun_shoot.set_volume(0.1)  # Set volume to 30% of original

        # themes
        self.home_theme = pygame.mixer.Sound("assets/sounds/hometheme.wav")
        self.pause_theme = pygame.mixer.Sound("assets/sounds/pausetheme.wav")
        self.bubble_warfare_background = pygame.mixer.Sound("assets/sounds/hometheme.wav")

        #winners
        self.player_1_wins = pygame.mixer.Sound("assets/sounds/player1-wins.wav")
        self.player_2_wins = pygame.mixer.Sound("assets/sounds/player2wins.wav")

class Images:
    def __init__(self) -> None:
        # guns
        self.boat_gun = pygame.transform.scale(
            pygame.image.load("assets/images/weapons/boat.png"), (120, 125)
        )
        self.duck_gun = pygame.transform.scale(
            pygame.image.load("assets/images/weapons/duck.png"), (120, 125)
        )
        self.future_gun = pygame.transform.scale(
            pygame.image.load("assets/images/weapons/future.png"), (130, 135)
        )
        self.water_gun = pygame.transform.scale(
            pygame.image.load("assets/images/weapons/water_gun.png"), (120, 125)
        )
        
        # sprites
        self.water_bubble_sprites = load_sprites(
            "assets/images/water_bubble.png", 8, (100, 100)
        )
        self.grass_bubble_sprites = load_sprites(
            "assets/images/grass_bubble.png", 8, (100, 100)
        )
        self.fire_bubble_sprites = load_sprites(
            "assets/images/fire_bubble.png", 8, (100, 100)
        )

        # backgrounds
        self.arena_background = pygame.transform.scale(
            pygame.image.load("assets/images/grass_battle_arena.jpeg"),
            (consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT),
        )
        self.bubble_warfare_background = pygame.transform.scale(
            pygame.image.load("assets/images/bubble_warfare.png"),
            (consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT),
        )
        self.pause_background = pygame.transform.scale(
            pygame.image.load("assets/images/pause.png"),
            (consts.SCREEN_WIDTH / 2, consts.SCREEN_HEIGHT / 2),
        )
        self.game_selection_background = pygame.transform.scale(
            pygame.image.load("assets/images/gameselection_space_2.jpeg"), (consts.SCREEN_WIDTH/2, consts.SCREEN_HEIGHT/2)
        )


        # random
        self.left_arrow = pygame.transform.scale(
            pygame.image.load("assets/images/selectionarrow_left.png"), (consts.SCREEN_WIDTH/2, consts.SCREEN_HEIGHT/2)
        )
        self.right_arrow = pygame.transform.scale(
            pygame.image.load("assets/images/selectionarrow_right.png"), (consts.SCREEN_WIDTH/2, consts.SCREEN_HEIGHT/2)
        )


class Assets:
    def __init__(self) -> None:
        pygame.init()
        self.sounds = Sounds()
        self.images = Images()


assets = Assets()
