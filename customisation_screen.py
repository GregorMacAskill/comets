import pygame as pg
import main_menu
import settings
from text import *


# function for the customisation screen
def custom_screen(display, clock, background_img):
    display.blit(background_img, [0, 0])
    custom_bool = True
    # creating the white border for the background image
    pg.draw.rect(display, white, (background_title_x + 50, background_title_y + 150, 590, 490))
    # creating the preview image of the rocket sprite
    sprite = settings.player_sprite
    sprite_image = pg.image.load(sprite).convert()
    # scaling the sprite image
    sprite_image = pg.transform.scale(sprite_image, [500, 400])
    sprite_image.set_colorkey(white)
    # creating the preview image of the background image
    background_thumbnail = pg.transform.scale(background_img, [565, 465])
    # scaling the background image
    background_name_text = gameplay_text.render(default_background_name, True, white)
    while custom_bool:
        mouse_pos = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        # displaying everything on the customisation screen
        pg.draw.rect(display, white, (background_title_x + 50, background_title_y + 150, 590, 490))
        sprite_image = pg.image.load(sprite).convert()
        sprite_image = pg.transform.scale(sprite_image, [250, 200])
        sprite_image.set_colorkey(white)
        display.blit(background_title, [background_title_x, background_title_y])
        display.blit(rocket_title, [rocket_title_x, rocket_title_y])
        display.blit(sprite_image, [rocket_title_x + 100, rocket_title_y + 200])
        display.blit(background_name_text, [background_name_text_x, background_name_text_y])
        display.blit(background_thumbnail, [background_title_x + 65, background_title_y + 165])
        display.blit(change_button1, [change_button1_x, change_button1_y])
        display.blit(change_button2, [change_button2_x, change_button2_y])
        display.blit(custom_back_button, [custom_back_button_x, custom_back_button_y])

        if main_menu.cursor_over_button(change_button1_x, change_button1_y, change_button1_width, change_button1_height, mouse_pos):
            display.blit(change_button1_grey, [change_button1_x, change_button1_y])
            if main_menu.click():
                background_img = change_background(clock)
                background_name = get_background_name()
                background_name_text = gameplay_text.render(str(background_name), True, white)
                display.blit(background_img, [0, 0])
                background_thumbnail = pg.transform.scale(background_img, [565, 465])

        if main_menu.cursor_over_button(change_button2_x, change_button2_y, change_button2_width, change_button2_height, mouse_pos):
            display.blit(change_button2_grey, [change_button2_x, change_button2_y])
            if main_menu.click():
                sprite = change_rocket(clock)
                settings.player_sprite = sprite
                display.blit(background_img, [0, 0])

        if main_menu.cursor_over_button(custom_back_button_x, custom_back_button_y, custom_back_button_width, custom_back_button_height, mouse_pos):
            display.blit(custom_back_button_grey, [custom_back_button_x, custom_back_button_y])
            if main_menu.click():
                custom_bool = False
                first_time = False
                main_menu.game_intro(display, clock, first_time, background_img)

        clock.tick(FPS)
        pg.display.update()


# function that handles changing the background image
def change_background(clock):
    # creating all of the thumbnails for the available background images
    default_background_thumbnail = pg.transform.scale(default_background, [100, 100])
    europe_bg_thumbnail = pg.transform.scale(europe_bg, [100, 100])
    neptune_bg_thumbnail = pg.transform.scale(neptune_bg, [100, 100])
    saturn_rings_bg_thumbnail = pg.transform.scale(saturn_rings_bg, [100, 100])
    earth_from_moon_bg_thumbnail = pg.transform.scale(earth_from_moon_bg, [100, 100])
    andromeda_bg_thumbnail = pg.transform.scale(andromeda_bg, [100, 100])
    dark_side_bg_thumbnail = pg.transform.scale(dark_side_bg, [100, 100])
    saturn_eclipse_bg_thumbnail = pg.transform.scale(saturn_eclipse_bg, [100, 100])
    jupiter_from_europa_bg_thumbnail = pg.transform.scale(jupiter_from_europa_bg, [100, 100])

    changing = True
    # detecting which background image the player selects
    while changing:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    chosen_background = default_background
                    settings.background_img = default_background
                    changing = False
                elif event.key == pg.K_2:
                    chosen_background = europe_bg
                    settings.background_img = europe_bg
                    changing = False
                elif event.key == pg.K_3:
                    chosen_background = neptune_bg
                    settings.background_img = neptune_bg
                    changing = False
                elif event.key == pg.K_4:
                    chosen_background = saturn_rings_bg
                    settings.background_img = saturn_rings_bg
                    changing = False
                elif event.key == pg.K_5:
                    chosen_background = earth_from_moon_bg
                    settings.background_img = earth_from_moon_bg
                    changing = False
                elif event.key == pg.K_6:
                    chosen_background = andromeda_bg
                    settings.background_img = andromeda_bg
                    changing = False
                elif event.key == pg.K_7:
                    chosen_background = dark_side_bg
                    settings.background_img = dark_side_bg
                    changing = False
                elif event.key == pg.K_8:
                    chosen_background = saturn_eclipse_bg
                    settings.background_img = saturn_eclipse_bg
                    changing = False
                elif event.key == pg.K_9:
                    chosen_background = jupiter_from_europa_bg
                    settings.background_img = jupiter_from_europa_bg
                    changing = False

        # displaying all of the available background images
        pg.draw.rect(display, dark_grey, (200, 200, 940, 200))
        display.blit(default_background_thumbnail, [220, 250])
        display.blit(europe_bg_thumbnail, [320, 250])
        display.blit(neptune_bg_thumbnail, [420, 250])
        display.blit(saturn_rings_bg_thumbnail, [520, 250])
        display.blit(earth_from_moon_bg_thumbnail, [620, 250])
        display.blit(andromeda_bg_thumbnail, [720, 250])
        display.blit(dark_side_bg_thumbnail, [820, 250])
        display.blit(saturn_eclipse_bg_thumbnail, [920, 250])
        display.blit(jupiter_from_europa_bg_thumbnail, [1020, 250])

        display.blit(select_bg_text, [select_bg_text_x, select_bg_text_y])
        # displaying a number beneath each available background image
        for number in range(1, 10):
            number_text = gameplay_text.render(str(number), True, white)
            display.blit(number_text, [(100 * number + 155), 350])

        pg.display.update()
    return chosen_background


# function to return the name that will be displayed for the background image
def get_background_name():
    if settings.background_img == default_background:
        background_name = default_background_name
    elif settings.background_img == europe_bg:
        background_name = europe_bg_name
    elif settings.background_img == neptune_bg:
        background_name = neptune_bg_name
    elif settings.background_img == saturn_rings_bg:
        background_name = saturn_rings_bg_name
    elif settings.background_img == earth_from_moon_bg:
        background_name = earth_from_moon_bg_name
    elif settings.background_img == andromeda_bg:
        background_name = andromeda_bg_name
    elif settings.background_img == dark_side_bg:
        background_name = dark_side_bg_name
    elif settings.background_img == saturn_eclipse_bg:
        background_name = saturn_eclipse_bg_name
    elif settings.background_img == jupiter_from_europa_bg:
        background_name = jupiter_from_europa_bg_name
    return background_name


# function that handles changing the rocket sprite
def change_rocket(clock):
    # creating the thumbnails for all of the available rocket sprites
    default_ship_sprite_thumbnail = pg.transform.scale(default_ship_sprite_loaded, [100, 100])
    default_ship_sprite_thumbnail.set_colorkey(white)
    green_ship_sprite_thumbnail = pg.transform.scale(green_ship_sprite_loaded, [100, 100])
    green_ship_sprite_thumbnail.set_colorkey(white)
    orange_ship_thumbnail = pg.transform.scale(orange_ship_sprite_loaded, [100, 100])
    orange_ship_thumbnail.set_colorkey(white)
    blue_ship_thumbnail = pg.transform.scale(blue_ship_sprite_loaded, [100, 100])
    blue_ship_thumbnail.set_colorkey(white)
    pink_ship_thumbnail = pg.transform.scale(pink_ship_sprite_loaded, [100, 100])
    pink_ship_thumbnail.set_colorkey(white)
    yellow_ship_thumbnail = pg.transform.scale(yellow_ship_sprite_loaded, [100, 100])
    yellow_ship_thumbnail.set_colorkey(white)
    purple_ship_thumbnail = pg.transform.scale(purple_ship_sprite_loaded, [100, 100])
    purple_ship_thumbnail.set_colorkey(white)
    dark_blue_ship_thumbnail = pg.transform.scale(dark_blue_ship_sprite_loaded, [100, 100])
    dark_blue_ship_thumbnail.set_colorkey(white)
    dark_green_ship_thumbnail = pg.transform.scale(dark_green_ship_sprite_loaded, [100, 100])
    dark_green_ship_thumbnail.set_colorkey(white)
    changing = True
    # detecting which rocket sprite the player selects
    while changing:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    settings.player_sprite = default_ship_sprite
                    sprite = default_ship_sprite
                    changing = False
                elif event.key == pg.K_2:
                    settings.player_sprite = green_ship_sprite
                    sprite = green_ship_sprite
                    changing = False
                elif event.key == pg.K_3:
                    settings.player_sprite = orange_ship_sprite
                    sprite = orange_ship_sprite
                    changing = False
                elif event.key == pg.K_4:
                    settings.player_sprite = blue_ship_sprite
                    sprite = blue_ship_sprite
                    changing = False
                elif event.key == pg.K_5:
                    settings.player_sprite = pink_ship_sprite
                    sprite = pink_ship_sprite
                    changing = False
                elif event.key == pg.K_6:
                    settings.player_sprite = yellow_ship_sprite
                    sprite = yellow_ship_sprite
                    changing = False
                elif event.key == pg.K_7:
                    settings.player_sprite = purple_ship_sprite
                    sprite = purple_ship_sprite
                    changing = False
                elif event.key == pg.K_8:
                    settings.player_sprite = dark_blue_ship_sprite
                    settings.player_sprite = dark_blue_ship_sprite
                    sprite = dark_blue_ship_sprite
                    changing = False
                elif event.key == pg.K_9:
                    settings.player_sprite = dark_green_ship_sprite
                    sprite = dark_green_ship_sprite
                    changing = False

        # displaying all of the available rocket sprites
        pg.draw.rect(display, dark_grey, (display_width * 0.14, display_height * 0.3, 902, 240))
        display.blit(default_ship_sprite_thumbnail, [180, 280])
        display.blit(green_ship_sprite_thumbnail, [280, 280])
        display.blit(orange_ship_thumbnail, [380, 280])
        display.blit(blue_ship_thumbnail, [480, 280])
        display.blit(pink_ship_thumbnail, [580, 280])
        display.blit(yellow_ship_thumbnail, [680, 280])
        display.blit(purple_ship_thumbnail, [780, 280])
        display.blit(dark_blue_ship_thumbnail, [880, 280])
        display.blit(dark_green_ship_thumbnail, [980, 280])

        display.blit(select_rocket_text, [select_rocket_text_x, select_rocket_text_y])
        # displaying a number beneath each rocket sprite
        for number in range(1, 10):
            number_text = gameplay_text.render(str(number), True, white)
            display.blit(number_text, [(100 * number + 120), 400])

        clock.tick(FPS)
        pg.display.update()
    return sprite
