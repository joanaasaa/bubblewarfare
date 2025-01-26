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
        self.current_selection = 0
        self.box_size = 75
        self.box_spacing = 10
        self.boxes_rects = []  # Store the rectangles for collision detection
        self.button = None
        self.text_surface_rect = None
        self.text_surface = None
        self.init_start_game_button()    
        self.p1 = p1
        self.p2 = p2
        
        self.button_clicked = False
        

    
    
    def overlay_theme(self):
        # Calculate desired dimensions (2/3 of screen)
        desired_width = int(self.width * 9/14)
        desired_height = int(self.height * 9/14)
        
        # Scale background to desired size
        scaled_bg = pygame.transform.scale(self.background, (desired_width, desired_height))
        
        # Calculate center position
        x = (self.width - desired_width) // 2
        y = (self.height - desired_height) // 2
        self.py_screen.blit(scaled_bg, (x, y))

    def draw_weapon_selection(self, x, y, player: Player):
        self.boxes_rects = []  # Clear previous rectangles
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()[0]
        
        start_x = x
        if not mouse_clicked:
            self.button_clicked = False
            
            
        # Draw the three boxes
        for i in range(3):
            box_x = start_x + (i * (self.box_size + self.box_spacing))
            box_rect = pygame.Rect(box_x, y, self.box_size, self.box_size)
            self.boxes_rects.append(box_rect)
            
            # Draw arrows in boxes
            if i == 0:  # Left box
                if box_rect.collidepoint(mouse_pos):
                    pygame.draw.rect(self.py_screen, (255, 255, 0), box_rect, 3)
                if box_rect.collidepoint(mouse_pos) and mouse_clicked and not self.button_clicked:
                    self.button_clicked = True
                    player.change_weapon(consts.Direction.LEFT)
                    print("clicked left")
                arrow = pygame.transform.scale(player.prev_weapon().image, (self.box_size*3/5  , self.box_size*3/5))
                arrow_x = box_x+self.box_size/4   # 10px padding
                arrow_y = y+self.box_size/4
                self.py_screen.blit(arrow, (arrow_x, arrow_y))
            elif i == 1:  # weapon selection
                arrow = pygame.transform.scale(player.active_weapon().image, (self.box_size*1.3, self.box_size*1.3))
                arrow_x = box_x 
                arrow_y = y 
                self.py_screen.blit(arrow, (arrow_x, arrow_y))
            elif i == 2:  # Right box
                if box_rect.collidepoint(mouse_pos):
                    pygame.draw.rect(self.py_screen, (255, 255, 0), box_rect, 3) 
                if box_rect.collidepoint(mouse_pos) and mouse_clicked and not self.button_clicked:
                    self.button_clicked = True
                    player.change_weapon(consts.Direction.RIGHT)
                    print("clicked right")
                arrow = pygame.transform.scale(player.next_weapon().image, (self.box_size*3/5, self.box_size*3/5))
                arrow_x = box_x+self.box_size/10 + 10  # 10px padding
                arrow_y = y+self.box_size/4
                self.py_screen.blit(arrow, (arrow_x, arrow_y))
    
    def init_start_game_button(self):

        # Create and draw button
        color = (50, 200, 50)
        width = 200
        height = 50
        x = (self.width - width) // 2
        y = self.height // 2 + 150
        text = "Start Game"
        # Create button rectangle
        # Add button text

        self.button = pygame.Rect(x, y, width, height)

        font = pygame.font.Font(None, 36)
        self.text_surface = font.render(text, True, (255, 255, 255))
        self.text_surface_rect = self.text_surface.get_rect(center=self.button.center)
        
        
    def start_game_button(self) -> bool:

        # Check for mouse click on button
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()[0]

        return self.text_surface_rect.collidepoint(mouse_pos) and mouse_clicked
    
    def draw_start_game_button(self):

        pygame.draw.rect(self.py_screen, (50, 200, 50), self.button)
        self.py_screen.blit(self.text_surface, self.text_surface_rect )
    
    def draw(self, dt) -> None:
        self.overlay_theme()
        self.draw_weapon_selection(self.width/5+30,self.height/3, self.p1)
        self.draw_weapon_selection(self.width*3/5-30,self.height/3, self.p2)
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
                    for i, box_rect in enumerate(self.boxes_rects):
                        if box_rect.collidepoint(mouse_pos):
                            self.current_selection = i
                            return consts.GAME_SCREEN
        
        return consts.GAME_SELECTION_SCREEN

