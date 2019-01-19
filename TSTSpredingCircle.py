import pygame
import os
import sys
import random as r
import math
import time

class circleCal():
    def __init__(self):
        self.dotNum = 8
        self.midAng = 360 / self.dotNum
        self.growRate = 2

    def AcutalMathCal(self):
        for n in range(len(the.Circle)):
            MPOSX = the.Circle[n][0]
            MPOSY = the.Circle[n][1]

            currentRad = the.Circle[n][2] + self.growRate
            SINVAL = math.sin(math.radians(self.midAng))
            print("SINVAL IS ", SINVAL)
            hight = SINVAL * currentRad

            instantX = MPOSX + currentRad
            instantY = MPOSY
            the.dots.append([instantX, instantY])

            instantX = round(MPOSX + hight)
            instantY = round(MPOSY + hight)
            the.dots.append([instantX, instantY])

            instantX = MPOSX
            instantY = MPOSY + currentRad
            the.dots.append([instantX, instantY])

            instantX = round(MPOSX - hight)
            instantY = round(MPOSY + hight)
            the.dots.append([instantX, instantY])

            instantX = MPOSX - currentRad
            instantY = MPOSY
            the.dots.append([instantX, instantY])

            instantX = round(MPOSX - hight)
            instantY = round(MPOSY - hight)
            the.dots.append([instantX, instantY])
            
            instantX = MPOSX
            instantY = MPOSY - currentRad
            the.dots.append([instantX, instantY])

            instantX = round(MPOSX + hight)
            instantY = round(MPOSY - hight)
            the.dots.append([instantX, instantY])
            
            the.Circle[n][2] += self.growRate
        
        

class MainGameOperator():
    def __init__(self):
        self.screenx = 700
        self.screeny = 700
        self.screen = pygame.display.set_mode((self.screenx, self.screeny))
        pygame.display.set_caption("Spreding Circle")

        self.gameStatus = True
        self.BGCol = (30, 30, 30)
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.gameSet()

    def gameSet(self):
        self.Circle = []
    
    def loopMain(self):
        while self.gameStatus == True:
            self.inputControl()
            for n in range((len(self.Circle))):
                print(n, "th Cicle is ", self.Circle[n])
            self.dots = []
            self.updateToCal()
            self.draw()

            pygame.display.update()
            

    def inputControl(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(event.type)
                self.gameStatus = True
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.gameStatus = False
                    print("Esc Key Pressed")
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = list(pygame.mouse.get_pos())
                print(pos)
                x = pos[0]
                y = pos[1]
                self.Circle.append([x, y, 0])
                print("M1 preseed")


    
    def updateToCal(self):
        blacklist = []
        for n in range(len(self.Circle)):
            if self.Circle[n][2] > 900:
                blacklist.append(n)
        
        for x in range(len(blacklist)):
            self.Circle.pop(blacklist[x])
        cal = circleCal()
        cal.AcutalMathCal()
        
    
    def draw(self):
        self.screen.fill(self.BGCol)

        for n in range(len(self.dots)):
            randCol = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
            curntpos = self.dots[n]
            pygame.draw.circle(self.screen, randCol, curntpos, 4)

if __name__ == '__main__':
    the = MainGameOperator()
    the.loopMain()