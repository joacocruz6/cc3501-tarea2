from OpenGL.GL import *
from CC3501Utils import *
from Pared import *
from Player import *
from Bombs import *
from Explosion import *
import pygame
class Vista:
    def dibujar(self,power_ups,f,l_players,l_paredes,l_destructibes,l_bombas,l_enemigos,l_explosiones,l_win,ancho,alto):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        if f!=None:
            f.dibujar()
        for w in l_win:
            w.dibujar()
        for pw in power_ups:
            pw.crear()
            pw.dibujar()
        for p in l_players:
            p.crear()
            p.dibujar()
        for pared in l_paredes:
            pared.dibujar()
        for des in l_destructibes:
            des.dibujar()
        for bomba in l_bombas:
            bomba.crear()
            bomba.dibujar()
        for enemigo in l_enemigos:
            enemigo.dibujar()
        for exp in l_explosiones:
            exp.dibujar()
