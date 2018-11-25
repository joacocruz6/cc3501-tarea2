import os
import random
import pygame
from CC3501Utils import *
from Pared import *
from Vista import *
from Player import *
from Enemy import *
from BUtils import *
from Explosion import *
from Bombs import *
from PDes import *
from Fondo import *
from Power import *
import random as ran
import math as m
os.environ['SDL_VIDEO_CENTERED'] = '1'
def main(args):
    ancho = 800
    alto = 600
    dx = 53.0
    dy = 46.0
    init(ancho,alto,"Modelo")
    vista=Vista()
    dibujos=[Fondo(),Win(Vector(0.0,0.0))]# cosas a dibujar
    run=True
    while run:
        for event in pygame.event.get():
            if event.type==QUIT:
                run=False
            vista.dibujar(dibujos,None,[],[],[],[],[],[],[],ancho,alto)  # dibujo
            pygame.display.flip()
            pygame.time.wait(int(1000 / 60))  # 60 fps
    pygame.quit()
if __name__=="__main__":
    import sys
    main(sys.argv)