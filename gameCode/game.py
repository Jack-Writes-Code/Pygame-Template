import pygame   as pg
import sys

from .constants import *
from .debug     import debug

from .player    import Player


class Game:
    """
    MAIN WINDOW HANDLER
        - CREATES WINDOW
        - HANDLES MAIN GAME LOOP
    """
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        pg.display.set_caption("Pygame Template by Jack-Writes-Code")
        programIcon = pg.image.load(resource_path(os.path.join("assets", "icon.png")))
        pg.display.set_icon(programIcon)
        self.clock = pg.time.Clock()
        
        """
        LEVEL CLASS GENERATES EVERYTHING AND HANDLES SPRITES
        """
        self.level = Level()
    
    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            
            self.screen.fill((0,0,0))
            self.level.run() #UPDATE GAME EACH FRAME
            #debug(round(self.clock.get_fps(), 2)) #DISPLAY FPS IN TOPLEFT CORNER
            pg.display.update()
            self.clock.tick(FPS)


class Level():
    """
    - LOADS THE MAP DATA
    - PLACES ALL SPRITES
    - CALLS UPDATE METHOD
    """
    def __init__(self):
        self.visible_sprites  = pg.sprite.Group()
        self.obstacle_sprites = pg.sprite.Group()
        self.display_surface = pg.display.get_surface()
        
        self.create_map()
    
    def create_map(self):
        """
        THIS WILL BE USED FOR GENERATING EVERYTHING ON THE SCREEEN INITITALLY
        CURRENTLY THIS WILL ONLY CREATE A CHARACTER INSTANCE
        """
        #self.visible_sprites.empty()
        #self.obstacle_sprites.empty()
        
        self.player = Player(
            name             = "player",
            position         = (SCREENWIDTH/2, SCREENHEIGHT/2),
            sprite_groups    = [self.visible_sprites], #MUST PASS 'visible_sprites' FIRST
            obstacle_sprites = self.obstacle_sprites
        )
    
    def run(self):
        """
        UPDATES AND DRAWS ALL VISIBLE SPRITES
        """
        self.visible_sprites.update()
        self.visible_sprites.draw(self.display_surface)
