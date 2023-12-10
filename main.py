import time
import set
import pygame as pg
import random
import plitki
import song
import pygame.freetype

pg.init()
pg.mixer.init()


class Main():
    def __init__(self):
        self.dp = pg.display.set_mode(set.SIZE)
        self.menuorgame = 0
        self.play = 1
        self.song = song.Song(set.CHRISTMAS_TREE_NOTES, set.CHRISTMAS_TREE_DURATION)
        self.life = 3
        self.clock = pg.time.Clock()
        self.dvig = True
        self.timeost = -1000
        self.menupng = pg.image.load('menu.png')


    def draw(self):
        self.dp.fill([250, 200, 200])
        self.song.draw(self.dp)
    def drawmenu(self):
        self.dp.blit(self.menupng,[0,0])
    def evemenu(self):
        evall = pg.event.get()
        for i in evall:
            if i.type == pg.QUIT:
                self.play = 0
    def updmenu(self):
        pg.display.update()






    def event(self):
        evall = pg.event.get()
        for i in evall:
            if i.type == pg.QUIT:
                self.play = 0
            if i.type == pg.MOUSEBUTTONDOWN :
                for u in self.song.spisnot:
                    if u.rect.collidepoint(i.pos):
                        if self.song.allnoteVigr(u.numnote) == False:

                            self.timeost = pg.time.get_ticks()
                            print('Neprav')
                            self.life -= 1
                            self.dvig = False

                        u.nazat(self.dp)
                        self.song.nose = u.name
    def game(self):
        self.event()
        self.draw()
        if pg.time.get_ticks() - self.timeost >= 1000:
            self.dvig = True
        if self.dvig:
            self.update()
        if self.life <= 0:
            self.play = 0
    def menu(self):
        self.evemenu()
        self.drawmenu()
        self.updmenu()








    def circle(self):
        while self.play == 1:
            if self.menuorgame == 0:
                self.menu()
            if self.menuorgame == 1:
                self.game()

            self.clock.tick(set.FPS)

    def update(self):
        self.song.update()
        self.promax()
        if len(self.song.notes) == self.song.numnote:
            self.play = 0
        pg.display.update()
    def promax(self):
        a = pg.mouse.get_pressed()
        print(a)
        if a[0] == True or a[1] == True or a[2] == True:
            for k in self.song.spisnot:
                if k.rect.collidepoint(pg.mouse.get_pos()):
                    return True
            self.life -= 1
            self.dvig = False
            self.timeost = pg.time.get_ticks()

            return False


game = Main()
game.circle()
