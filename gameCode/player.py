import pygame       as pg
import os

from .characters    import Character
from .constants     import *
from .debug         import debug

class Player(Character):
    """
    SUBCLASS OF CHARACTER FOR THE GAMES PLAYER
    HANDLES USER INPUT TO CONTROL THE CHARACTER ONSCREEN
    """
    def __init__(self, name, position, sprite_groups, obstacle_sprites):
        super().__init__(name, position, sprite_groups, obstacle_sprites)
        self.speed = 4
    
    def input(self):
        """
        TAKES THE KEYS BEING PRESSED AND IF WASD OR ARROW KEYS ARE PRESSED
        IT WILL CHANGE THE X & Y POSITIONS OF THE PLAYER ACCORDINGLY
        """
        keys = pg.key.get_pressed()
        
        #IF UP/DOWN KEYS ARE PRESSED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.direction.y = -1
        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        
        #IF RIGHT/LEFT KEYS ARE PRESSED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.direction.x = 1
        elif keys[pg.K_LEFT] or keys[pg.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0
