import time
import set
import pygame as pg
import random
import plitki

pg.init()
pg.mixer.init()


class Main():
    def __init__(self):
        self.dp = pg.display.set_mode(set.SIZE)
        self.play = 1
        self.timal = pg.time.get_ticks()
        self.notatim = 0
        self.spisnot = []
        self.clock = pg.time.Clock()
    def draw(self):
        self.dp.fill([250, 200, 200])
        for i in self.spisnot:
            i.draw(self.dp)

    def event(self):
        evall = pg.event.get()
        for i in evall:
            if i.type == pg.QUIT:
                self.play = 0

    def circle(self):
        while self.play == 1:
            self.event()
            self.draw()
            self.update()
            self.clock.tick(set.FPS)

    def update(self):
        self.timal = pg.time.get_ticks()
        if self.timal - self.notatim >= 2000:
            plitka = plitki.Plitki(random.randint(1,2),'c4',random.randint(0,set.KOLPOL - 1) * set.SHIR,0)
            self.spisnot.append(plitka)
            self.notatim = self.timal
        for i in self.spisnot:
            i.update()




        pg.display.update()




game = Main()
game.circle()
