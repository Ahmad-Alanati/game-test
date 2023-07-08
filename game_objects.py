import pygame

pygame.init()


class LevelObject:
    def __init__(self, image, rect,x_incrsse):
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect(midbottom=rect.midtop)
        self.default_position = rect.midtop

    def update_position(self, direction):
        if direction == True:
            self.rect.x -= 5
        elif direction == False:
            self.rect.x += 5

    def reset_position(self):
        self.rect = self.image.get_rect(midbottom=self.default_position)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Ground:
    def __init__(self, image, position):
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect(midbottom=position)
        self.default_position = position

    def update_position(self, direction):
        if direction == True:
            self.rect.x -= 5
        elif direction == False:
            self.rect.x += 5

    def reset_position(self):
        self.rect = self.image.get_rect(
            midbottom=self.default_position)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def get_rect(self):
        return self.rect


class Coin:
    def __init__(self, image, position):
        self.images = [pygame.image.load(
            f"{image}{image_number}.png").convert_alpha() for image_number in range(1, 11)]
        self.rect = self.images[0].get_rect(bottomleft=position)
        self.default_position = position
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 60
        self.frame = 0

    def get_rect(self):
        return self.rect

    def reset_position(self):
        self.rect = self.images[0].get_rect(bottomleft=self.default_position)

    def update_position(self, direction):
        if direction == True:
            self.rect.x -= 5
        elif direction == False:
            self.rect.x += 5

    def animation(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.frame = (self.frame + 1) % 10
            self.last_update = current_time

    def draw(self, screen):
        self.animation()
        screen.blit(self.images[self.frame], self.rect)


class Key:
    def __init__(self, image, position):
        self.images = [pygame.image.load(
            f"{image}{image_number}.png").convert_alpha() for image_number in range(1, 24)]
        self.rect = self.images[0].get_rect(bottomleft=position)
        self.default_position = position
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 60
        self.frame = 0

    def get_rect(self):
        return self.rect

    def reset_position(self):
        self.rect = self.images[0].get_rect(bottomleft=self.default_position)

    def update_position(self, direction):
        if direction == True:
            self.rect.x -= 5
        elif direction == False:
            self.rect.x += 5

    def animation(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.frame = (self.frame + 1) % 23
            self.last_update = current_time

    def draw(self, screen):
        self.animation()
        screen.blit(self.images[self.frame], self.rect)


