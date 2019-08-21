import pygame as pg
import settings
from random import randint
import time
import math
# module to handle vectors
vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self, player_spawn_time):
        # inheriting from the pygame sprite class
        pg.sprite.Sprite.__init__(self)
        self.player_spawn_time = player_spawn_time
        self.sprite = settings.transparent_player_sprite
        self.image_master = pg.image.load(self.sprite).convert()
        self.image_master.set_colorkey(settings.white)
        self.image = self.image_master.copy()
        self.rect = self.image_master.get_rect()
        self.rect.center = (settings.display_width / 2, settings.display_height / 2)
        self.pos = vec(settings.display_width / 2, settings.display_height / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.rot = 0
        self.rotacc = 0
        self.lasers = pg.sprite.Group()
        self.thrust_sprite = pg.sprite.Group()
        self.last_shot = pg.time.get_ticks()
        self.run_once1 = 0
        self.run_once2 = 0

    # handles everything about the Player class that changes
    def update(self):
        self.time = pg.time.get_ticks()
        if self.time - self.player_spawn_time <= settings.inv_duration:
            # if the time that the player has been spawned/respawned for is less than the 'inv_duration', the rocket sprite will be the grey sprite
            if self.run_once1 == 0:
                self.sprite = settings.transparent_player_sprite
                self.image_master = pg.image.load(self.sprite).convert()
                self.image_master.set_colorkey(settings.black)
                self.image = self.image_master.copy()
                self.run_once1 = 1
        else:
            # if the time that the player has been spawned/respawned for is less than the 'inv_duration', the rocket sprite will be whichever sprite is selected
            if self.run_once2 == 0:
                self.sprite = settings.player_sprite
                self.image_master = pg.image.load(self.sprite).convert()
                self.image_master.set_colorkey(settings.white)
                self.image = self.image_master.copy()
                # making it so that the player's rotation does not reset when the sprite image changes
                if 0 <= self.rot <= 360:
                    self.rotate_left(self.image_master, self.rot)
                else:
                    self.rotate_right(self.image_master, self.rot)
                self.run_once2 = 1
        self.acc = vec(0, 0)
        self.rad = math.radians(self.rot)
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            pg.mixer.Channel(0).play(settings.thrust_sound)
            # as trigonometric functions (sin & cos) are used, there need to be some exceptions
            if self.rot == 0:
                self.acc.y -= settings.player_acc
            elif self.rot == 180 or self.rot == -180:
                self.acc.y += settings.player_acc
            elif self.rot == 90:
                self.acc.x -= settings.player_acc
            elif self.rot == -90:
                self.acc.x += settings.player_acc
            elif self.rot == 270:
                self.acc.x += settings.player_acc
            elif self.rot == -270:
                self.acc.x -= settings.player_acc
            elif 0 < self.rot < 90:
                self.acc.y = math.cos(self.rad) * -settings.player_acc
                self.acc.x = math.sin(self.rad) * -settings.player_acc
            elif -90 < self.rot < 0:
                self.acc.y = -(math.cos(self.rad) * settings.player_acc)
                self.acc.x = math.sin(self.rad) * -settings.player_acc
            elif -180 < self.rot < -90:
                self.acc.y = math.cos(self.rad) * -settings.player_acc
                self.acc.x = math.sin(self.rad) * -settings.player_acc
            elif -270 < self.rot < -180:
                self.acc.y = math.cos(self.rad) * -settings.player_acc
                self.acc.x = math.sin(self.rad) * -settings.player_acc
                self.acc.x = math.sin(self.rad) * -settings.player_acc
            elif -360 < self.rot < -270:
                self.acc.y = math.cos(self.rad) * -settings.player_acc
                self.acc.x = math.sin(self.rad) * -settings.player_acc
            elif 90 < self.rot < 180:
                self.acc.y = math.cos(self.rad) * -settings.player_acc
                self.acc.x = math.sin(self.rad) * -settings.player_acc
            elif 180 < self.rot < 270:
                self.acc.y = math.cos(self.rad) * -settings.player_acc
                self.acc.x = math.sin(self.rad) * -settings.player_acc
            elif 270 < self.rot < 360:
                self.acc.y = math.cos(self.rad) * -settings.player_acc
                self.acc.x = math.sin(self.rad) * -settings.player_acc
        if not keys[pg.K_w]:
            settings.thrust_sound.fadeout(250)
        if keys[pg.K_d]:
            self.rotate_right(self.image_master, self.rot)
        if keys[pg.K_a]:
            self.rotate_left(self.image_master, self.rot)
        # using this the boolean method so that the player cannot hold down space to fire many lasers repeatedly
        if keys[pg.K_SPACE]:
            if self.sprite == settings.transparent_player_sprite:
                damage_laser = False
            else:
                damage_laser = True
            self.shoot(self.rect.centerx, self.rect.centery, self.rot, damage_laser)
        # friction increases as velocity increases
        self.acc += self.vel * settings.player_dec
        self.vel += self.acc
        # s = ut + 0.5at^2; t = 1
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.y < 0:
            self.pos.y = settings.display_height
        elif self.pos.y > settings.display_height:
            self.pos.y = 0
        if self.pos.x < 0:
            self.pos.x = settings.display_width
        elif self.pos.x > settings.display_width:
            self.pos.x = 0
        self.rect.center = self.pos
        # setting up mask for more accurate collisions
        self.mask = pg.mask.from_surface(self.image)

    # function to rotate the rocket to the left (anti-clockwise)
    def rotate_left(self, image_master, rot):
        self.image = pg.transform.rotate(image_master, rot)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.rot += settings.player_rot_vel
        if self.rot >= 360:
            self.rot = 0

    # function to rotate the rocket to the right (clockwise)
    def rotate_right(self, image_master, rot):
        self.image = pg.transform.rotate(image_master, rot)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.rot -= settings.player_rot_vel
        if self.rot <= -360:
            self.rot = 0

    # function that handles shooting lasers
    def shoot(self, x, y, ang, damage):
        now = pg.time.get_ticks()
        if now - self.last_shot > settings.ship_shoot_delay:
            # if the time since the player last shot is greater than the shooting delay, then the player can shoot again
            self.last_shot = now
            # playing a 1 of 4 random shooting sounds
            sound = randint(1, 4)
            if sound == 1:
                pg.mixer.Channel(1).play(settings.laser_sound_1)
            elif sound == 2:
                pg.mixer.Channel(1).play(settings.laser_sound_2)
            elif sound == 3:
                pg.mixer.Channel(1).play(settings.laser_sound_3)
            elif sound == 4:
                pg.mixer.Channel(1).play(settings.laser_sound_4)
            # adding a new laser to the laser sprite group
            new_laser = Laser(x, y, ang, self.vel, damage)
            self.lasers.add(new_laser)

    def reset_pos(self):
        pg.mixer.Channel(2).play(settings.ship_destroy_sound)
        self.rect.center = (settings.display_width / 2, settings.display_height / 2)
        self.pos = vec(settings.display_width / 2, settings.display_height / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.rot = 5
        self.rotacc = 0
        # making it so that the rocket sprite matches with its new rotation (0)
        self.rotate_right(self.image_master, self.rot)
        self.player_spawn_time = pg.time.get_ticks()

class Laser(pg.sprite.Sprite):
    def __init__(self, x, y, ang, player_vel, damage):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.ang = ang
        self.starting_vel = player_vel
        self.damage = damage
        self.rad = math.radians(self.ang)
        self.image = pg.Surface((5, 5))
        self.image.fill(settings.red)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.pos = vec(x, y)
        self.vel = vec(0,0)
        # as trigonometric functions (sin & cos) are used, there need to be some exceptions
        if self.ang == 0:
            self.vel.y -= settings.laser_vel
        elif self.ang == 180 or self.ang == -180:
            self.vel.y += settings.laser_vel
        elif self.ang == 90:
            self.vel.x -= settings.laser_vel
        elif self.ang == -90:
            self.vel.x += settings.laser_vel
        elif self.ang == 270:
            self.vel.x += settings.laser_vel
        elif self.ang == -270:
            self.vel.x -= settings.laser_vel
        elif 0 < self.ang < 90:
            self.vel.y = math.cos(self.rad) * -settings.laser_vel
            self.vel.x = math.sin(self.rad) * -settings.laser_vel
        elif -90 < self.ang < 0:
            self.vel.y = -(math.cos(self.rad) * +settings.laser_vel)
            self.vel.x = math.sin(self.rad) * -settings.laser_vel
        elif -180 < self.ang < -90:
            self.vel.y = math.cos(self.rad) * -settings.laser_vel
            self.vel.x = math.sin(self.rad) * -settings.laser_vel
        elif -270 < self.ang < -180:
            self.vel.y = math.cos(self.rad) * -settings.laser_vel
            self.vel.x = math.sin(self.rad) * -settings.laser_vel
        elif -360 < self.ang < -270:
            self.vel.y = math.cos(self.rad) * -settings.laser_vel
            self.vel.x = math.sin(self.rad) * -settings.laser_vel
        elif 90 < self.ang < 180:
            self.vel.y = math.cos(self.rad) * -settings.laser_vel
            self.vel.x = math.sin(self.rad) * -settings.laser_vel
        elif 180 < self.ang < 270:
            self.vel.y = math.cos(self.rad) * -settings.laser_vel
            self.vel.x = math.sin(self.rad) * -settings.laser_vel
        elif 270 < self.ang < 360:
            self.vel.y = math.cos(self.rad) * -settings.laser_vel
            self.vel.x = math.sin(self.rad) * - settings.laser_vel
        self.time_created = pg.time.get_ticks()

    # handles everything about the Laser class that changes
    def update(self):
        if not 0 < self.rect.x < settings.display_width:
            self.kill()
        if not 0 < self.rect.y < settings.display_height:
            self.kill()
        self.now = pg.time.get_ticks()
        if self.now - self.time_created > settings.laser_range:
            self.kill()
        self.pos += self.starting_vel
        self.pos += self.vel
        self.rect.center = self.pos


class Comet(pg.sprite.Sprite):
    # first 2 are for large comets, second 2 for medium, third 2 for small
    vel = [1.5, -1.5, 2.0, -2.0, 3.5, -3.5]
    # first 2 are for large comets, second 2 for medium, third 2 for small
    spin = [1, -1, 1.5, -1.5, 2, -2]

    def __init__(self, size, pos):
        pg.sprite.Sprite.__init__(self)
        self.size = size
        self.ang = 0
        self.pos = pos
        if self.size == 0:
            # if the comet has a size of 0 (small), its sprite image will be the small comet image and its velocity and rotation will be set appropriately
            self.image_master = pg.image.load(settings.small_comet_sprite).convert()
            self.image_master.set_colorkey(settings.white)
            self.image = self.image_master.copy()
            self.vel = vec(Comet.vel[randint(4, 5)], Comet.vel[randint(4, 5)])
            self.spin = Comet.spin[4 + randint(0, 1)]
            self.buffer = settings.small_buffer
            self.is_special = False
            self.special = randint(0, 100)
            # 5% chance of small comet being a special comet
            if self.special < 5:
                self.is_special = True
                self.image_master = pg.image.load(settings.special_comet_sprite).convert()
                self.image_master.set_colorkey(settings.white)
                self.image = self.image_master.copy()
                self.vel = vec(5, 5)
        elif self.size == 1:
            # if the comet has a size of 1 (medium), its sprite image will be the medium comet image and its velocity and rotation will be set appropriately
            self.image_master = pg.image.load(settings.med_comet_sprite).convert()
            self.image_master.set_colorkey(settings.white)
            self.image = self.image_master.copy()
            self.vel = vec(Comet.vel[randint(2, 3)], Comet.vel[randint(2, 3)])
            self.spin = Comet.spin[2 + randint(0, 1)]
            self.buffer = settings.med_buffer
        elif self.size == 2:
            # if the comet has a size of 2 (large), its sprite image will be the large comet image and its velocity and rotation will be set appropriately
            self.image_master = pg.image.load(settings.large_comet_sprite).convert()
            self.image_master.set_colorkey(settings.white)
            self.image = self.image_master.copy()
            self.vel = vec(Comet.vel[randint(0, 1)], Comet.vel[randint(0, 1)])
            self.spin = Comet.spin[0 + randint(0, 1)]
            self.buffer = settings.large_buffer
        self.image.set_colorkey(settings.white)
        self.rect = self.image_master.get_rect()
        # if the comet has a predefined position, its centre will be set to that position
        if self.pos != None:
            self.rect.center = self.pos
        # if the comet does not have a predefined position, its centre will be set to a random location
        else:
            self.rect.center = (randint(0, display_width), randint(0, settings.display_height))
            self.pos = vec(self.rect.centerx, self.rect.centery)

    # handles everything about the Comet class that changes
    def update(self):
        # updating the comet's position
        self.pos += self.vel
        # updating the sprite's position
        self.rect.center = self.pos
        # making the comet constantly rotate
        self.image = pg.transform.rotate(self.image_master, self.ang)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.ang += self.spin
        self.mask = pg.mask.from_surface(self.image)
        # handling the wraparound of the comet
        if self.rect.midbottom[1] < 0:
            self.rect[1] += settings.display_height + self.buffer
        elif self.rect.midtop[1] > settings.display_height:
            self.rect[1] -= (settings.display_height + self.buffer)
        elif self.rect.midleft[0] > settings.display_width:
            self.rect[0] -= (settings.display_width + self.buffer)
        elif self.rect.midright[0] < 0:
            self.rect[0] += (settings.display_width + self.buffer)

    def split(self):
        if self.size == 1:
            settings.comet_destroy_sound.play()
            create_comets(3, 0)
            # removes the comet from the sprite group
            self.kill()
        else:
            settings.comet_destroy_sound.play()
            create_comets(3, 1)
            # removes the comet from the sprite group
            self.kill()

class Explosion(pg.sprite.Sprite):
    def __init__(self, center, size):
        pg.sprite.Sprite.__init__(self)
        self.size = size
        self.image = settings.explo_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pg.time.get_ticks()
        # time wait between each frame of animation i.e. speed of explosion
        self.frame_rate = 50

    # handles everything about the Explosion class that changes
    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(settings.explo_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = settings.explo_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
