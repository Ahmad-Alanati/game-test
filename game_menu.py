import pygame
from button import Button

pygame.init()


class Menu:
    def __init__(self, screen_width, screen_height, font_size):
        self.font = pygame.font.Font("assets\\fonts\game_over.ttf", font_size)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.buttons = []

    def add_button(self, button_text, position, button_type):
        self.buttons.append(Button(button_text, position, button_type))


# start menu class
class StartGameMenu(Menu):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height, 128)
        self.background_frame = 0
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 100
        background_path = "assets\\backgrounds\\start_game_background\\start_game_background_"
        self.background_image = [pygame.image.load(
            f'{background_path}{image_number}.png').convert_alpha() for image_number in range(1, 12)]
        self.background_rect = self.background_image[0].get_rect(
            topleft=(0, 0))
        button_path = "assets\\menu_assets\\button_"
        self.add_button("Play", (screen_width*0.5,
                        screen_height * 0.45), button_path)
        self.add_button("Quit", (screen_width * 0.5,
                        screen_height * 0.7), button_path)

    def logo_info(self, position):
        logo = self.font.render("Pixel Rampage", False, "#F5F5F5")
        logo_rect = logo.get_rect(midtop=position)
        return logo, logo_rect

    def start_game_draw(self, screen):
        logo, logo_rect = self.logo_info(
            (self.screen_width*0.5, self.screen_height*0.15))
        screen.blit(
            self.background_image[self.background_frame % 11], self.background_rect)
        screen.blit(logo, logo_rect)
        for button in self.buttons:
            button.draw(screen)
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.background_frame = (self.background_frame + 1) % 11
            self.last_update = current_time


# Pause menu class
class PauseGameMenu(Menu):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height, 128)
        background_path = 'assets\menu_assets\pause_menu.png'
        self.background_image = pygame.image.load(
            background_path).convert_alpha()
        self.background_rect = self.background_image.get_rect(
            center=(screen_width*0.5, screen_height*0.48))
        button_path = "assets\\menu_assets\\button_"
        self.add_button("Resume", (screen_width*0.5,
                        screen_height*0.45), button_path)
        self.add_button("Main Menu", (screen_width * 0.5,
                        screen_height * 0.7), button_path)

    def menu_text(self, position):
        text = self.font.render("Pause Game", False, "#505050")
        text_rect = text.get_rect(midtop=position)
        return text, text_rect

    def pause_game_draw(self, screen):
        text, text_rect = self.menu_text(
            (self.screen_width*0.5, self.screen_height*0.15))
        width, height = self.background_image.get_size()
        self.background_image = pygame.transform.scale(
            self.background_image, (width, self.screen_height*0.6))
        screen.blit(self.background_image, self.background_rect)
        screen.blit(text, text_rect)
        for button in self.buttons:
            button.draw(screen)


# Game Over menu class
class GameOverMenu(Menu):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height, 256)
        self.background_frame = 0
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 100
        background_path = "assets\\backgrounds\\game_over_background\\game_over_ground"
        self.background_image = [pygame.image.load(
            f'{background_path}{image_number}.png').convert_alpha() for image_number in range(1, 28)]
        self.background_rect = self.background_image[0].get_rect(
            topleft=(0, 0))
        button_path = "assets\\menu_assets\\game_over_button_"
        self.add_button("Play Again", (screen_width*0.5,
                        screen_height * 0.35), button_path)
        self.add_button("Main Menu", (screen_width * 0.5,
                        screen_height * 0.6), button_path)

    def menu_text(self, position):
        text = self.font.render("Game Over", False, "#F5F5F5")
        text_rect = text.get_rect(center=position)
        return text, text_rect

    def game_over_draw(self, screen):
        text, text_rect = self.menu_text(
            (self.screen_width*0.5, self.screen_height*0.07))
        scaled_background = pygame.transform.scale(
            self.background_image[self.background_frame % 27], (self.screen_width, self.screen_height))
        screen.blit(scaled_background, self.background_rect)
        screen.blit(text, text_rect)
        self.buttons[0].draw(screen)
        self.buttons[1].draw(screen)
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.background_frame = (self.background_frame + 1) % 11
            self.last_update = current_time


        