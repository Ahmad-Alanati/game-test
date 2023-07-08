import pygame
from sound import Sound

pygame.init()

class Button:
    def __init__(self, button_text, position, button_image):
        self.font = pygame.font.Font("assets\\fonts\game_over.ttf", 128)
        self.button_text = button_text
        button_stats = ["off.png", "on.png"]
        self.selected_button = 0
        self.buttons_images = [pygame.image.load(button_image+button_images_stats).convert_alpha() for button_images_stats in button_stats]
        self.text = self.font.render(button_text, True, "#F5F5F5")
        self.button_rect = self.buttons_images[0].get_rect(center=position)
        text1_pos = (position[0], position[1]-(position[1]*0.02))
        self.text_rect = self.text.get_rect(center=text1_pos)
        self.button_sound = Sound("assets\\audio\\button_click_sound.wav")

    def hover(self):
        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            self.selected_button = 1
            self.text = self.font.render(self.button_text, False, "#CD7F32")
        else:
            self.selected_button = 0
            self.text = self.font.render(self.button_text, False, "#F5F5F5")

    def button_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos) and event.button == 1:
                self.button_sound.play_sound(1)
                return True
            else:
                return False

    def draw(self, screen):
        screen.blit(self.buttons_images[self.selected_button], self.button_rect)
        screen.blit(self.text, self.text_rect)
