import pygame as pg
from settings import*

pg.font.init()

# main menu text #

title_font = pg.font.SysFont('couriernew', 150, bold=True)
title = title_font.render("Comets", True, white)
title_x = display_width * 0.30
title_y = display_height * 0.15


title_options = pg.font.SysFont('couriernew', 80)

play = title_options.render("Play", True, white)
play_grey = title_options.render("Play", True, grey)
play_width = play.get_width()
play_height = play.get_height()
play_x = display_width * 0.43
play_y = display_height * 0.4

instructions = title_options.render("Instructions", True, white)
instructions_grey = title_options.render("Instructions", True, grey)
instructions_width = instructions.get_width()
instructions_height = instructions.get_height()
instructions_x = display_width * 0.29
instructions_y = display_height * 0.5

customisation = title_options.render("Customisation", True, white)
customisation_grey = title_options.render("Customisation", True, grey)
custom_width = customisation.get_width()
custom_height = customisation.get_height()
custom_x = display_width * 0.27
custom_y = display_height * 0.6

# name has to be different from the 'quit()' function
game_quit = title_options.render("Quit", True, white)
game_quit_grey = title_options.render("Quit", True, grey)
quit_width = game_quit.get_width()
quit_height = game_quit.get_height()
quit_x = display_width * 0.42
quit_y = display_height * 0.8


# instructions screen text
instructions_text = pg.font.SysFont('couriernew', 20)
instructions_title = title_font.render('Instructions', True, white)
instructions_title_x = display_width * 0.1
instructions_title_y = display_height * 0.03

objective = title_options.render("Objective", True, white)
objective_x = display_width * 0.02
objective_y = display_height * 0.2
objective_text1 = instructions_text.render("Your hyperdrive has failed and you find yourself", True, white)
objective_text1_x = display_width * 0.02
objective_text1_y = display_height * 0.4
objective_text2 = instructions_text.render("in a dense comet field and with no immediate means of escape.", True, white)
objective_text2_x = display_width * 0.02
objective_text2_y = display_height * 0.45
objective_text3 = instructions_text.render("Your only chance of survival relies on destroying", True, white)
objective_text3_x = display_width * 0.02
objective_text3_y = display_height * 0.5
objective_text4 = instructions_text.render("the comets with your laser cannons.", True, white)
objective_text4_x = display_width * 0.02
objective_text4_y = display_height * 0.55
objective_text5 = instructions_text.render("Doing so will increase your score so you can compete with", True, white)
objective_text5_x = display_width * 0.02
objective_text5_y = display_height * 0.6
objective_text6 = instructions_text.render("other pilots who have been in your situation.", True, white)
objective_text6_x = display_width * 0.02
objective_text6_y = display_height * 0.65
objective_text7 = instructions_text.render("The smaller the comet, the more points you will gain.", True, white)
objective_text7_x = display_width * 0.02
objective_text7_y = display_height * 0.7
objective_text8 = instructions_text.render("Destroying rare, radioactive comets will give ", True, white)
objective_text8_x = display_width * 0.02
objective_text8_y = display_height * 0.75
objective_text9 = instructions_text.render("your ship extra shields", True, white)
objective_text9_x = display_width * 0.02
objective_text9_y = display_height * 0.80


controls = title_options.render("Controls", True, white)
controls_x = display_width * 0.6
controls_y = display_height * 0.2
controls_text1 = instructions_text.render("Thrust - W", True, white)
controls_text1_x = display_width * 0.6
controls_text1_y = display_height * 0.4
controls_text2 = instructions_text.render("Rotate Clockwise - D", True, white)
controls_text2_x = display_width * 0.6
controls_text2_y = display_height * 0.5
controls_text3 = instructions_text.render("Rotate Anticlockwise - A", True, white)
controls_text3_x = display_width * 0.6
controls_text3_y = display_height * 0.6
controls_text4 = instructions_text.render("Shoot - SPACE (hold to shoot constantly)", True, white)
controls_text4_x = display_width * 0.6
controls_text4_y = display_height * 0.7
controls_text5 = instructions_text.render("Pause - P", True, white)
controls_text5_x = display_width * 0.6
controls_text5_y = display_height * 0.8
controls_text6 = instructions_text.render("Quit - ESC", True, white)
controls_text6_x = display_width * 0.6
controls_text6_y = display_height * 0.9

back_button_text = pg.font.SysFont('couriernew', 30)

back_button = back_button_text.render("Back", True, white)
back_button_grey = back_button_text.render("Back", True, grey)
back_button_width = back_button.get_width()
back_button_height = back_button.get_height()
back_button_x = display_width * 0.05
back_button_y = display_height * 0.9


# game text

gameplay_text = pg.font.SysFont('couriernew', 30)

lives = gameplay_text.render("Lives:", True, white)

score = gameplay_text.render("Score:", True, white)

# post-game text
game_over_text = pg.font.SysFont('couriernew', 150)
game_over_options = pg.font.SysFont('couriernew', 40)

game_over = game_over_text.render("GAME OVER", True, white)
game_over_x = display_width * 0.2
game_over_y = display_height * 0.01

play_again = game_over_options.render("1 | Play Again", True, white)
play_again_grey = game_over_options.render("1 | Play Again", True, grey)
play_again_width = play_again.get_width()
play_again_height = play_again.get_height()
play_again_x = display_width * 0.1
play_again_y = display_height * 0.9

main_menu_button = game_over_options.render("2 | Main Menu", True, white)
main_menu_button_grey = game_over_options.render("2 | Main Menu", True, grey)
main_menu_button_width = main_menu_button.get_width()
main_menu_button_height = main_menu_button.get_height()
main_menu_button_x = display_width * 0.7
main_menu_button_y = display_height * 0.9


# leaderboard font
leaderboard_text = pg.font.SysFont('couriernew', 40)

rank_text = leaderboard_text.render('Rank', True, white)
name_text = leaderboard_text.render('Name', True, white)
score_text = leaderboard_text.render('Score', True, white)

# username text
username_prompt_text = pg.font.SysFont('couriernew', 50)
username_prompt = username_prompt_text.render("Please enter a username:", True, white)
username_prompt_x = display_width * 0.25
username_prompt_y = display_height * 0.35


# customisation screen text

background_title = title_options.render("Background", True, white)
background_title_x = display_width * 0.02
background_title_y = display_height * 0.05

rocket_title = title_options.render("Rocket", True, white)
rocket_title_x = display_width * 0.6
rocket_title_y = display_height * 0.05

change_button1 = back_button_text.render("Change", True, white)
change_button1_grey = back_button_text.render("Change", True, grey)
change_button1_width = change_button1.get_width()
change_button1_height = change_button1.get_height()
change_button1_x = display_width * 0.4
change_button1_y = display_height * 0.95

change_button2 = back_button_text.render("Change", True, white)
change_button2_grey = back_button_text.render("Change", True, grey)
change_button2_width = change_button2.get_width()
change_button2_height = change_button2.get_height()
change_button2_x = display_width * 0.8
change_button2_y = display_height * 0.95

custom_back_button = back_button_text.render("Back", True, white)
custom_back_button_grey = back_button_text.render("Back", True, grey)
custom_back_button_width = back_button.get_width()
custom_back_button_height = back_button.get_height()
custom_back_button_x = display_width * 0.05
custom_back_button_y = display_height * 0.95

select_bg_text = gameplay_text.render("Select a background image using the number keys:", True, white)
select_bg_text_x = display_width * 0.16
select_bg_text_y = display_height * 0.3

select_rocket_text = gameplay_text.render("Select a rocket sprite using the number keys:", True, white)
select_rocket_text_x = display_width * 0.15
select_rocket_text_y = display_height * 0.3


background_name_text_x = display_width * 0.05 + 10
background_name_text_y = display_height * 0.2

# paused text

paused_text = game_over_text.render('PAUSED', True, white)
paused_text_x = display_width * 0.3
paused_text_y = display_height * 0.35