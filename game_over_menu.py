import pygame as pg
from settings import *
from text import *
from sprites import *


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


def show_game_over_screen(display, clock):
    game_over_bool = True
    while game_over_bool:
        display.blit(game_over, [game_over_x, game_over_y])
        display.blit(play_again, [play_again_x, play_again_y])
        display.blit(main_menu_button, [main_menu_button_x, main_menu_button_y])
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    game_over_bool = False
                    return True
                elif event.key == pg.K_2:
                    game_over_bool = False
                    username_needed = False
                    return False

        mouse_pos = pg.mouse.get_pos()

        if cursor_over_button(play_again_x, play_again_y, play_again_width, play_again_height, mouse_pos):
            display.blit(play_again_grey, [play_again_x, play_again_y])

        elif cursor_over_button(main_menu_button_x, main_menu_button_y, main_menu_button_width, main_menu_button_height, mouse_pos):
            display.blit(main_menu_button_grey, [main_menu_button_x, main_menu_button_y])



        pg.display.update()
        clock.tick(FPS)