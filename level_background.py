import pygame

pygame.init()


class LevelBackground:
    def __init__(self, screen_width, screen_height, background_image, position):
        self.screen_width = screen_width
        self.background_images = [pygame.image.load(
            f"{background_image}{image_number}.png").convert_alpha() for image_number in range(1, 4)]
        self.background_images = [pygame.transform.scale(
            image, (screen_width, screen_height)) for image in self.background_images]
        self.background_rects = self.background_images[0].get_rect(
            topleft=(screen_width*position, 0))
        self.defult_position = position

    def update_position(self, direction):
        if direction == True:
            self.background_rects.x -= 5
        elif direction == False:
            self.background_rects.x += 5

    def reset_position(self):
        self.background_rects = self.background_images[0].get_rect(
            topleft=(self.screen_width*self.defult_position, 0))

    def draw(self, screen):
        for image in self.background_images:
            screen.blit(image, self.background_rects)
