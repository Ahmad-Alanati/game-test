import pygame
from sound import Sound
from controller import Joystickclass

pygame.init()
pygame.mixer.set_num_channels(5)
controller = Joystickclass()


class Player:
    def __init__(self, color, position,control,name):
        animation_path = f"assets\\character_animation\\{color}"
        self.attack_animation = [pygame.transform.scale2x(pygame.image.load(
            f"{animation_path}\\attack\\attack{number}.png").convert_alpha()) for number in range(3)]
        self.running_animation = [pygame.transform.scale2x(pygame.image.load(
            f"{animation_path}\\run\\run{number}.png").convert_alpha()) for number in range(1,9)]
        self.idle_animation = [pygame.transform.scale2x(pygame.image.load(
            f"{animation_path}\\idle\\idle{number}.png").convert_alpha()) for number in range(1,7)]
        self.damage_animation = [pygame.transform.scale2x(pygame.image.load(
            f"{animation_path}\\damage\\damage{number}.png").convert_alpha()) for number in range(1,5)]
        self.jump_animation = [pygame.transform.scale2x(pygame.image.load(f"{animation_path}\\jump\\jump{number}.png").convert_alpha()) for number in range(1,4)]
        self.rect = self.attack_animation[0].get_rect(midbottom=position)
        self.default_position = position
        self.name = name

        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 100
        self.frame = 0

        self.x_velocity = 0
        self.y_velocity = 0
        self.on_ground = False

        self.control_buttons = control
        self.attack_state = False
        self.fleped = False
        self.current_move = self.idle_animation

        ## sounds
        self.attack_sound=Sound('assets\\audio\\sword-hit-7160.mp3')
        self.jump_sound=Sound('assets\\audio\\Jump.mp3')
        self.coin_sound=Sound('assets\\audio\\coins.mp3')
        self.key_sound=Sound('assets\\audio\\Key.wav')
        self.hurt_sound=Sound('assets\\audio\\hurt_c_08-102842.mp3')

        
    def move_right(self):
        self.x_velocity = 5
        if self.fleped:
            self.fleped = False
        if self.on_ground:
            self.current_move = self.running_animation

    def move_left(self):
        self.x_velocity = -5
        if not self.fleped:
            self.fleped = True
        if self.on_ground:
            self.current_move = self.running_animation
        

    def jump_up(self):
        self.y_velocity = -18
        self.on_ground = False
        self.current_move = self.jump_animation
        self.jump_sound.play_sound(0.5)

    def idle(self):
        self.current_move = self.idle_animation

    def attack(self):
        self.current_move = self.attack_animation
        self.x_velocity = 0
        self.y_velocity = 0
        if not self.attack_state:
            self.attack_sound.play_sound(0.5)

    def ground_collide(self,rects):
        rect = self.rect.collidelist(rects)
        if rect != -1:

            if self.y_velocity > 0 : 
                self.rect.bottom = rects[rect].top 
                self.y_velocity = 0 
                self.on_ground = True

            if self.y_velocity < 0 : 
                self.rect.top = rects[rect].bottom 
                self.y_velocity = 0
                self.on_ground = False  
        else:
            self.on_ground = False

    def get_player_position(self):
        return self.rect.x
    
    def get_rect(self):
        return self.rect
    
    def reset_position(self):
        self.rect = self.attack_animation[0].get_rect(midbottom=self.default_position)


    def movment(self,rects):
        if self.name=='player_one':
            self.x_velocity = 0
            keys=pygame.key.get_pressed()
            input_buttons = [keys[button] for  button in self.control_buttons]

            self.ground_collide(rects)

            if input_buttons[3] and self.on_ground or self.attack_state:
                if self.current_move != self.attack_animation:
                    self.frame = 0
                self.attack()
                if self.frame < len(self.attack_animation)-1:
                    self.attack_state = True
                else:
                    self.attack_state = False
                return

            if input_buttons[0]:
                if self.current_move != self.running_animation:
                    self.frame = 0
                self.move_left()
                
            elif input_buttons[1]:
                if self.current_move != self.running_animation:
                    self.frame = 0
                self.move_right()

            if input_buttons[2] and self.on_ground or (controller.joystick_check_if____Y__button() and self.on_ground):
                if self.current_move != self.jump_animation:
                    self.frame = 0
                self.jump_up()
            

            if self.x_velocity == 0 and self.on_ground:
                if self.current_move != self.idle_animation:
                    self.frame = 0
                self.idle()

            if not self.on_ground:
                self.y_velocity += 0.8

            if self.y_velocity > 20:
                self.y_velocity = 20
                
            self.rect.x += self.x_velocity
            self.rect.y += self.y_velocity

            if self.rect.left < 200:
                self.rect.left = 200

            if self.rect.right > 1000:
                self.rect.right = 1000

        if self.name=='player_two':
            self.x_velocity = 0
            keys=pygame.key.get_pressed()
            input_buttons = [keys[button] for  button in self.control_buttons]

            self.ground_collide(rects)

            if controller.joystick_check_if_atacking___B_button() and self.on_ground or self.attack_state:
                if self.current_move != self.attack_animation:
                    self.frame = 0
                self.attack()
                if self.frame < len(self.attack_animation)-1:
                    self.attack_state = True
                else:
                    self.attack_state = False
                return

            if controller.joystick_check_if_run_left():
                if self.current_move != self.running_animation:
                    self.frame = 0
                self.move_left()
                
            elif controller.joystick_check_if_run_right():
                if self.current_move != self.running_animation:
                    self.frame = 0
                self.move_right()

            if controller.joystick_check_if_jump____A_button() and self.on_ground :
                if self.current_move != self.jump_animation:
                    self.frame = 0
                self.jump_up()
            

            if self.x_velocity == 0 and self.on_ground:
                if self.current_move != self.idle_animation:
                    self.frame = 0
                self.idle()

            if not self.on_ground:
                self.y_velocity += 0.8

            if self.y_velocity > 20:
                self.y_velocity = 20
                
            self.rect.x += self.x_velocity
            self.rect.y += self.y_velocity

            if self.rect.left < 200:
                self.rect.left = 200

            if self.rect.right > 1000:
                self.rect.right = 1000 

    def draw(self, screen):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.frame = (self.frame + 1) % len(self.current_move)
            self.last_update = current_time
        image = self.current_move[self.frame]
        image = pygame.transform.flip(image, self.fleped, False)
        screen.blit(image, self.rect)
