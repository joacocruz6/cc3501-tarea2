from CC3501Utils import *
import math as m
from pygame.locals import *
class Enemy(Figura):
    def __init__(self,pos: Vector,tipo: int,vivo=True,rgb=(1.0,1.0,51.0/255)):
        self._tipo=tipo
        self.vivo=vivo
        self._r_x = 53.0 / 2
        self._r_y = 46.0 / 2
        self.centro=Vector(pos.x+(53.0/2),pos.y+(46.0/2))
        super().__init__(pos,rgb)
    def figura(self):
        """
        Crea el dibujo de los enemigos, es llamado por el metodo dibujar de la clase padre
        :return: None
        """


        (r,g,b)=self.color
        ##################
        ###Rafa Gorgori###
        ##################
        if self._tipo==1:
            dx=53.0/14
            dy=46.0/16
            ##############
            ###Contorno###
            ##############
            glColor3f(0.0,0.0,0.0)
            glBegin(GL_POLYGON)
            glVertex2f(7*dx,6*dy)
            glVertex2f(7*dx,15*dy)
            glVertex2f(10*dx,15*dy)
            glVertex2f(10*dx,14*dy)
            glVertex2f(11*dx,14*dy)
            glVertex2f(11*dx,12*dy)
            glVertex2f(12*dx,12*dy)
            glVertex2f(12*dx,8*dy)
            glVertex2f(13*dx,8*dy)
            glVertex2f(13*dx,6*dy)
            glEnd()
            glBegin(GL_POLYGON)
            glVertex2f(7 * dx, 6 * dy)
            glVertex2f(7 * dx, 15 * dy)
            glVertex2f(4 * dx, 15 * dy)
            glVertex2f(4 * dx, 14 * dy)
            glVertex2f(3 * dx, 14 * dy)
            glVertex2f(3 * dx, 12 * dy)
            glVertex2f(2 * dx, 12 * dy)
            glVertex2f(2 * dx, 8 * dy)
            glVertex2f(dx, 8 * dy)
            glVertex2f(dx, 6 * dy)
            glEnd()
            #piernas
            glBegin(GL_QUADS)
            glVertex2f(3*dx,6*dy)
            glVertex2f(11*dx,6*dy)
            glVertex2f(11*dx,2*dy)
            glVertex2f(3*dx,2*dy)
            glEnd()
            #detalles
            glBegin(GL_QUADS)
            glVertex2f(2*dx,5*dy)
            glVertex2f(2*dx,6*dy)
            glVertex2f(3*dx,6*dy)
            glVertex2f(3*dx,5*dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(11 * dx, 5 * dy)
            glVertex2f(11 * dx, 6 * dy)
            glVertex2f(12 * dx, 6 * dy)
            glVertex2f(12 * dx, 5 * dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(4*dx,dy)
            glVertex2f(4*dx,2*dy)
            glVertex2f(6*dx,2*dy)
            glVertex2f(6*dx,dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(8 * dx, dy)
            glVertex2f(8 * dx, 2 * dy)
            glVertex2f(10 * dx, 2 * dy)
            glVertex2f(10 * dx, dy)
            glEnd()
            glColor3f(138.0/255,138.0/255,138.0/255)
            glBegin(GL_QUADS)
            glVertex2f(2*dx,9*dy)
            glVertex2f(2*dx,11*dy)
            glVertex2f(3*dx,11*dy)
            glVertex2f(3*dx,9*dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(11 * dx, 9 * dy)
            glVertex2f(11 * dx, 11 * dy)
            glVertex2f(12 * dx, 11 * dy)
            glVertex2f(12 * dx, 9 * dy)
            glEnd()





            ###figura###
            #---zapatos---#
            glColor3f(0.2, 0.2, 0.2)
            glBegin(GL_QUADS)
            glVertex2f(4*dx,2*dy)
            glVertex2f(4 * dx, 3 * dy)
            glVertex2f(6*dx,3*dy)
            glVertex2f(6*dx,2*dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(8 * dx, 2 * dy)
            glVertex2f(8 * dx, 3 * dy)
            glVertex2f(10 * dx, 3 * dy)
            glVertex2f(10 * dx, 2 * dy)
            glEnd()
            #---pantalones---#
            glColor3f(165.0/255,0.0,38.0/255)
            glBegin(GL_QUADS)
            glVertex2f(4*dx,3*dy)
            glVertex2f(4*dx,6*dy)
            glVertex2f(6*dx,6*dy)
            glVertex2f(6*dx,3*dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(8 * dx, 3 * dy)
            glVertex2f(8 * dx, 6 * dy)
            glVertex2f(10 * dx, 6 * dy)
            glVertex2f(10 * dx, 3 * dy)
            glEnd()
            #---ropa---#
            glColor3f(50.0/255,50.0/255,152.0/255)
            glBegin(GL_QUADS)
            glVertex2f(4*dx,6*dy)
            glVertex2f(4*dx,7*dy)
            glVertex2f(10*dx,7*dy)
            glVertex2f(10*dx,6*dy)
            glEnd()
            #hombros
            glBegin(GL_QUADS)
            glVertex2f(4*dx,7*dy)
            glVertex2f(4*dx,8*dy)
            glVertex2f(5*dx,8*dy)
            glVertex2f(5*dx,7*dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(4 * dx, 8 * dy)
            glVertex2f(4 * dx, 9 * dy)
            glVertex2f(3 * dx, 9 * dy)
            glVertex2f(3 * dx, 8 * dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(2 * dx, 7 * dy)
            glVertex2f(2 * dx, 8 * dy)
            glVertex2f(3 * dx, 8 * dy)
            glVertex2f(3 * dx, 7 * dy)
            glEnd()
            #derecho
            glBegin(GL_QUADS)
            glVertex2f(9 * dx, 7 * dy)
            glVertex2f(9 * dx, 8 * dy)
            glVertex2f(10 * dx, 8 * dy)
            glVertex2f(10 * dx, 7 * dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(10 * dx, 8 * dy)
            glVertex2f(10 * dx, 9 * dy)
            glVertex2f(11 * dx, 9 * dy)
            glVertex2f(11 * dx, 8 * dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(11 * dx, 7 * dy)
            glVertex2f(11 * dx, 8 * dy)
            glVertex2f(12 * dx, 8 * dy)
            glVertex2f(12 * dx, 7 * dy)
            glEnd()
            #---piel ---#
            #---manos---#
            glColor3f(r,g,b)
            glBegin(GL_QUADS)
            glVertex2f(2*dx,6*dy)
            glVertex2f(2*dx,7*dy)
            glVertex2f(3*dx,7*dy)
            glVertex2f(3*dx,6*dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(11 * dx, 6 * dy)
            glVertex2f(11 * dx, 7 * dy)
            glVertex2f(12 * dx, 7 * dy)
            glVertex2f(12 * dx, 6 * dy)
            glEnd()
            #---cara---#
            #-boca-#
            glBegin(GL_QUADS)
            glVertex2f(5*dx,8*dy)
            glVertex2f(5*dx,9*dy)
            glVertex2f(9*dx,9*dy)
            glVertex2f(9*dx,8*dy)
            glEnd()
            #-nariz-#
            glBegin(GL_QUADS)
            glVertex2f(6*dx,9*dy)
            glVertex2f(6*dx,11*dy)
            glVertex2f(8*dx,11*dy)
            glVertex2f(8*dx,9*dy)
            glEnd()
            #-frente-#
            glBegin(GL_QUADS)
            glVertex2f(4*dx,11*dy)
            glVertex2f(4*dx,14*dy)
            glVertex2f(10*dx,14*dy)
            glVertex2f(10*dx,11*dy)
            glEnd()
            #-costados de los ojos-#
            glBegin(GL_QUADS)
            glVertex2f(4*dx,9*dy)
            glVertex2f(4*dx,11*dy)
            glVertex2f(5*dx,11*dy)
            glVertex2f(5*dx,9*dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(9 * dx, 9 * dy)
            glVertex2f(9 * dx, 11 * dy)
            glVertex2f(10 * dx, 11 * dy)
            glVertex2f(10 * dx, 9 * dy)
            glEnd()
            #-orejas-#
            glBegin(GL_QUADS)
            glVertex2f(3*dx,11*dy)
            glVertex2f(3*dx,12*dy)
            glVertex2f(4*dx,12*dy)
            glVertex2f(4*dx,11*dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(10 * dx, 11 * dy)
            glVertex2f(10 * dx, 12 * dy)
            glVertex2f(11 * dx, 12 * dy)
            glVertex2f(11 * dx, 11 * dy)
            glEnd()
        ######################
        ###Flanders###########
        ######################
        if self._tipo==2:
            dx=53.0/16
            dy=46.0/20
            #####################
            ####contorno negro####
            ######################
            glColor3f(0.0,0.0,0.0)
            #torso
            glBegin(GL_POLYGON)
            glVertex2f(8*dx,8*dy)
            glVertex2f(8*dx,19*dy)
            glVertex2f(11*dx,19*dy)
            glVertex2f(11*dx,18*dy)
            glVertex2f(12*dx,18*dy)
            glVertex2f(12*dx,16*dy)
            glVertex2f(13*dx,16*dy)
            glVertex2f(13*dx,12*dy)
            glVertex2f(14*dx,12*dy)
            glVertex2f(14*dx,11*dy)
            glVertex2f(15*dx,11*dy)
            glVertex2f(15*dx,8*dy)
            glEnd()
            glBegin(GL_POLYGON)
            glVertex2f(8 * dx, 8 * dy)
            glVertex2f(8 * dx, 19 * dy)
            glVertex2f(5* dx, 19 * dy)
            glVertex2f(5 * dx, 18 * dy)
            glVertex2f(4 * dx, 18 * dy)
            glVertex2f(4 * dx, 16 * dy)
            glVertex2f(3 * dx, 16 * dy)
            glVertex2f(3 * dx, 12 * dy)
            glVertex2f(2 * dx, 12 * dy)
            glVertex2f(2 * dx, 11 * dy)
            glVertex2f(dx, 11 * dy)
            glVertex2f(dx, 8 * dy)
            glEnd()
            #---piernas---
            glBegin(GL_QUADS)
            glVertex2f(8*dx,8*dy)
            glVertex2f(12*dx,8*dy)
            glVertex2f(12*dx,2*dy)
            glVertex2f(8*dx,2*dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(8 * dx, 8 * dy)
            glVertex2f(4 * dx, 8 * dy)
            glVertex2f(4 * dx, 2 * dy)
            glVertex2f(8 * dx, 2 * dy)
            glEnd()
            #los que faltan (detalles)
            glBegin(GL_QUADS)
            glVertex2f(5*dx,dy)
            glVertex2f(5*dx,2*dy)
            glVertex2f(7*dx,2*dy)
            glVertex2f(7*dx,dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(9 * dx, dy)
            glVertex2f(9 * dx, 2 * dy)
            glVertex2f(11 * dx, 2 * dy)
            glVertex2f(11 * dx, dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(2*dx,7*dy)
            glVertex2f(2*dx,8*dy)
            glVertex2f(4*dx,8*dy)
            glVertex2f(4*dx,7*dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(12 * dx, 7 * dy)
            glVertex2f(12 * dx, 8 * dy)
            glVertex2f(14 * dx, 8 * dy)
            glVertex2f(14 * dx, 7 * dy)
            glEnd()
            glColor3f(138.0/255,138.0/255,138.0/255)
            glBegin(GL_QUADS)
            glVertex2f(3*dx,13*dy)
            glVertex2f(3*dx,14*dy)
            glVertex2f(4*dx,14*dy)
            glVertex2f(4*dx,13*dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(12 * dx, 13 * dy)
            glVertex2f(12 * dx, 14 * dy)
            glVertex2f(13 * dx, 14 * dy)
            glVertex2f(13 * dx, 13 * dy)
            glEnd()






            #--------------------
            ####figura####
            #zapatos
            glColor3f(0.2,0.2,0.2)
            glBegin(GL_QUADS)
            glVertex2f(5*dx,2*dy)
            glVertex2f(5*dx,3*dy)
            glVertex2f(7*dx,3*dy)
            glVertex2f(7*dx,2*dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(9*dx,2*dy)
            glVertex2f(9*dx,3*dy)
            glVertex2f(11*dx,3*dy)
            glVertex2f(11*dx,2*dy)
            glEnd()
            #pantalones
            glColor3f(113.0/255,118.0/255,124.0/255)
            glBegin(GL_QUADS)
            glVertex2f(5*dx,3*dy)
            glVertex2f(5*dx,6*dy)
            glVertex2f(7*dx,6*dy)
            glVertex2f(7*dx,3*dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(9 * dx, 3 * dy)
            glVertex2f(9 * dx, 6 * dy)
            glVertex2f(11 * dx, 6 * dy)
            glVertex2f(11 * dx, 3 * dy)
            glEnd()
            ###sueter###
            glColor3f(0.0,119.0/255,4.0/255)
            glBegin(GL_QUADS)
            glVertex2f(5 * dx, 6 * dy)
            glVertex2f(5 * dx, 10 * dy)
            glVertex2f(11* dx, 10 * dy)
            glVertex2f(11 * dx, 6 * dy)
            glEnd()
            #---hombro derecho---
            glBegin(GL_QUADS)
            glVertex2f(2*dx,10*dy)
            glVertex2f(2*dx,11*dy)
            glVertex2f(3*dx,11*dy)
            glVertex2f(3*dx,10*dy)
            glEnd()
            glBegin(GL_POLYGON)
            glVertex2f(3*dx,10*dy)
            glVertex2f(3*dx,12*dy)
            glVertex2f(5*dx,12*dy)
            glVertex2f(5*dx,11*dy)
            glVertex2f(6*dx,11*dy)
            glVertex2f(6*dx,10*dy)
            glEnd()
            #---izquierdo---
            glBegin(GL_QUADS)
            glVertex2f(10 * dx, 10 * dy)
            glVertex2f(10 * dx, 11 * dy)
            glVertex2f(11 * dx, 11 * dy)
            glVertex2f(11 * dx, 10 * dy)
            glEnd()
            glBegin(GL_POLYGON)
            glVertex2f(11 * dx, 10 * dy)
            glVertex2f(11 * dx, 12 * dy)
            glVertex2f(13 * dx, 12 * dy)
            glVertex2f(13 * dx, 11 * dy)
            glVertex2f(14 * dx, 11 * dy)
            glVertex2f(14 * dx, 10 * dy)
            glEnd()
            #---Manos dentro del sueter---
            glBegin(GL_QUADS)
            glVertex2f(2*dx,9*dy)
            glVertex2f(2*dx,10*dy)
            glVertex2f(4*dx,10*dy)
            glVertex2f(4*dx,9*dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(12 * dx, 9 * dy)
            glVertex2f(12 * dx, 10 * dy)
            glVertex2f(14 * dx, 10 * dy)
            glVertex2f(14 * dx, 9 * dy)
            glEnd()
            # cosita del chaleco
            glColor3f(242.0 / 255, 99.0 / 255, 180.0 / 255)
            glBegin(GL_QUADS)
            glVertex2f(7 * dx, 9 * dy)
            glVertex2f(7 * dx, 10 * dy)
            glVertex2f(9 * dx, 10 * dy)
            glVertex2f(9 * dx, 9 * dy)
            glEnd()
            #piel
            glColor3f(r,g,b)
            #---Manos---
            glBegin(GL_QUADS)
            glVertex2f(2*dx,8*dy)
            glVertex2f(2*dx,9*dy)
            glVertex2f(4*dx,9*dy)
            glVertex2f(4*dx,8*dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(12 * dx, 8 * dy)
            glVertex2f(12 * dx, 9 * dy)
            glVertex2f(14 * dx, 9 * dy)
            glVertex2f(14 * dx, 8 * dy)
            glEnd()
            #---boca---
            glBegin(GL_QUADS)
            glVertex2f(6*dx,11*dy)
            glVertex2f(6*dx,13*dy)
            glVertex2f(10*dx,13*dy)
            glVertex2f(10*dx,11*dy)
            glEnd()
            #---frente---
            glBegin(GL_QUADS)
            glVertex2f(4*dx,14*dy)
            glVertex2f(4*dx,16*dy)
            glVertex2f(12*dx,16*dy)
            glVertex2f(12*dx,14*dy)
            glEnd()
            #anteojo
            glColor3f(1.0,1.0,1.0)
            glBegin(GL_QUADS)
            glVertex2f(5*dx,12*dy)
            glVertex2f(5*dx,14*dy)
            glVertex2f(7*dx,14*dy)
            glVertex2f(7*dx,12*dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(9 * dx, 12 * dy)
            glVertex2f(9 * dx, 14 * dy)
            glVertex2f(11 * dx, 14 * dy)
            glVertex2f(11 * dx, 12 * dy)
            glEnd()
            #--pelos--
            glColor3f(97.0/255,55.0/255,0.0)
            #bigote
            glBegin(GL_QUADS)
            glVertex2f(7*dx,11*dy)
            glVertex2f(7*dx,12*dy)
            glVertex2f(9*dx,12*dy)
            glVertex2f(9*dx,11*dy)
            glEnd()
            #Pelo
            glBegin(GL_QUADS)
            glVertex2f(5*dx,16*dy)
            glVertex2f(5*dx,18*dy)
            glVertex2f(11*dx,18*dy)
            glVertex2f(11*dx,16*dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(4*dx,15*dy)
            glVertex2f(4*dx,16*dy)
            glVertex2f(5*dx,16*dy)
            glVertex2f(5*dx,15*dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(11 * dx, 15 * dy)
            glVertex2f(11 * dx, 16 * dy)
            glVertex2f(12 * dx, 16 * dy)
            glVertex2f(12 * dx, 15 * dy)
            glEnd()


    def updatecenter(self):
        """
        Actualiza el centro del enemigo al moverse
        :return: None
        """
        self.centro=Vector(self.pos.x+53.0/2,self.pos.y+46.0/2)
    def moverx(self,direccion: int):
        """
        Mueve el enemigo en cierta direccion, 1 para la derecha y -1 a la izquierda
        :param direccion: int
        :return: None
        """
        self.pos=sumar(self.pos,Vector(direccion*53.0,0.0))
        self.updatecenter()
    def movery(self,direccion: int):
        """
        Mueve el enemigo en cierta direccion en el eje y, 1 para arriba y -1 para abajo
        :param direccion: int
        :return: None
        """
        self.pos=sumar(self.pos,Vector(0.0,direccion*46.0))
        self.updatecenter()
    def getcenter(self):
        """
        Da el centro como una tupla (x,y)
        :return: tuple
        """
        return self.centro.cartesianas()
    def setlife(self,v):
        """
        Recibe un nuevo estado de vida para el enemigo
        :param v:boolean
        :return:None
        """
        self.vivo=v
    def getlife(self):
        """
        True si el enemigo esta vivo
        :return: boolean
        """
        return self.vivo

