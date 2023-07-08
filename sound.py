import pygame

pygame.init()
pygame.mixer.init()

class Sound:
    def __init__(self,path):
        self.sound=pygame.mixer.Sound(path)
# play sounds of game
    def play_sound(self,volume):
            self.sound.set_volume(volume)
            self.sound.play()
# stop -play Sound
    def stop_sound(self):
        self.sound.stop()