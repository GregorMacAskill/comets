# GAMEPLAY FOR COMETS

import pygame as pg
import settings
from text import *
from sprites import *
import main_menu
import game_over_menu
import leaderboard
from customisation_screen import *
from random import randint
import os


class Game:
    running = True

    def __init__(self):
        # initialises all sound pygame sound functions
        pg.init()
        # creating the display, complete with 'Comets' caption
        self.display = pg.display.set_mode((display_width, display_height), pg.HWSURFACE) #| pg.FULLSCREEN)
        pg.display.set_caption(CAPTION)
        # establishing the game clock that is used to time certain events
        self.clock = pg.time.Clock()
        self.running = True
        self.player_lives = player_lives
        self.score = 0
        self.scores = []
        self.lives_number = gameplay_text.render(str(self.player_lives), True, white)
        self.score_number = gameplay_text.render(str(self.score), True, white)
        self.leaderboard_data = []
        self.last_hit = 0
        self.current_session_scores = []

    # method for starting new game
    def new(self, number, size):
        self.all_sprites = pg.sprite.Group()
        self.comets = pg.sprite.Group()
        self.player_spawn_time = pg.time.get_ticks()
        self.player = Player(self.player_spawn_time)
        self.all_sprites.add(self.player)
        self.create_comets(number, size, pos=None)
        self.last_spawn = pg.time.get_ticks()
        self.horizontal_velocity = gameplay_text.render(str(round(self.player.vel[0], 2)), True, white)
        self.vertical_velocity = gameplay_text.render(str(round(self.player.vel[1], 2)), True, white)
        self.rotation_display = gameplay_text.render(str(abs(self.player.rot)), True, white)
        self.run()

    # method to control everything that must happen to keep the game running
    def run(self):
        # adding the game's FPS to the caption
        self.caption_FPS = round(self.clock.get_fps())
        pg.display.set_caption(CAPTION + " " + str(self.caption_FPS))
        # loading the background gameplay music
        pg.mixer.music.load(gameplay_music)
        # looping the music -1 times so that it loops indefinitely
        pg.mixer.music.play(-1)
        self.clock.tick(FPS)
        self.playing = True
        # game loop
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()
            self.update()
    # update for the main game loop
    def update(self):
        self.all_sprites.update()
        self.all_sprites.add(self.player.lasers)
        self.horizontal_velocity = gameplay_text.render(str(round(self.player.vel[0], 2)), True, white)
        self.vertical_velocity = gameplay_text.render(str(round(self.player.vel[1], 2)), True, white)
        self.rotation_display = gameplay_text.render(str(abs(self.player.rot)), True, white)
        self.now = pg.time.get_ticks()
        # condition to check if collisions between the rocket and the comets can occur
        if self.player.sprite != transparent_player_sprite:
            # checking for collisions between the player's rocket and the comets sprite group
            # the 'True' parameter makes it so that the rocket sprite and the comet disappear (rocket will be respawned)
            for hit in pg.sprite.spritecollide(self.player, self.comets, True, pg.sprite.collide_mask):
                # everytime there is a collision between the rocket and a comet the following occur
                self.player_lives -= 1
                self.lives_number = gameplay_text.render(str(self.player_lives), True, white)
                self.score += 20
                self.score_number = gameplay_text.render(str(self.score), True, white)
                self.player.reset_pos()
                self.player.run_once1 = 0
                self.player.run_once2 = 0
                # splitting the comet if it the rocket hits it
                self.comet_split(hit)
        for laser in self.player.lasers:
            # condition to ensure that laser was shot after invulnerability period
            if laser.damage:
                # checking for collisions between comets and lasers sprite groups
                # the 'True' parameter makes it so that the laser and comet will both disappear
                for hit in pg.sprite.groupcollide(self.comets, self.player.lasers, True, pg.sprite.collide_mask):
                    pg.mixer.Channel(3).play(comet_destroy_sound)
                    self.comet_split(hit)
                    # if the comet's size was large, the player will gain 20 points and there will be a large explosion
                    if hit.size == 2:
                        self.score += 20
                        expl = Explosion(hit.rect.center, 'lg')
                        self.all_sprites.add(expl)
                    # if the comet's size was medium, the player will gain 50 points and there will be a medium explosion
                    elif hit.size == 1:
                        self.score += 50
                        expl = Explosion(hit.rect.center, 'med')
                        self.all_sprites.add(expl)
                    # if the comet's size was small, the player will gain 100 points and there will be a small explosion
                    elif hit.size == 0:
                        if hit.is_special:
                            # if the player destroys a special comet, they gain a life
                            self.player_lives += 1
                            self.lives_number = gameplay_text.render(str(self.player_lives), True, white)
                        self.score += 100
                        expl = Explosion(hit.rect.center, 'sm')
                        self.all_sprites.add(expl)
                    # updating the on-screen score number
                    self.score_number = gameplay_text.render(str(self.score), True, white)
        # if time since last comets spawned is greater than 10000ms (10 sec) then 5 more large comets will spawn
        # they will have a 'random' position within a certain range
        if self.now - self.last_spawn > 10000:
            self.create_comets(5, 2, 'rand')
            self.last_spawn = pg.time.get_ticks()
        if self.player_lives <= 0:
            # getting the player's username from the main_menu module
            player_username = main_menu.returning_username()
            leaderboard.save_score(self.score)
            self.high_score = leaderboard.find_high_score(leaderboard.scores)
            high_score_text = leaderboard_text.render('High Score:' + str(self.high_score), True, white)
            self.score_number = gameplay_text.render(str(self.score), True, white)
            thrust_sound.stop()
            # if the player has lost all of their lives, their username and score will be saved to the 'scores.txt' file
            with open('scores.txt', 'a') as file:
                # username and score are separated by comma and different entries are separated by a newline
                file.write(str(player_username + str(',') + str(self.score) + "\n"))
            f = open("scores.txt", "r")
            for line in f:
                # .strip() function removes newline at the end of each line | .rsplit() stops reading the string once it reaches the specified character (,)
                self.leaderboard_data.append(line.strip().rsplit(','))
            # calling the function to sort the leaderboard data
            sorted = leaderboard.sorting_and_ranking(self.leaderboard_data)
            leaderboard.write_leaderboard_to_file(sorted)
            # displaying the leaderboard
            leaderboard.display_leaderboard(sorted, self.display, high_score_text)
            # displaying the 'game_over_screen' and determining if the player wants to play again
            keep_playing = game_over_menu.show_game_over_screen(self.display, self.clock)
            # if the player wants to continue playing the game (i.e. if they select 'Play Again') a new instance of the game will be created
            if keep_playing:
                # creating a new instance of the game
                new_game = Game()
                while new_game.running:
                    new_game.new(10, 2)
                    new_game.draw()
                    new_game.clock.tick(FPS)
                    self.player_spawn_time = pg.time.get_ticks()
            # if the player does not want to continue playing the game (i.e. they select 'Main Menu') they will be taken back to the Main Menu
            else:
                leaderboard.scores = []
                self.playing = False
                self.running = False
                new_game = Game()
                while new_game.running:
                    game_instance.show_main_menu()
                    new_game.new(10, 2)
                    new_game.draw()
                    game_instance.show_main_menu()
                    new_game.clock.tick(FPS)

    # all of the event that need to be handled during the gameplay that are separate from any classes
    def events(self):
        for event in pg.event.get():
            # if the player clicks the red 'X' in the top right corner of the window (they won't actually be able to do this as the game is fullscreen)
            if event.type == pg.QUIT:
                # stop playing the game
                self.playing = False
                # stop running the whole program
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    # pausing the game
                    self.pause()

    # drawing every graphic used within the gameplay to the display
    def draw(self):
        self.display.blit(settings.background_img, [0, 0])
        self.all_sprites.draw(self.display)
        self.display.blit(lives, [(display_width * 0.05), (display_height * 0.05)])
        self.display.blit(self.lives_number, [(display_width * 0.15), (display_height * 0.05)])
        self.display.blit(score, [(display_width * 0.8), (display_height * 0.05)])
        self.display.blit(self.score_number, [(display_width * 0.9), (display_height * 0.05)])
        pg.display.update()


    def show_main_menu(self):
        # using a boolean see if it the first time that the player has been on the title screen since they launched the game
        # this is used to ensure that the music does not start again when the user returns to this screen
        self.first_time = True
        main_menu.game_intro(self.display, self.clock, self.first_time, settings.background_img)

    # function to generate the position of the initial comets
    def generate_start_comet_pos(self):
        left_or_right = randint(0,1)
        if left_or_right == 0:
            self.x_pos = randint(0, 590)
        elif left_or_right == 1:
            self.x_pos = randint(690, 1280)
        top_or_bottom = randint(0, 1)
        if top_or_bottom == 0:
            self.y_pos = randint(0, 310)
        elif top_or_bottom == 1:
            self.y_pos = randint(360, 720)
        self.pos = self.x_pos, self.y_pos
        return self.pos

    # function to generate the position of the comets that spawn every 10 seconds
    # this function ensures that the player will not see the comets spawn as they spawn off-screen
    def generate_comet_pos_outside(self):
        left_or_right = randint(0, 1)
        if left_or_right == 0:
            self.x_pos = randint(-20, -10)
        elif left_or_right == 1:
            self.x_pos = randint(display_width + 10, display_width + 20)
        top_or_bottom = randint(0, 1)
        if top_or_bottom == 0:
            self.y_pos = randint(-20, -10)
        elif top_or_bottom == 1:
            self.y_pos = randint(display_height + 10, display_height + 20)
        self.pos = self.x_pos, self.y_pos
        return self.pos

    # function to generate the position of comets that are produced from a larger comet being destroyed
    def genereate_comet_pos(self, parent_rect):
        # comets that spawn from a larger comet splitting will be within 10 pixels of their parent comet
        self.x_pos = parent_rect[0] + randint(-10, 10)
        self.y_pos = parent_rect[1] + randint(-10, 10)
        self.pos = self.x_pos, self.y_pos

    #function to add new comets to the comets sprite group
    def create_comets(self, number, size, pos):
        for i in range(number):
            if pos == None:
                self.pos = self.generate_start_comet_pos()
            if pos == 'rand':
                self.pos = self.generate_comet_pos_outside()
            self.new_comet = Comet(size, self.pos)
            self.comets.add(self.new_comet)
            self.all_sprites.add(self.new_comet)
            self.list_of_comets = pg.sprite.Group.sprites(self.comets)

    # function to split a larger comet into smaller comets
    def comet_split(self, comet):
        if comet.size == 2:
            # if the comet's size was 2 (large), 3 medium comets will be created around the initial comet's position
            self.genereate_comet_pos(comet.rect.center)
            self.create_comets(3, 1, self.pos)
        elif comet.size == 1:
            # if the comet's size was 1 (medium), 3 small comets will be created around the initial comet's position
            self.genereate_comet_pos(comet.rect.center)
            self.create_comets(3, 0, self.pos)

    # function to pause the game
    def pause(self):
        display.blit(paused_text, [paused_text_x, paused_text_y])
        pg.display.update()
        paused = True
        while paused:
            # while the game has been paused, the game won't do anything apart from detecting the player pressing 'P'
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_p:
                        paused = False

# if guard
if __name__ == '__main__':

    # creating a new instance of the game
    game_instance = Game()

    # MAIN GAME LOOP
    while game_instance.running:
        game_instance.show_main_menu()
        # initialising the new game instance with 10 size 2 (large) comets
        game_instance.new(10, 2)
        game_instance.draw()
        game_instance.clock.tick(FPS)

# quitting pygame and python if the game has been closed
pg.quit()
quit()

