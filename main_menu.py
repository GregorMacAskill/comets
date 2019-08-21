import pygame as pg
from settings import *
from text import *
from customisation_screen import *
from leaderboard import *
from random import randint

# function to detect whether or not the player's cursor is over a certain area
def cursor_over_button(x, y, width, height, mouse_pos):
    if x < mouse_pos[0] < (x + width) and y < mouse_pos[1] < (y + height):
        return True

# function to check if the player has clicked
def click():
    event = pg.event.poll()
    # if the player presses a mouse button and that mouse button is a left click
    if event.type == pg.MOUSEBUTTONUP and event.button == 1:
        return True


# making the main menu
def game_intro(display, clock, first_time, background_img):
    # blitting the background image to clear the display
    display.blit(background_img, [0, 0])
    if first_time:
        pg.mixer.music.load(main_menu_music)
        # using -1 to make music loop infinitely
        pg.mixer.music.play(-1)
    intro = True
    while intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        # displaying the background image
        display.blit(background_img, [0, 0])
        # displaying the title 'Comets'
        display.blit(title, [title_x, title_y])
        # displaying all of the buttons
        display.blit(play, [play_x, play_y])
        display.blit(instructions, [instructions_x, instructions_y])
        display.blit(customisation, [custom_x, custom_y])
        display.blit(game_quit, [quit_x, quit_y])

        # constantly getting the position of the mouse
        mouse_pos = pg.mouse.get_pos()

        if cursor_over_button(play_x, play_y, play_width, play_height, mouse_pos):
            display.blit(play_grey, [play_x, play_y])
            if click():
                pg.mixer.music.stop()
                first_time = False
                intro = False
                # if the player clicks 'Play', they are taken to the username screen
                username_function(display, clock, background_img)
        elif cursor_over_button(instructions_x, instructions_y, instructions_width, instructions_height, mouse_pos):
            display.blit(instructions_grey, [instructions_x, instructions_y])
            if click():
                first_time = False
                intro = False
                # if the player clicks 'Instructions', they are taken to the instructions screen
                instructions_screen(display, clock, background_img)
        elif cursor_over_button(custom_x, custom_y, custom_width, custom_height, mouse_pos):
            display.blit(customisation_grey, [custom_x, custom_y])
            if click():
                first_time = False
                intro = False
                # if the player clicks 'Customisation', they are taken to the customisation screen
                custom_screen(display, clock, background_img)
                display.blit(background_img, [0, 0])
        elif cursor_over_button(quit_x, quit_y, quit_width, quit_height, mouse_pos):
            display.blit(game_quit_grey, [quit_x, quit_y])
            if click():
                # if the player clicks 'Quit', the game quits and the window closes
                pg.quit()
                quit()
        clock.tick(FPS)
        pg.display.update()


# function for the instructions screen
def instructions_screen(display, clock, background_img):
    # blitting the background image to clear the display
    display.blit(background_img, [0, 0])
    instructions_bool = True
    while instructions_bool:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        # displaying all of the test related to the objective of the game
        display.blit(objective, [objective_x, objective_y])
        display.blit(objective_text1, [objective_text1_x, objective_text1_y])
        display.blit(objective_text2, [objective_text2_x, objective_text2_y])
        display.blit(objective_text3, [objective_text3_x, objective_text3_y])
        display.blit(objective_text4, [objective_text4_x, objective_text4_y])
        display.blit(objective_text5, [objective_text5_x, objective_text5_y])
        display.blit(objective_text6, [objective_text6_x, objective_text6_y])
        display.blit(objective_text7, [objective_text7_x, objective_text7_y])
        display.blit(objective_text8, [objective_text8_x, objective_text8_y])
        display.blit(objective_text9, [objective_text9_x, objective_text9_y])

        # displaying all of the test realted to the controls of the game
        display.blit(controls, [controls_x, controls_y])
        display.blit(controls_text1, [controls_text1_x, controls_text1_y])
        display.blit(controls_text2, [controls_text2_x, controls_text2_y])
        display.blit(controls_text3, [controls_text3_x, controls_text3_y])
        display.blit(controls_text4, [controls_text4_x, controls_text4_y])
        display.blit(controls_text5, [controls_text5_x, controls_text5_y])
        display.blit(controls_text6, [controls_text6_x, controls_text6_y])
        display.blit(back_button, [back_button_x, back_button_y])

        # constantly getting the position of the mouse
        mouse_pos = pg.mouse.get_pos()

        if cursor_over_button(back_button_x, back_button_y, back_button_width, back_button_height, mouse_pos):
            display.blit(back_button_grey, [back_button_x, back_button_y])
            if click():
                instructions_bool = False
                first_time = False
                # if the player clicks 'Back', they will be taken back to the main menu
                game_intro(display, clock, first_time, background_img)

        clock.tick(FPS)
        pg.display.update()

# function for the username screen
def username_function(display, clock, background_img):
    display.blit(background_img, [0, 0])
    display.blit(username_prompt, [username_prompt_x, username_prompt_y])
    # creating the font for the username
    font = pg.font.Font(None, 50)
    global username
    username = ""
    username_bool = True
    while username_bool:
        display.blit(username_prompt, [username_prompt_x, username_prompt_y])
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if len(username) < 12:
                    play_keyboard_sound()
                    # checking if input is a string of letters
                    if event.unicode.isalpha():
                        username += event.unicode
                    # checking if the input is an integer
                    elif event.unicode.isdigit():
                        username += event.unicode
                    elif event.key == pg.K_BACKSPACE:
                        # if the player presses 'BACKSPACE', the last letter will be removed from the username
                        username = username[:-1]
                    if len(username) != 0:
                        if event.key == pg.K_RETURN:
                            # if the length of the username is not equal to 0, the player can submit it by pressing enter
                            username_bool = False
                if len(username) >= 12:
                    # if the length of the username is 12, the player can only submit it or delete characters
                    if event.key == pg.K_BACKSPACE:
                        play_keyboard_sound()
                        username = username[:-1]
                    elif event.key == pg.K_RETURN:
                        username_bool = False
                display.blit(background_img, [0, 0])
        # rendering and displaying the username
        block = font.render(username, True, (255, 255, 255))
        rect = block.get_rect()
        rect.center = display.get_rect().center
        display.blit(block, rect)
        clock.tick(FPS)
        pg.display.update()

# function to return the username to 'main.py'
def returning_username():
    return username

# function to play a random keyboard sound while the player is typing their userame
def play_keyboard_sound():
    sound = randint(1, 7)
    if sound == 1:
        key1.play()
    elif sound == 2:
        key2.play()
    elif sound == 3:
        key3.play()
    elif sound == 4:
        key4.play()
    elif sound == 5:
        key5.play()
    elif sound == 6:
        key6.play()
    elif sound == 7:
        key7.play()

