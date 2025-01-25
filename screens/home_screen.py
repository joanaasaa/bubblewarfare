import pygame
import consts


class HomeScreen:
    def __init__(self, py_screen, width, height) -> None:
        self.width = width
        self.height = height
        self.background = pygame.transform.scale(
            pygame.image.load("assets/images/bubble_warfare.png"),
            (self.width, self.height),
        )
        self.py_screen = py_screen
        self.next_screen = consts.HOME_SCREEN

    def start_game_button(self, text, x, y, width, height, color) -> bool:
        # Create button rectangle
        button_rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(self.py_screen, color, button_rect)

        # Add button text
        font = pygame.font.Font(None, 36)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=button_rect.center)
        self.py_screen.blit(text_surface, text_rect)

        # Check for mouse click on button
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()[0]

        return button_rect.collidepoint(mouse_pos) and mouse_clicked

    def draw(self, dt) -> None:
        self.py_screen.blit(self.background, (0, 0))

        # Create and draw button
        button_width = 200
        button_height = 50
        button_x = (self.width - button_width) // 2
        button_y = self.height // 2

        if self.start_game_button(
            "Start Game", button_x, button_y, button_width, button_height, (50, 200, 50)
        ):
            self.next_screen = consts.GAME_SCREEN

    def update(self):
        return self.next_screen

