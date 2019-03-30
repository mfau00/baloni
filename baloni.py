import pygame
import random
import time

pygame.init()

LIGHTBLUE = (0, 178, 238)
DARKBLUE = (0, 0, 180)
display_width = 500
display_height = 600
clock = pygame.time.Clock()
FPS = 30

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Balloons")

all_sprites = pygame.sprite.Group()

class Balloons(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(DARKBLUE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, display_width - 20)

    def update(self):
        self.rect.y += 5

        if self.rect.bottom > display_height:
            self.rect.top = 0
            self.rect.x = random.randrange(0, display_width - 20)





balloon = Balloons()
all_sprites.add(balloon)


gameExit = False

while not gameExit:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    all_sprites.update()
    gameDisplay.fill(LIGHTBLUE)
    all_sprites.draw(gameDisplay)

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
quit()
