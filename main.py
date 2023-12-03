import time
import set
import pygame as pg
import random
import plitki
import song

pg.init()
pg.mixer.init()


class Main():
    def __init__(self):
        self.dp = pg.display.set_mode(set.SIZE)
        self.play = 1
        self.song = song.Song(set.CHRISTMAS_TREE_NOTES, set.CHRISTMAS_TREE_DURATION)

        self.clock = pg.time.Clock()

    def draw(self):
        self.dp.fill([250, 200, 200])
        self.song.draw(self.dp)


    def event(self):
        evall = pg.event.get()
        for i in evall:
            if i.type == pg.QUIT:
                self.play = 0
            if i.type == pg.MOUSEBUTTONDOWN:
                for u in self.song.spisnot:
                    if u.rect.collidepoint(i.pos):
                        u.nazat(self.dp)
                        self.song.nose = u.name
        a = pg.mouse.get_pressed()
        print(a)



    def circle(self):
        while self.play == 1:
            self.event()
            self.draw()
            self.update()
            self.clock.tick(set.FPS)

    def update(self):
        self.song.update()

        pg.display.update()


game = Main()
game.circle()
