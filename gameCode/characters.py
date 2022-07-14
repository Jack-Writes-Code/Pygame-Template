import pygame       as pg
import os

from .constants     import *
from .debug         import debug

class Character(pg.sprite.Sprite):
    """
    BASE CLASS FOR MANAGING CHARACTERS
        - MOVEMENT
        - COLLISION WITH OBSTACLE SPRITES
        - ANIMATION CYCLING
    """
    def __init__(self, name, position, sprite_groups, obstacle_sprites):
        super().__init__(sprite_groups)
        
        self.name = name
        self.direction = pg.math.Vector2()
        self.speed = 1
        self.visible_sprites = sprite_groups[0]
        self.obstacle_sprites = obstacle_sprites
        
        #RESOURCE_PATH AND OS.PATH.JOIN ARE BOTH USED HERE SO THAT PYINSTALLER WILL WORK WITH ASSETS
        self.image = pg.image.load(resource_path(os.path.join("assets", "placeholder.png")))
        self.rect = self.image.get_rect(topleft = position)
        self.hitbox = self.rect.inflate(-10,-20) #MAKE HITBOX SMALLER THAN SPRITE FOR MOVEMENT AND COMBAT
    
    def input(self):
        """
        THIS WILL BE AI TO DETERMINE OUTPUT VECTOR
        """
        pass
    
    def load_image(self, image_file_name, size=(30,32), forced=False):
        current_tick = pg.time.get_ticks()
        if current_tick - self.last_attack_frame >= self.attack_animation_duration or forced:
            self.image = pg.image.load(resource_path(os.path.join("assets/characters", image_file_name))).convert_alpha()
            self.image = pg.transform.scale(self.image, size) #SCALE THE 16X16 IMAGE TO GIVEN SIZE
    
    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize() #STOP DIAGANALS BEING TOO FAST
        
        self.hitbox.x += self.direction.x * self.speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * self.speed
        self.collision('verticle')
        self.rect.center = self.hitbox.center
    
    def collision(self,direction):
        """
        GO THROUGH ALL OBSTACLES AND IF PLAYER COLLIDES,
        SET PLAYER EDGE TO LINE UP WITH THE OPPOSING EDGE OF OBSTACLE
        """
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: #MOVING RIGHT
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: #MOVING LEFT
                        self.hitbox.left = sprite.hitbox.right
        
        if direction == 'verticle':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: #MOVING DOWN
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: #MOVING UP
                        self.hitbox.top = sprite.hitbox.bottom
    
    def update(self):
        self.input()
        self.move()
        #debug(f"{self.rect.x}, {self.rect.y}")
