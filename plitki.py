import pygame
import pygame.freetype as pf
import set


class Plitki:
    def __init__(self, size, name, x, y,numnote):
        self.size = size
        self.name = name
        self.getprsd = False
        self.wri = pf.Font(None, 30)
        self.sound = pygame.mixer.Sound('Sounds/' + self.name + '.ogg')
        self.proigr = False
        self.timenaz = 0
        self.numnote = numnote

        if self.size == 1:
            self.kart1 = pygame.image.load('short_tile.png')
            self.kart2 = pygame.image.load('short_tile_pressed.png')
        else:
            self.kart1 = pygame.image.load('long_tile.png')
            self.kart2 = pygame.image.load('long_tile_pressed.png')
        self.pazmer = self.kart1.get_size()
        self.rect = pygame.Rect([x, y - self.pazmer[1]], self.pazmer)
        self.image = self.kart1

    def draw(self, dp):
        dp.blit(self.image, self.rect)
        self.wri.render_to(dp, [self.rect.x + 15, self.rect.y + 15], self.name)

    def update(self):
        a = False
        if self.rect.y <= set.SIZE[1]:
            self.rect.y += 3
        r = pygame.mouse.get_pressed()
        if self.size == 2 and r[0] == True and self.rect.collidepoint(pygame.mouse.get_pos()) and self.getprsd == True:
            self.timenaz += 1
        else:
            self.timenaz = 0

        if self.timenaz == 60:
            self.proigr = True
            self.timenaz = 0
            self.image = self.kart2

    def nazat(self, dp):
        if self.getprsd == False:
            self.sound.play()
            self.getprsd = True
            if self.size == 1:
                self.proigr = True
                self.image = self.kart2



