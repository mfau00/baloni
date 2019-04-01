import pygame as pg
import random

pg.init() #prije nego počnemo rad s Pygame paketom, potrebno je inicijalizirati njegove module (tu spada display, draw itd)

LIGHTBLUE = pg.Color('lightskyblue2')
DARKBLUE = (11, 8, 69)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

gameDisplay = pg.display.set_mode((400, 600))
width, height = gameDisplay.get_size()
pg.display.set_caption("Balloons")

#pg.mouse.set_visible(False) ovako se onemogući da se miš vidi
clock = pg.time.Clock()
FPS = 30

class Player(pg.sprite.Sprite):
    player_position = (200, 550) #pocetna pozicija

    def __init__(self, image):
        super().__init__() #potrebna da se nasljede atributi nadklase
        self.size = (30, 25)
        self.mx = 5
        self.bounds = pg.Rect(10, 500, 380, 25)
        self.image = pg.transform.scale(image, self.size)     #  namistimo da slika playera odgovara dimenzijama
        self.rect = self.image.get_rect(center=self.player_position)

    def update(self, keys, *args):
        if keys[pg.K_LEFT]:
            self.rect.move_ip(-self.mx, 0)
        elif keys[pg.K_RIGHT]:
            self.rect.move_ip(self.mx, 0)
        self.rect.clamp_ip(self.bounds)


class Balloons(pg.sprite.Sprite):
    first_ball_position = (100, 50)
    def __init__(self, image):
        super().__init__()
        self.size = (30, 30)
        self.image = pg.transform.scale(image, self.size)
        self.rect = self.image.get_rect(center = self.first_ball_position)

    def update(self, *args):
        self.rect.y += 5


class Game:
    def __init__(self):
        self.images = {}
        self.load_images()
        self.player = None
        self.balloon = None

        self.game_started = True

        self.all_sprites = pg.sprite.Group() #spremamo sve spritove
        self.player_single = pg.sprite.GroupSingle() #spremamo jedan spriter, a to je player
        self.balloons_group = pg.sprite.Group()

    def create_sprites(self):
        self.create_player()
        self.create_balloons()


    def load_images(self):
        image_names = ["player2"]
        for img in image_names:
            self.images[img] = pg.image.load(f"{img}.jpg").convert()
            self.images[img].set_colorkey(pg.Color("Black"))

        self.images["background"] = pg.image.load("back.png").convert()
        self.images["balloon_red"] = pg.image.load("balloon_red.png").convert()

    def process_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return True

    def create_player(self):
        self.player = Player(self.images["player2"])
        self.player_single.add(self.player)
        self.all_sprites.add(self.player)

    def create_balloons(self):
        self.balloon = Balloons(self.images["balloon_red"])
        self.balloons_group.add(self.balloon)
        self.all_sprites.add(self.balloon)

    def display_frame(self, gameDisplay):

        gameDisplay.fill(DARKBLUE)
        keys = pg.key.get_pressed()
        self.create_sprites()
        self.all_sprites.update(keys)
        self.all_sprites.draw(gameDisplay)

        pg.display.flip()


gameExit = False

game = Game()
while not gameExit:
    
    gameExit = game.process_events()
    game.display_frame(gameDisplay) #prikaz na ekranu
    clock.tick(FPS)

pg.quit()

