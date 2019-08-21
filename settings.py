import os
import platform
import pygame as pg


pg.init()
# initialising the pygame's mixer module to handle sounds
pg.mixer.init()

# SETTINGS FOR GAME #

# Setting display dimensions
display_width = 1280
display_height = 720
display = pg.display.set_mode((display_width, display_height), pg.RESIZABLE)

# setting the maximum FPS to 120
FPS = 120
# setting the window captino to 'Comets'
CAPTION = "Comets"

# setting colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
grey = (128, 128, 128)
dark_grey = (75, 75, 75)

# setting up assets folders #
# finding file path of game
game_folder = os.path.dirname(__file__)
# getting img_folder file path
img_folder = os.path.join(game_folder, 'img')
# getting snd_folder file path
snd_folder = os.path.join(game_folder, 'sound')

# SOUNDS
# setting the number of sound channels to 10, so that 10 sounds could potentially play at once
pg.mixer.set_num_channels(10)
main_menu_music = os.path.join(snd_folder, 'menu.ogg')
gameplay_music = os.path.join(snd_folder, 'gameplay_music.wav')

thrust_wav = os.path.join(snd_folder, 'thrust.wav')
thrust_sound = pg.mixer.Sound(thrust_wav)

ship_destroy_wav = os.path.join(snd_folder, 'ship_destroy.wav')
ship_destroy_sound = pg.mixer.Sound(ship_destroy_wav)
ship_destroy_sound.set_volume(0.5)

comet_destroy_wav = os.path.join(snd_folder, 'comet_destroy.wav')
comet_destroy_sound = pg.mixer.Sound(comet_destroy_wav)

laser_sound_1_wav = os.path.join(snd_folder, 'laser1.wav')
laser_sound_1 = pg.mixer.Sound(laser_sound_1_wav)
laser_sound_2_wav = os.path.join(snd_folder, 'laser2.wav')
laser_sound_2 = pg.mixer.Sound(laser_sound_2_wav)
laser_sound_3_wav = os.path.join(snd_folder, 'laser3.wav')
laser_sound_3 = pg.mixer.Sound(laser_sound_3_wav)
laser_sound_4_wav = os.path.join(snd_folder, 'laser4.wav')
laser_sound_4 = pg.mixer.Sound(laser_sound_4_wav)


# typing sounds | Copyright 2012 eklee http://freesound.org/people/eklee/ | Copyright 2012 qubodup http://freesound.org/people/qubodup/ extraction of single sounds | License: CC Attribution 3.0 http://creativecommons.org/licenses/by/3.0/

key1_wav = os.path.join(snd_folder, 'key1.wav')
key1 = pg.mixer.Sound(key1_wav)
key2_wav = os.path.join(snd_folder, 'key2.wav')
key2 = pg.mixer.Sound(key2_wav)
key3_wav = os.path.join(snd_folder, 'key3.wav')
key3 = pg.mixer.Sound(key3_wav)
key4_wav = os.path.join(snd_folder, 'key4.wav')
key4 = pg.mixer.Sound(key4_wav)
key5_wav = os.path.join(snd_folder, 'key5.wav')
key5 = pg.mixer.Sound(key5_wav)
key6_wav = os.path.join(snd_folder, 'key6.wav')
key6 = pg.mixer.Sound(key6_wav)
key7_wav = os.path.join(snd_folder, 'key7.wav')
key7 = pg.mixer.Sound(key7_wav)


# IMAGES
default_ship_sprite = os.path.join(img_folder, 'ship.png')
transparent_player_sprite = os.path.join(img_folder, 'trans_ship.png')
ship_thrust_sprite = os.path.join(img_folder, 'ship_thrust.png')
green_ship_sprite = os.path.join(img_folder, 'green_ship.png')
orange_ship_sprite = os.path.join(img_folder, 'orange_ship.png')
blue_ship_sprite = os.path.join(img_folder, 'blue_ship.png')
pink_ship_sprite = os.path.join(img_folder, 'pink_ship.png')
yellow_ship_sprite = os.path.join(img_folder, 'yellow_ship.png')
purple_ship_sprite = os.path.join(img_folder, 'purple_ship.png')
dark_blue_ship_sprite = os.path.join(img_folder, 'dark_blue_ship.png')
dark_green_ship_sprite = os.path.join(img_folder, 'dark_green_ship.png')
player_sprite = default_ship_sprite

default_ship_sprite_loaded = pg.image.load(default_ship_sprite).convert()
green_ship_sprite_loaded = pg.image.load(green_ship_sprite).convert()
orange_ship_sprite_loaded = pg.image.load(orange_ship_sprite).convert()
blue_ship_sprite_loaded = pg.image.load(blue_ship_sprite).convert()
pink_ship_sprite_loaded = pg.image.load(pink_ship_sprite).convert()
yellow_ship_sprite_loaded = pg.image.load(yellow_ship_sprite).convert()
purple_ship_sprite_loaded = pg.image.load(purple_ship_sprite).convert()
dark_blue_ship_sprite_loaded = pg.image.load(dark_blue_ship_sprite).convert()
dark_green_ship_sprite_loaded = pg.image.load(dark_green_ship_sprite).convert()

small_comet_sprite = os.path.join(img_folder, 'small_comet.png')
med_comet_sprite = os.path.join(img_folder, 'med_comet.png')
large_comet_sprite = os.path.join(img_folder, 'large_comet.png')
special_comet_sprite = os.path.join(img_folder, 'special_comet.png')


default_background = pg.image.load(os.path.join(img_folder, 'default_bg_img.jpg'))
default_background_name = 'Galaxies'

blue_planet_bg = pg.image.load(os.path.join(img_folder, 'blue_planet.jpg'))
blue_planet_bg_name = 'Blue Planet'

europe_bg = pg.image.load(os.path.join(img_folder, 'europe.jpg'))
europe_bg_name = 'Europe'

neptune_bg = pg.image.load(os.path.join(img_folder, 'earth_and_milkyway2.jpg'))
neptune_bg_name = 'Earth and Milky Way'

saturn_rings_bg = pg.image.load(os.path.join(img_folder, 'rings.jpg'))
saturn_rings_bg_name = 'Rings of Saturn'

earth_from_moon_bg = pg.image.load(os.path.join(img_folder, 'earth_from_moon3.jpg'))
earth_from_moon_bg_name = 'Earth from Moon'

andromeda_bg = pg.image.load(os.path.join(img_folder, 'andromeda.jpg'))
andromeda_bg_name = 'Andromeda'

dark_side_bg = pg.image.load(os.path.join(img_folder, 'neptune.jpg'))
dark_side_bg_name = 'Neptune'

saturn_eclipse_bg = pg.image.load(os.path.join(img_folder, 'saturn_eclipse1.jpg'))
saturn_eclipse_bg_name = 'Saturn Eclipse'

jupiter_from_europa_bg = pg.image.load(os.path.join(img_folder, 'jupiter_from_europa.jpg'))
jupiter_from_europa_bg_name = 'Jupiter from Europa'

background_img = default_background


# loading images for explosion animation
explo_anim = {}
explo_anim['lg'] = []
explo_anim['med'] = []
explo_anim['sm'] = []

for i in range(11):
    filename = 'explo{}.png'.format(i)
    img = pg.image.load(os.path.join(img_folder, filename)).convert()
    img.set_colorkey(black)
    img_lg = pg.transform.scale(img, (150, 150))
    explo_anim['lg'].append(img_lg)
    img_med = pg.transform.scale(img, (100, 100))
    explo_anim['med'].append(img_med)
    img_sm = pg.transform.scale(img, (50,50))
    explo_anim['sm'].append(img_sm)

# determining os of system that game is running on
os = platform.system()

# PLAYER SETTINGS
# 30 FPS:player_acc = 0.3 60FPS = 0.1
player_acc = 0.3
player_dec = -0.01
#  30 FPS: player_rot_vel = 11.5 60 FPS = 6.5
player_rot_vel = 11.5
player_lives = 1
# 60 FPS = 300, 30 FPS =300
ship_shoot_delay = 300
# 60 FPS 1000, 30 FPS 2500
laser_range = 2500

# player invulnerability duration (milliseconds)
inv_duration = 3000

# laser settings
vec = pg.math.Vector2
# 60 FPS 10, 30 FPS 15
laser_vel = 15

# comet wraparound buffer

small_buffer = 50
med_buffer = 100
large_buffer = 150
