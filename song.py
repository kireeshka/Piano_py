import pygame as pg
import random
import  set
import plitki
import pygame.freetype as pf
class Song:
    def __init__(self,notes,longs):
        self.notesnames = notes
        self.longs = longs
        self.spisnot = []
        self.timal = pg.time.get_ticks()
        self.notatim = 0
        self.numnote = 0
        self.notes = notes
        self.wri = pf.Font(None, 30)
        self.nose = ''
        self.noteneprav = 0
        self.notepred = None


    def update(self):
        self.timal = pg.time.get_ticks()
        if self.timal - self.notatim >= 2000 :
            plitka = plitki.Plitki(self.longs[self.numnote],
                self.notesnames[self.numnote], random.randint(0, set.KOLPOL - 1) * set.SHIR, 0,self.numnote)
            self.notepred = plitka
            self.numnote += 1
            self.spisnot.append(plitka)
            self.notatim = self.timal
        for i in self.spisnot:
            i.update()


    def draw(self,dp):
        for i in self.spisnot:
            i.draw(dp)
        self.wri.render_to(dp, [set.SIZE[0] - 50,set.SIZE[1] - 30], self.nose)
    def allnoteVigr(self,numnote):
        for i in range(self.noteneprav + 1,numnote):
            if self.spisnot[i].proigr == False:
                self.noteneprav = i
                return False
        return True
