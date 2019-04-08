import pygame as pg
import random

pg.init()

#boje
#LIGHTBLUE = pg.Color('lightskyblue2')
DARKBLUE = (11, 8, 69)
DARKGREEN = (0, 119, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLACK = (155, 230, 123)

#varijable
DISPLAY_WIDTH = 400
DISPLAY_HEIGHT = 600

gameDisplay = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
# width, height = gameDisplay.get_size()

clock = pg.time.Clock()
FPS = 30
all_sprites = pg.sprite.Group()
player_group = pg.sprite.GroupSingle()


class Balloons(pg.sprite.Sprite):

    def __init__(self, color):
        pg.sprite.Sprite.__init__(self)
        self.color = color
        self.image = pg.Surface((30, 30))
        self.image.fill(random.choice(self.color))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, DISPLAY_WIDTH - 50)
        self.rect.y = random.randrange(-400, 0)

    def update(self):
        #balon pada
        self.rect.y += 5

        # Kad dode do dna, generira se novi balon
        if self.rect.bottom > DISPLAY_HEIGHT:
            self.generate_balloons()

        cursor = pg.mouse.get_pos() # Uzimamo poziciju miša
        print(cursor)
        click = pg.mouse.get_pressed() # Jesmo li kliknuli mišom ili ne
        if self.rect.x + 50 > cursor[0] > self.rect.x and self.rect.y + 50 > cursor[1] > self.rect.y:
            print('prelazis')
            if click[0] == 1: # Ako kliknemo, balon nestane i generira se novi
                self.generate_balloons()

    # Funkcija koja generira nove balone
    def generate_balloons(self):
        self.rect.x = random.randrange(10, DISPLAY_WIDTH - 50)
        self.rect.y = random.randrange(-500, 0)
        self.image.fill(random.choice(self.color))


class Player(pg.sprite.Sprite):
    player_position = (DISPLAY_WIDTH/2, DISPLAY_HEIGHT-50)
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((60, 30))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect(center=self.player_position)
        self.move_x = 15

    def update(self, *args):
        keys = pg.key.get_pressed()
        self.move_player(keys)

    def move_player(self,keys):
        if keys[pg.K_LEFT]:
            self.rect.move_ip(-self.move_x, 0)
        elif keys[pg.K_RIGHT]:
            self.rect.move_ip(self.move_x, 0)


def game_loop():

    gameExit = False
    colors = [RED, BLUE, GREEN, YELLOW]
    ball_num = 4

    player = Player()
    player_group.add(player)
    all_sprites.add(player)

    # Kreiramo balone, kao instance klase
    for i in range(0, ball_num):
        balloon = Balloons(colors)
        all_sprites.add(balloon)


    # Dok traje igra
    while not gameExit:
        # Upravljanje događajima
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                gameExit = True

        # Update
        all_sprites.update()

        # Draw
        gameDisplay.fill(DARKBLUE)
        all_sprites.draw(gameDisplay)
        pg.draw.line(gameDisplay, DARKGREEN, (0, DISPLAY_HEIGHT), (400, DISPLAY_HEIGHT), 75)
        #player_group.draw(gameDisplay)


        pg.display.update()
        clock.tick(FPS)

    pg.quit()

game_loop()