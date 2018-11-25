from CC3501Utils import *
import math as m
class Player(Figura):
    #inicializador
    def __init__(self,pos: Vector,rgb=(1.0,1.0,51.0/255),vida=True,numero=1):
        self.vida=vida#true si esta vivo
        self.centro=Vector(pos.x+(53.0/2),pos.y+(46.0/2))
        self.numero=numero
        if self.numero==1:
            self.color_camisa=(1.0,1.0,1.0)
        if self.numero==2:
            self.color_camisa=(43.0/255,185/255,0.0)
        super().__init__(pos,rgb)
    def figura(self):
        """
        Dibuja al modelo en pantalla
        :return: None
        """

        (r,g,b)=self.color
        (cr,cg,cb)=self.color_camisa
        #discretizacion
        #################
        ###Homero (P1)###
        #################
        if self.numero==1:
            dx = 53.0 / 16
            dy = 46.0 / 20
            ######################
            ####contorno negro####
            ######################
            glColor3f(0.0, 0.0, 0.0)
            # torso
            glBegin(GL_POLYGON)
            glVertex2f(8 * dx, 8 * dy)
            glVertex2f(8 * dx, 19 * dy)
            glVertex2f(11 * dx, 19 * dy)
            glVertex2f(11 * dx, 18 * dy)
            glVertex2f(12 * dx, 18 * dy)
            glVertex2f(12 * dx, 16 * dy)
            glVertex2f(13 * dx, 16 * dy)
            glVertex2f(13 * dx, 12 * dy)
            glVertex2f(14 * dx, 12 * dy)
            glVertex2f(14 * dx, 11 * dy)
            glVertex2f(15 * dx, 11 * dy)
            glVertex2f(15 * dx, 8 * dy)
            glEnd()
            glBegin(GL_POLYGON)
            glVertex2f(8 * dx, 8 * dy)
            glVertex2f(8 * dx, 19 * dy)
            glVertex2f(5 * dx, 19 * dy)
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
            # ---piernas---
            glBegin(GL_QUADS)
            glVertex2f(8 * dx, 8 * dy)
            glVertex2f(12 * dx, 8 * dy)
            glVertex2f(12 * dx, 2 * dy)
            glVertex2f(8 * dx, 2 * dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(8 * dx, 8 * dy)
            glVertex2f(4 * dx, 8 * dy)
            glVertex2f(4 * dx, 2 * dy)
            glVertex2f(8 * dx, 2 * dy)
            glEnd()
            # los que faltan (detalles)
            glBegin(GL_QUADS)
            glVertex2f(5 * dx, dy)
            glVertex2f(5 * dx, 2 * dy)
            glVertex2f(7 * dx, 2 * dy)
            glVertex2f(7 * dx, dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(9 * dx, dy)
            glVertex2f(9 * dx, 2 * dy)
            glVertex2f(11 * dx, 2 * dy)
            glVertex2f(11 * dx, dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(2 * dx, 7 * dy)
            glVertex2f(2 * dx, 8 * dy)
            glVertex2f(4 * dx, 8 * dy)
            glVertex2f(4 * dx, 7 * dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(12 * dx, 7 * dy)
            glVertex2f(12 * dx, 8 * dy)
            glVertex2f(14 * dx, 8 * dy)
            glVertex2f(14 * dx, 7 * dy)
            glEnd()
            glColor3f(138.0 / 255, 138.0 / 255, 138.0 / 255)
            glBegin(GL_QUADS)
            glVertex2f(3 * dx, 13 * dy)
            glVertex2f(3 * dx, 14 * dy)
            glVertex2f(4 * dx, 14 * dy)
            glVertex2f(4 * dx, 13 * dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(12 * dx, 13 * dy)
            glVertex2f(12 * dx, 14 * dy)
            glVertex2f(13 * dx, 14 * dy)
            glVertex2f(13 * dx, 13 * dy)
            glEnd()






            # --------------------
            ####figura####
            # zapatos
            glColor3f(0.2, 0.2, 0.2)
            glBegin(GL_QUADS)
            glVertex2f(5 * dx, 2 * dy)
            glVertex2f(5 * dx, 3 * dy)
            glVertex2f(7 * dx, 3 * dy)
            glVertex2f(7 * dx, 2 * dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(9 * dx, 2 * dy)
            glVertex2f(9 * dx, 3 * dy)
            glVertex2f(11 * dx, 3 * dy)
            glVertex2f(11 * dx, 2 * dy)
            glEnd()
            # pantalones
            glColor3f(75.0 / 255, 146.0 / 255, 226.0 / 255)
            glBegin(GL_QUADS)
            glVertex2f(5 * dx, 3 * dy)
            glVertex2f(5 * dx, 6 * dy)
            glVertex2f(7 * dx, 6 * dy)
            glVertex2f(7 * dx, 3 * dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(9 * dx, 3 * dy)
            glVertex2f(9 * dx, 6 * dy)
            glVertex2f(11 * dx, 6 * dy)
            glVertex2f(11 * dx, 3 * dy)
            glEnd()
            ###camisa###
            glColor3f(cr,cg,cb)
            glBegin(GL_QUADS)
            glVertex2f(5 * dx, 6 * dy)
            glVertex2f(5 * dx, 10 * dy)
            glVertex2f(11 * dx, 10 * dy)
            glVertex2f(11 * dx, 6 * dy)
            glEnd()
            # ---hombro derecho---
            glBegin(GL_QUADS)
            glVertex2f(2 * dx, 10 * dy)
            glVertex2f(2 * dx, 11 * dy)
            glVertex2f(3 * dx, 11 * dy)
            glVertex2f(3 * dx, 10 * dy)
            glEnd()
            glBegin(GL_POLYGON)
            glVertex2f(3 * dx, 10 * dy)
            glVertex2f(3 * dx, 12 * dy)
            glVertex2f(5 * dx, 12 * dy)
            glVertex2f(5 * dx, 11 * dy)
            glVertex2f(6 * dx, 11 * dy)
            glVertex2f(6 * dx, 10 * dy)
            glEnd()
            # ---izquierdo---
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
            # piel
            glColor3f(r, g, b)
            # ---Manos---
            glBegin(GL_QUADS)
            glVertex2f(2 * dx, 8 * dy)
            glVertex2f(2 * dx, 10 * dy)
            glVertex2f(4 * dx, 10 * dy)
            glVertex2f(4 * dx, 8 * dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(12 * dx, 8 * dy)
            glVertex2f(12 * dx, 10 * dy)
            glVertex2f(14 * dx, 10 * dy)
            glVertex2f(14 * dx, 8 * dy)
            glEnd()
            #---cabeza---
            #nariz
            glBegin(GL_QUADS)
            glVertex2f(7*dx,13*dy)
            glVertex2f(7*dx,14*dy)
            glVertex2f(9*dx,14*dy)
            glVertex2f(9*dx,13*dy)
            glEnd()
            #laterales
            glBegin(GL_QUADS)
            glVertex2f(5*dx,12*dy)
            glVertex2f(5*dx,14*dy)
            glVertex2f(6*dx,14*dy)
            glVertex2f(6*dx,12*dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(10 * dx, 12 * dy)
            glVertex2f(10 * dx, 14 * dy)
            glVertex2f(11 * dx, 14 * dy)
            glVertex2f(11 * dx, 12 * dy)
            glEnd()
            #frente
            glBegin(GL_QUADS)
            glVertex2f(5*dx,14*dy)
            glVertex2f(5*dx,18*dy)
            glVertex2f(11*dx,18*dy)
            glVertex2f(11*dx,14*dy)
            glEnd()
            #orejas
            glBegin(GL_QUADS)
            glVertex2f(4*dx,14*dy)
            glVertex2f(4*dx,15*dy)
            glVertex2f(5*dx,15*dy)
            glVertex2f(5*dx,14*dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(11 * dx, 14 * dy)
            glVertex2f(11 * dx, 15 * dy)
            glVertex2f(12 * dx, 15 * dy)
            glVertex2f(12 * dx, 14 * dy)
            glEnd()
            # ---barba---
            glColor3f(171.0/255,82.0/255,4.0/255)
            glBegin(GL_QUADS)
            glVertex2f(5*dx,11*dy)
            glVertex2f(5*dx,12*dy)
            glVertex2f(10*dx,12*dy)
            glVertex2f(10*dx,11*dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(7*dx,12*dy)
            glVertex2f(7*dx,13*dy)
            glVertex2f(9*dx,13*dy)
            glVertex2f(9*dx,12*dy)
            glEnd()

        ################
        ###Marge (P2)###
        ################
        if self.numero==2:
            dx=53.0/16
            dy=46.0/24
            ##############
            ###contorno###
            ##############
            glColor3f(0.0, 0.0, 0.0)
            # torso
            glBegin(GL_POLYGON)
            glVertex2f(8 * dx, 8 * dy)
            glVertex2f(8 * dx, 23 * dy)
            glVertex2f(11 * dx, 23 * dy)
            glVertex2f(11 * dx, 22 * dy)
            glVertex2f(12 * dx, 22 * dy)
            glVertex2f(12 * dx, 21 * dy)
            glVertex2f(13 * dx, 21 * dy)
            glVertex2f(13 * dx, 12 * dy)
            glVertex2f(14 * dx, 12 * dy)
            glVertex2f(14 * dx, 11 * dy)
            glVertex2f(15 * dx, 11 * dy)
            glVertex2f(15 * dx, 8 * dy)
            glEnd()
            glBegin(GL_POLYGON)
            glVertex2f(8 * dx, 8 * dy)
            glVertex2f(8 * dx, 23 * dy)
            glVertex2f(5 * dx, 23 * dy)
            glVertex2f(5 * dx, 22 * dy)
            glVertex2f(4 * dx, 22 * dy)
            glVertex2f(4 * dx, 21 * dy)
            glVertex2f(3 * dx, 21 * dy)
            glVertex2f(3 * dx, 12 * dy)
            glVertex2f(2 * dx, 12 * dy)
            glVertex2f(2 * dx, 11 * dy)
            glVertex2f(dx, 11 * dy)
            glVertex2f(dx, 8 * dy)
            glEnd()
            # ---piernas---
            glBegin(GL_QUADS)
            glVertex2f(8 * dx, 8 * dy)
            glVertex2f(12 * dx, 8 * dy)
            glVertex2f(12 * dx, 2 * dy)
            glVertex2f(8 * dx, 2 * dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(8 * dx, 8 * dy)
            glVertex2f(4 * dx, 8 * dy)
            glVertex2f(4 * dx, 2 * dy)
            glVertex2f(8 * dx, 2 * dy)
            glEnd()
            # los que faltan (detalles)
            glBegin(GL_QUADS)
            glVertex2f(5 * dx, dy)
            glVertex2f(5 * dx, 2 * dy)
            glVertex2f(7 * dx, 2 * dy)
            glVertex2f(7 * dx, dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(9 * dx, dy)
            glVertex2f(9 * dx, 2 * dy)
            glVertex2f(11 * dx, 2 * dy)
            glVertex2f(11 * dx, dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(2 * dx, 7 * dy)
            glVertex2f(2 * dx, 8 * dy)
            glVertex2f(4 * dx, 8 * dy)
            glVertex2f(4 * dx, 7 * dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(12 * dx, 7 * dy)
            glVertex2f(12 * dx, 8 * dy)
            glVertex2f(14 * dx, 8 * dy)
            glVertex2f(14 * dx, 7 * dy)
            glEnd()
            glColor3f(138.0 / 255, 138.0 / 255, 138.0 / 255)
            glBegin(GL_QUADS)
            glVertex2f(3 * dx, 13 * dy)
            glVertex2f(3 * dx, 14 * dy)
            glVertex2f(4 * dx, 14 * dy)
            glVertex2f(4 * dx, 13 * dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(12 * dx, 13 * dy)
            glVertex2f(12 * dx, 14 * dy)
            glVertex2f(13 * dx, 14 * dy)
            glVertex2f(13 * dx, 13 * dy)
            glEnd()




            ############
            ###figura###
            ############
            #---zapatos---#
            glColor3f(235.0/255, 0.0, 0.0)
            glBegin(GL_QUADS)
            glVertex2f(5 * dx, 2 * dy)
            glVertex2f(5 * dx, 3 * dy)
            glVertex2f(7 * dx, 3 * dy)
            glVertex2f(7 * dx, 2 * dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(9 * dx, 2 * dy)
            glVertex2f(9 * dx, 3 * dy)
            glVertex2f(11 * dx, 3 * dy)
            glVertex2f(11 * dx, 2 * dy)
            glEnd()
            #---vestido---#
            glColor3f(cr,cg,cb)
            glBegin(GL_QUADS)
            glVertex2f(5*dx,3*dy)
            glVertex2f(5*dx,10*dy)
            glVertex2f(11*dx,10*dy)
            glVertex2f(11*dx,3*dy)
            glEnd()
            # ---hombro derecho---
            # piel
            glColor3f(r, g, b)
            glBegin(GL_QUADS)
            glVertex2f(2 * dx, 10 * dy)
            glVertex2f(2 * dx, 11 * dy)
            glVertex2f(3 * dx, 11 * dy)
            glVertex2f(3 * dx, 10 * dy)
            glEnd()
            glBegin(GL_POLYGON)
            glVertex2f(3 * dx, 10 * dy)
            glVertex2f(3 * dx, 12 * dy)
            glVertex2f(5 * dx, 12 * dy)
            glVertex2f(5 * dx, 11 * dy)
            glVertex2f(6 * dx, 11 * dy)
            glVertex2f(6 * dx, 10 * dy)
            glEnd()
            # ---izquierdo---
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
            # ---Manos---
            glBegin(GL_QUADS)
            glVertex2f(2 * dx, 8 * dy)
            glVertex2f(2 * dx, 10 * dy)
            glVertex2f(4 * dx, 10 * dy)
            glVertex2f(4 * dx, 8 * dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(12 * dx, 8 * dy)
            glVertex2f(12 * dx, 10 * dy)
            glVertex2f(14 * dx, 10 * dy)
            glVertex2f(14 * dx, 8 * dy)
            glEnd()
            #---cabeza---#
            #boca
            glBegin(GL_QUADS)
            glVertex2f(6*dx,11*dy)
            glVertex2f(6*dx,12*dy)
            glVertex2f(10*dx,12*dy)
            glVertex2f(10*dx,11*dy)
            glEnd()
            # nariz
            glBegin(GL_QUADS)
            glVertex2f(7 * dx, 12 * dy)
            glVertex2f(7 * dx, 14 * dy)
            glVertex2f(9 * dx, 14 * dy)
            glVertex2f(9 * dx, 12 * dy)
            glEnd()
            # laterales
            glBegin(GL_QUADS)
            glVertex2f(5 * dx, 12 * dy)
            glVertex2f(5 * dx, 14 * dy)
            glVertex2f(6 * dx, 14 * dy)
            glVertex2f(6 * dx, 12 * dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(10 * dx, 12 * dy)
            glVertex2f(10 * dx, 14 * dy)
            glVertex2f(11 * dx, 14 * dy)
            glVertex2f(11 * dx, 12 * dy)
            glEnd()
            # frente + orejas
            glBegin(GL_QUADS)
            glVertex2f(4 * dx, 14 * dy)
            glVertex2f(4 * dx, 16 * dy)
            glVertex2f(12 * dx, 16 * dy)
            glVertex2f(12 * dx, 14 * dy)
            glEnd()
            #---pelo---#
            glColor3f(0.0,12.0/255,175.0/255)
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
            glBegin(GL_QUADS)
            glVertex2f(4*dx,16*dy)
            glVertex2f(4*dx,21*dy)
            glVertex2f(12*dx,21*dy)
            glVertex2f(12*dx,16*dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(5*dx,21*dy)
            glVertex2f(5*dx,22*dy)
            glVertex2f(11*dx,22*dy)
            glVertex2f(11*dx,21*dy)
            glEnd()
    def updatecenter(self):
        """
        Actualiza el centro del jugador al moverse
        :return: None
        """
        self.centro=Vector(self.pos.x+53.0/2,self.pos.y+46.0/2)
    #moverse: se mueve segun la discretizacion, direccion es -1 o 1 segun si le resto a sumo
    def moverx(self,direccion: int):
        self.pos=sumar(self.pos,Vector(direccion*53.0,0.0))
        self.dibujar()
        self.updatecenter()
    def movery(self,direccion:int):
        self.pos=sumar(self.pos,Vector(0.0,direccion*46.0))
        self.updatecenter()
    def getpos(self):
        """
        Da la posicion como tupla x,y
        :return: tuple
        """
        return self.pos.cartesianas()
    def getcenter(self):
        """
        Da el centro como tupla x,y
        :return: tuple
        """
        return self.centro.cartesianas()
    def getlife(self):
        """
        True si esta vivo
        :return: boolean
        """
        return self.vida
    def setlife(self,v):
        """
        Pone el valor de la vida como v
        :param v: boolean
        :return: None
        """
        self.vida=v
    def normalizar_camisa(self):
        """
        Al terminar un power up, deja el valor de la camisa como normal
        :return: None
        """
        if self.numero==1:
            self.color_camisa=(1.0,1.0,1.0)
        if self.numero==2:
            self.color_camisa=(43.0/255,185/255,0.0)
    def setcoloracion(self,rgb: tuple):
        """
        Cambia el color de la camisa
        :param rgb: tuple
        :return: None
        """
        self.color_camisa=rgb