import pygame

pygame.init()

class CharacterAnimation:
    def __init__(self, steps,color,animation_folder):
        self.color = color
        self.animation_list = []
        self.animation_steps = steps
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 100
        self.frame = 0
        self.load_animation_images(animation_folder)

    def make_rect(self,pos):
        rect = self.animation_list[0].get_rect(midbottom=pos)
        
        return rect


    def load_animation_images(self, animation_folder):
        self.animation_list = []
        for x in range(self.animation_steps):
            image_path = f'assets/character_animation/{self.color}/{animation_folder}/{animation_folder}{x+1}.png'
            image = pygame.transform.scale2x(pygame.image.load(
                image_path)).convert_alpha()
            self.animation_list.append(image)

    def run_animation(self, screen,pos,flep=False):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.frame = (self.frame + 1) % self.animation_steps
            self.last_update = current_time
        if not flep:
            image = self.animation_list[self.frame]
        else:
            image = pygame.transform.flip(self.animation_list[self.frame],True,False)
        screen.blit(image, pos)


if __name__ == "__main__":
    # Create an instance of the AnimationGame class and run the game

    # Load and idel running animation
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Spritesheets')
    BG = (150, 50, 5)

    game1 = CharacterAnimation(8,"green",'attack')
    game2 = CharacterAnimation(4,"blue",'damage')
    game3 = CharacterAnimation(12,"blue",'death')
    game4 = CharacterAnimation(6,"blue",'idle')
    game5 = CharacterAnimation(8,"blue",'jump_up')
    game6 = CharacterAnimation(8,"blue",'jump_down')
    game7 = CharacterAnimation(8,"blue",'run')
    game8 = CharacterAnimation(3,"blue",'shield')
    list_pos = [(0, 0), (150, 0), (300, 0), (450, 0), (600, 0), (750, 0), (900, 0), (1050, 0)]
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill(BG)
        game1.run_animation(screen, list_pos[0])
        game2.run_animation(screen, list_pos[1])
        game3.run_animation(screen, list_pos[2])
        game4.run_animation(screen, list_pos[3],True)
        game5.run_animation(screen, list_pos[4])
        game6.run_animation(screen, list_pos[5])
        game7.run_animation(screen, list_pos[6],True)
        game8.run_animation(screen, list_pos[7],True)
        pygame.display.update()
    pygame.quit()
