import pygame
from game_menu import StartGameMenu, PauseGameMenu, GameOverMenu
from level_maker import LevelMaker
from player import Player
from sound import Sound
from monster import Monsters
from sys import exit

pygame.init()
pygame.mixer.set_num_channels(5)

def quit_game():
    pygame.quit()
    exit()

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
    return ground1_position,ground3_position,ground4_position,ground_height,ground_width

def coin_list(rects):
    coins_position =[(rect.x,rect.y-20) for rect in rects]
    return coins_position

def key_list(rects):
    keys_position =[rect.topright for rect in rects]
    return keys_position


# this is the main function
def main():
    # building the screen
    pygame.display.set_caption("Pixel Rampage")
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    FPS = 60


    #creating some needed variable for the game to run
    ## sounds
    play_starting_menu_music_one_time=True
    game_starting_music=Sound('assets\\audio\\starting_menu_music.mp3')
    game_over_sound =Sound("assets\\audio\\loss_sound.wav")
    level_music=Sound('assets\\audio\\Kim Lightyear - The Final.mp3')
    game_state = "start_game"
    pause_or_not = False
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
    ground1_position,ground3_position,ground4_position,ground_height,ground_width = ground_list(ground_type,screen_height)
    tree_position = (250,screen_height-ground_height)
    door_position = (max(ground1_position, key=lambda x: x[0])[0],screen_height - ground_height)

    #making the object
    start_game = StartGameMenu(screen_width, screen_height)
    pause_game = PauseGameMenu(screen_width, screen_height)
    game_over = GameOverMenu(screen_width, screen_height)
    level_one = LevelMaker(screen_width, screen_height, background_type,background_object_list[1],(200+ground_width/2+ground_width*3,screen_height-ground_height))
    player = Player("blue", (50, 200),[pygame.K_a, pygame.K_d, pygame.K_SPACE, pygame.K_f],"player_one")
    # player2 = Player("red", (100, 200),[pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_RSHIFT],"player_two")

    for position in range(4):
        level_one.add_ground(ground_type[0], (200+ground_width/2+ground_width*position,screen_height+50))
    # level_one.add_ground(ground_type[1], (2730, screen_height+600))
    # for position in ground3_position:
    #     level_one.add_ground(ground_type[2], position)
    # for position in ground4_position:
    #     level_one.add_ground(ground_type[3], position)

    level_one.add_level_object(background_object_list[0],level_one.get_grounds_rect()[0])
    # level_one.add_level_object(background_object_list[1],door_position)

    ground_rects = level_one.get_grounds_rect()
    coins_position = coin_list(ground_rects)
    keys_position = key_list(ground_rects)
    # print(keys_position)
    for position in coins_position:
        level_one.add_coin(coin_path,position)
    for position in keys_position:
        level_one.add_key(key_path,position)
    # level_one.add_coin(coin_path,(rects[1].x,rects[1].y-10))

    monster_1 = Monsters('assets\monsters\eater\eater_',level_one.get_grounds_rect()[1] ,400,3,13)

    

    while True:
        ground_rects = level_one.get_grounds_rect()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if game_state == "start_game":
                start_game.buttons[0].hover()
                start_game.buttons[1].hover()
                if play_starting_menu_music_one_time:
                    game_starting_music.play_sound(0.3)
                if start_game.buttons[0].button_clicked(event):
                    pygame.mouse.set_visible(False)
                    game_state = "playing"
                if start_game.buttons[1].button_clicked(event):
                    quit_game()
            elif game_state == "playing":
                game_starting_music.stop_sound()
                level_music.play_sound(0.4)

                # puase menu events handler
                if event.type == pygame.KEYDOWN and not pause_or_not:
                    if event.key == pygame.K_ESCAPE:
                        pause_or_not = True
                        pygame.mouse.set_visible(True)
                    if event.key == pygame.K_1:
                        pygame.mouse.set_visible(True)
                        game_over_sound.play_sound(1)
                        game_state = "game_over"

                if pause_or_not:
                    level_music.stop_sound()
                    pause_game.buttons[0].hover()
                    pause_game.buttons[1].hover()
                    if pause_game.buttons[0].button_clicked(event):
                        pygame.mouse.set_visible(False)
                        pause_or_not = False
                    if pause_game.buttons[1].button_clicked(event):
                        play_starting_menu_music_one_time = False
                        game_starting_music.play_sound(0.6)
                        level_one.level_reset()
                        player.reset_position()
                        # player2.reset_position()
                        pause_or_not = False
                        game_state = "start_game"
            
            if game_state == "game_over":
                level_music.stop_sound()
                game_over.buttons[0].hover()
                game_over.buttons[1].hover()
                if game_over.buttons[0].button_clicked(event):
                    level_one.level_reset()
                    player.reset_position()
                    # player2.reset_position()
                    pygame.mouse.set_visible(False)
                    game_over_sound.stop_sound()
                    game_state = "playing"
                if game_over.buttons[1].button_clicked(event):
                    level_one.level_reset()
                    player.reset_position()
                    # player2.reset_position()
                    play_starting_menu_music_one_time = False
                    game_starting_music.play_sound(0.6)
                    game_state = "start_game"
            

        if game_state == "start_game":
            start_game.start_game_draw(screen)
        elif game_state == "playing":
            if pause_or_not:
                pause_game.pause_game_draw(screen)
            else:
                # all the draws here
                level_one.draw(screen)
                monster_1.draw(screen)
                player.draw(screen)
                # player2.draw(screen)

                # all the update here and player2.get_player_position()> screen_width*0.5
                level_one.update_position(player.get_rect())

                # print(level_one.end_level(player.get_rect()))
                # # print(ground_rects)
                level_one.collect_coin(player.get_rect())
                level_one.collect_key(player.get_rect())
                # level_one.collect_coin(player2.get_rect())
                # level_one.collect_key(player2.get_rect())
                monster_1.movement()
                player.movment(ground_rects)
                # player2.movment(ground_rects)

            
        elif game_state == "game_over":
            game_over.game_over_draw(screen)

            
        # frame_rate = clock.get_fps()
        # print(frame_rate)
        clock.tick(FPS)
        pygame.display.update()


if __name__ == "__main__":
    main()
