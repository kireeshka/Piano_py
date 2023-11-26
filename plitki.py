import pygame

import set


class Plitki:
    def __init__(self, size, name, x, y):
        self.size = size
        self.name = name
        self.getprsd = False

        if self.size == 1:
            self.kart1 = pygame.image.load('short_tile.png')
            self.kart2 = pygame.image.load('short_tile_pressed.png')
        else:
            self.kart1 = pygame.image.load('long_tile.png')
            self.kart2 = pygame.image.load('long_tile_pressed.png')
        self.pazmer = self.kart1.get_size()
        self.rect = pygame.Rect([x, y - self.pazmer[1]],self.pazmer)


    def draw(self, dp):
        dp.blit(self.kart1, self.rect)

    def update(self):
        if self.rect.y <= set.SIZE[1]:
            self.rect.y += 3
