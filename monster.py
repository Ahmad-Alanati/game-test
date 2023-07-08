import pygame
from player import Player
from level_maker import LevelMaker

class Monsters:
    def __init__(self,image,rect,distance,speed,animation_steps,name = None):
        self.image = [pygame.image.load(f"{image}{number}.png").convert_alpha() for number in range(1,animation_steps)]
        self.rect = self.image[0].get_rect(midbottom=rect.midtop)
        self.start_rect = rect

        self.default_position = rect.midtop

        self.animation_steps = animation_steps
        self.animation_index = 0
        self.distance = distance
        self.state = False
        self.speed = speed
        self.name = name

        # self.death = False
        # self.death_count = 0

        self.death_sound  = pygame.mixer.Sound("assets\\audio\mixkit-exclamation-of-pain-from-a-zombie-2207.wav")
        self.death_sound.set_volume(0.2)

        # self.last_update = pygame.time.get_ticks()
        # self.animation_cooldown = 100
        # self.frame = 0

    def reset_posision(self):
        self.rect = self.image[0].get_rect(midbottom=self.default_position)
        


    def movement(self):

        # key = pygame.key.get_pressed()
        # if key[pygame.K_LEFT]  and player.get_rect().x > 0:
        #     self.rect.x += 5
        # if key[pygame.K_RIGHT]  and player.get_rect().x < 3000:
        #     self.rect.x -= 5

        self.rect.x += self.speed
        if self.rect.x <= self.start_rect.x or self.rect.x >= self.start_rect.x + self.distance:
            self.speed *= -1  # Reverse the direction
            self.state = not(self.state)

        # if self.state :
        #     self.image = pygame.transform.flip(self.image[self.animation_steps], True,False)


    def animation(self):
        self.animation_index += 0.1
        if self.animation_index > self.animation_steps - 1 :
            self.animation_index = 0
                
        if self.name == "eater":
            current_time = pygame.time.get_ticks()
            key = pygame.key.get_pressed()
            if key[pygame.K_RSHIFT] and self.rect.colliderect(player.get_rect) and  current_time - player.last_update >= 1500:
                self.image = [pygame.image.load(f"assets\Parallax\eater_damage_{number}.png").convert_alpha() for number in range(1,8)]
                self.animation_steps = 8
                self.death = True      

                # pygame.time.wait(100)
                # self.kill()
            if self.death == True:
                self.death_count += 1
                if self.death_count == 50:
                    self.kill()

    def draw(self ,screen):
        self.movement()
        
        self.animation()
        
        if self.state :
            screen.blit(pygame.transform.flip(self.image[int(self.animation_index)],True,False),self.rect)
        else :
            screen.blit(self.image[int(self.animation_index)],self.rect)




class Eater(Monsters):
    def __init__(self, image, position, distance, speed, animation_steps):
        super().__init__(image, position, distance, speed, animation_steps)






def ground_list(ground_type,screen_height):
    image1 = pygame.image.load(ground_type[0]).convert_alpha()
    ground_width = image1.get_width()
    ground_height = image1.get_height()-20
    del image1
    ground1_position = []
    for i in range(3):
        ground1_position.append((ground_width * i, screen_height+20))
    pos_list = [(1300, screen_height-150), (1820, screen_height-320),
                ((ground_width * 10)+20, screen_height-220)]
    for element in pos_list:
        ground1_position.append(element)
    for i in range(11, 13):
        ground1_position.append((ground_width * i, screen_height+20))
    pos_list = [((ground_width * 13)+70, screen_height-150),
                ((ground_width * 15)-50, screen_height-150)]
    for element in pos_list:
        ground1_position.append(element)
    for i in range(16, 20):
        ground1_position.append((ground_width * i, screen_height+20))
    ground1_position.append(((ground_width * 2)+50, screen_height-340))
    ground3_position = [((ground_width * 16)+100, screen_height-350),
                        ((ground_width * 17)+100, screen_height-350),
                        ((ground_width * 18)+100, screen_height-350)
                        ]
    ground4_position = [((ground_width * 18)+500, screen_height-300),
                        ((ground_width * 18)+800, screen_height-450),
                        ((ground_width * 18)+1100, screen_height-450)
                        ]
    return ground1_position,ground3_position,ground4_position,ground_height

def coin_list(rects):
    coins_position =[(rect.x,rect.y-20) for rect in rects]
    return coins_position

def key_list(rects):
    keys_position =[rect.midtop for rect in rects]
    return keys_position


if __name__ == "__main__":
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('player test')
    BG = (150, 50, 5)
    clock = pygame.time.Clock()
    FPS = 60

    background_type = "assets\\backgrounds\\game_background\\sky_"
    ground_type = [
        "assets\\grounds\\ground1.png",
        "assets\\grounds\\ground2.png",
        "assets\\grounds\\ground3.png",
        "assets\\grounds\\ground4.png"
    ]
    background_object_list = [
        "assets\\game_objects\\tree.png",
        "assets\\game_objects\\door_off.png",
        "assets\\game_objects\\door_on.png",
    ]
    coin_path = "assets\game_objects\coin\Gold_"
    key_path = "assets\game_objects\key\key"
    ground1_position,ground3_position,ground4_position,ground_height = ground_list(ground_type,screen_height)
    tree_position = (250,screen_height-ground_height)
    door_position = (max(ground1_position, key=lambda x: x[0])[0],screen_height - ground_height)

    #making the object
    level_one = LevelMaker(screen_width, screen_height, background_type)
    player = Player("blue", (50, 200),[pygame.K_a, pygame.K_d, pygame.K_SPACE, pygame.K_f])
    player2 = Player("red", (100, 200),[pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_RSHIFT])
    



    for position in ground1_position:
        level_one.add_ground(ground_type[0], position)
    level_one.add_ground(ground_type[1], (2730, screen_height+600))
    for position in ground3_position:
        level_one.add_ground(ground_type[2], position)
    for position in ground4_position:
        level_one.add_ground(ground_type[3], position)

    level_one.add_level_object(background_object_list[0],tree_position)
    level_one.add_level_object(background_object_list[1],door_position)

    ground_rects = level_one.get_grounds_rect()
    coins_position = coin_list(ground_rects)
    keys_position = key_list(ground_rects)
    # print(keys_position)
    for position in coins_position:
        level_one.add_coin(coin_path,position)
    for position in keys_position:
        level_one.add_key(key_path,position)
    # level_one.add_coin(coin_path,(rects[1].x,rects[1].y-10))
    monster_1 = Monsters('assets\Parallax\eater_',level_one.get_grounds_rect()[1] ,400,3,13)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        
        # all the draws here
        level_one.draw(screen)
        monster_1.draw(screen)
        player.draw(screen)
        # player2.draw(screen)

        # all the update here and player2.get_player_position()> screen_width*0.5
        level_one.update_position(player.get_rect())
        # print(ground_rects)
        level_one.collect_coin(player.get_rect())
        level_one.collect_key(player.get_rect())
        player.movment(ground_rects)
        # player2.movment(ground_rects)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()