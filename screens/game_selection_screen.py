import pygame
import consts
from assets import assets
from models.player import Player


class GameSelectionScreen:
    def __init__(self, py_screen, width, height, p1: Player, p2: Player) -> None:
        self.width = width
        self.height = height
        self.background = assets.images.game_selection_background
        self.py_screen = py_screen
        self.theme = assets.sounds.bubble_warfare_background
        self.is_playing = False
        self.box_size = 110
        self.box_spacing = 10
        self.boxes_rects = []  # Store the rectangles for collision detection
        self.button = None
        self.text_surface_rect = None
        self.text_surface = None
        self.init_start_game_button()
        self.p1 = p1
        self.p2 = p2
        self.button_clicked = False

        self.button_clicked = False

    def overlay_theme(self):
        # Calculate desired dimensions (2/3 of screen)
        desired_width = int(self.width)
        desired_height = int(self.height)

        # Scale background to desired size
        scaled_bg = pygame.transform.scale(
            self.background, (desired_width, desired_height)
        )

        # Calculate center position
        x = (self.width - desired_width) // 2
        y = (self.height - desired_height) // 2
        self.py_screen.blit(scaled_bg, (x, y))

    def draw_weapon_selection(self, x, y, player: Player):
        self.boxes_rects = []  # Clear previous rectangles
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()[0]
        selector_size = self.box_size*4/7
        selected_size = self.box_size*1.6

        if not mouse_clicked:
            self.button_clicked = False

        # Draw the three boxes
        for i in range(3):
            box_rect = pygame.Rect(x, y, selector_size, selector_size)
            self.boxes_rects.append(box_rect)
                
            # Draw arrows in boxes
            if i == 0:  # Left box
                box_rect = pygame.Rect(x, y, selector_size, selector_size)
                self.boxes_rects.append(box_rect)
                
                if box_rect.collidepoint(mouse_pos):
                    pygame.draw.rect(self.py_screen, (255, 255, 0), box_rect, 3)
                if (
                    box_rect.collidepoint(mouse_pos)
                    and mouse_clicked
                    and not self.button_clicked
                ):
                    self.button_clicked = True
                    player.change_weapon(consts.Direction.LEFT)
                arrow = pygame.transform.scale(player.prev_weapon().image, (selector_size  , selector_size))
                self.py_screen.blit(arrow, (x, y))
                
            elif i == 1:  # weapon selection
                arrow = pygame.transform.scale(player.active_weapon().image, (selected_size, selected_size))
                self.py_screen.blit(arrow, (x+selector_size, y- (selector_size/2)))

                
            elif i == 2:  # right box
                box_rect = pygame.Rect(x+selector_size+selected_size, y, selector_size, selector_size)
                self.boxes_rects.append(box_rect)
                
                if box_rect.collidepoint(mouse_pos):
                    pygame.draw.rect(self.py_screen, (255, 255, 0), box_rect, 3)
                if (
                    box_rect.collidepoint(mouse_pos)
                    and mouse_clicked
                    and not self.button_clicked
                ):
                    self.button_clicked = True
                    player.change_weapon(consts.Direction.RIGHT)
                arrow = pygame.transform.scale(player.next_weapon().image, (selector_size, selector_size))
                
                self.py_screen.blit(arrow, (x+selector_size+selected_size, y))
             
    
    
    def draw_arena_selection(self, x, y):
        self.boxes_rects = []  # Clear previous rectangles
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()[0]
        selector_size = self.box_size*4/5
        arena_size = self.box_size*1.6
        
        if not mouse_clicked:
            self.button_clicked = False
            
        # Draw the three boxes
        for i in range(3):
            # Draw arrows in boxes
            if i == 0:
                box_rect = pygame.Rect(x, y, selector_size, selector_size)
                self.boxes_rects.append(box_rect)

                if box_rect.collidepoint(mouse_pos):
                    pygame.draw.rect(self.py_screen, (255, 255, 0), box_rect, 3)
                if (
                    box_rect.collidepoint(mouse_pos)
                    and mouse_clicked
                    and not self.button_clicked
                ):
                    self.button_clicked = True
                    consts.current_arena = (consts.current_arena - 1) % len(
                        assets.images.arenas
                    )
                arrow = pygame.transform.scale(
                    assets.images.left_arrow, (selector_size, selector_size)
                )
                self.py_screen.blit(arrow, (x, y))
            elif i == 1:  # arena selection
                arrow = pygame.transform.scale(
                    assets.images.arenas[consts.current_arena],
                    (arena_size, arena_size),
                )
                self.py_screen.blit(arrow, (x + selector_size, y - (selector_size / 2)))
            
            elif i == 2:
                box_rect = pygame.Rect(x+selector_size+arena_size, y, selector_size, selector_size)
                self.boxes_rects.append(box_rect)
                
                if box_rect.collidepoint(mouse_pos):
                    pygame.draw.rect(self.py_screen, (255, 255, 0), box_rect, 3)
                if (
                    box_rect.collidepoint(mouse_pos)
                    and mouse_clicked
                    and not self.button_clicked
                ):
                    self.button_clicked = True
                    consts.current_arena = (consts.current_arena + 1) % len(
                        assets.images.arenas
                    )
                arrow = pygame.transform.scale(assets.images.right_arrow, (selector_size, selector_size))
                self.py_screen.blit(arrow, (x+selector_size+arena_size, y))

            

    def init_start_game_button(self):
        # Create and draw button
        color = (50, 200, 50)
        width = 200
        height = 50
        x = (self.width - width) // 2 -35
        y = self.height // 2 + 200
        text = "Start Game"
        # Create button rectangle
        # Add button text

        self.button = pygame.Rect(x, y, width, height)

        font = pygame.font.Font("assets/fonts/PixelifySans-Regular.ttf", 30)
        self.text_surface = font.render(text, True, (255, 255, 255))
        self.text_surface_rect = self.text_surface.get_rect(center=self.button.center)

    def start_game_button(self) -> bool:
        # Check for mouse click on button
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()[0]

        return self.text_surface_rect.collidepoint(mouse_pos) and mouse_clicked

    def draw_start_game_button(self):
        pygame.draw.rect(self.py_screen, (50, 200, 50), self.button, border_radius=15)
        self.py_screen.blit(self.text_surface, self.text_surface_rect)

    def draw(self, dt) -> None:
        self.overlay_theme()
        self.draw_weapon_selection(self.width / 12 + 30, self.height / 5, self.p1)
        self.draw_weapon_selection(self.width * 3 / 5 - 30, self.height / 5, self.p2)
        self.draw_arena_selection(self.width / 3, self.height * 2 / 5 + 60)
        self.draw_start_game_button()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.start_game_button():
            self.theme.stop()
            return consts.GAME_SCREEN

        # Check for mouse clicks
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    # Check which box was clicked
                    for _, box_rect in enumerate(self.boxes_rects):
                        if box_rect.collidepoint(mouse_pos):
                            return consts.GAME_SCREEN

        return consts.GAME_SELECTION_SCREEN
