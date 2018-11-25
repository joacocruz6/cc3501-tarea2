from CC3501Utils import *
import math as m
class Bombs(Figura):
    def __init__(self,pos: Vector,t,vivo=True,rgb=(0.0,0.0,0.0)):
        self.vivo=vivo
        self.t=t
        self.centro=Vector(pos.x+53./2,pos.y+46.0/2)
        self.cambio=False
        super().__init__(pos,rgb)

    def figura(self):
        """
        Metodo que dibuja la figura de la bomba, es llamado por dibujar de su padre
        :return: None
        """


        (r,g,b)=self.color
        dx=53.0/17
        dy=46.0/23
        ############
        ###figura###
        ############
        (cx,cy)=(9*dx,9*dy)
        alpha=0
        i=0.1
        rx=7*dx
        ry=8*dy
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(cx,cy)
        while alpha<=m.pi/2 + 0.1:
            glVertex2f(cx+rx*m.cos(alpha),cy+ry*m.sin(alpha))
            alpha+=i
        glEnd()
        alpha=m.pi/2
        rx=8*dx
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(cx, cy)
        while alpha <= m.pi +0.1:
            glVertex2f(cx + rx * m.cos(alpha), cy + ry * m.sin(alpha))
            alpha += i
        glEnd()
        alpha=m.pi
        ry=7*dy
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(cx, cy)
        while alpha <= 3*m.pi /2 + 0.1:
            glVertex2f(cx + rx * m.cos(alpha), cy + ry * m.sin(alpha))
            alpha += i
        glEnd()
        alpha=3*m.pi/2
        rx=7*dx
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(cx, cy)
        while alpha <= 2*m.pi + 0.1:
            glVertex2f(cx + rx * m.cos(alpha), cy + ry * m.sin(alpha))
            alpha += i
        glEnd()
        #lo que faltaba de negro
        glBegin(GL_QUADS)
        glVertex2f(6*dx,16*dy)
        glVertex2f(6*dx,18*dy)
        glVertex2f(12*dx,18*dy)
        glVertex2f(12*dx,16*dy)
        glEnd()
        glBegin(GL_QUADS)
        glVertex2f(7*dx,18*dy)
        glVertex2f(7*dx,19*dy)
        glVertex2f(11*dx,19*dy)
        glVertex2f(11*dx,18*dy)
        glEnd()
        #blancos
        glColor3f(1.0,1.0,1.0)
        glBegin(GL_QUADS)
        glVertex2f(10*dx,14*dy)
        glVertex2f(10*dx,15*dy)
        glVertex2f(12*dx,15*dy)
        glVertex2f(12*dx,14*dy)
        glEnd()
        glBegin(GL_QUADS)
        glVertex2f(11 * dx, 13 * dy)
        glVertex2f(11 * dx, 14 * dy)
        glVertex2f(13 * dx, 14 * dy)
        glVertex2f(13 * dx, 13 * dy)
        glEnd()
        glBegin(GL_QUADS)
        glVertex2f(12 * dx, 12 * dy)
        glVertex2f(12 * dx, 13 * dy)
        glVertex2f(13 * dx, 13 * dy)
        glVertex2f(13 * dx, 12 * dy)
        glEnd()
        glBegin(GL_QUADS)
        glVertex2f(4 * dx, 14 * dy)
        glVertex2f(4 * dx, 15 * dy)
        glVertex2f(5 * dx, 15 * dy)
        glVertex2f(5 * dx, 14 * dy)
        glEnd()
        #naranjo
        glColor3f(1.0,0.5,0.0)
        glBegin(GL_QUADS)
        glVertex2f(7*dx,17*dy)
        glVertex2f(7*dx,18*dy)
        glVertex2f(11*dx,18*dy)
        glVertex2f(11*dx,17*dy)
        glEnd()
        #cuerda
        glColor3f(r,g,b)
        glBegin(GL_QUADS)
        glVertex2f(8*dx,19*dy)
        glVertex2f(8*dx,20*dy)
        glVertex2f(9*dx,20*dy)
        glVertex2f(9*dx,19*dy)
        glEnd()
        if not self.cambio:
            glBegin(GL_QUADS)
            glVertex2f(7*dx,20*dy)
            glVertex2f(7*dx,21*dy)
            glVertex2f(8*dx,21*dy)
            glVertex2f(8*dx,20*dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(4*dx,21*dy)
            glVertex2f(4*dx,22*dy)
            glVertex2f(7*dx,22*dy)
            glVertex2f(7*dx,21*dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(3*dx,20*dy)
            glVertex2f(3*dx,21*dy)
            glVertex2f(4*dx,21*dy)
            glVertex2f(4*dx,20*dy)
            glEnd()
            #mecha
            glColor3f(1.0,128.0/255,0.0)
            glBegin(GL_QUADS)
            glVertex2f(2*dx,19*dy)
            glVertex2f(2*dx,20*dy)
            glVertex2f(3*dx,20*dy)
            glVertex2f(3*dx,19*dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(0.0, 19 * dy)
            glVertex2f(0.0, 20 * dy)
            glVertex2f(dx, 20 * dy)
            glVertex2f(dx, 19 * dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(dx, 20 * dy)
            glVertex2f(dx, 21 * dy)
            glVertex2f(2*dx, 21 * dy)
            glVertex2f(2 * dx, 20 * dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f( dx, 18 * dy)
            glVertex2f( dx, 19 * dy)
            glVertex2f(2* dx, 19 * dy)
            glVertex2f(2 * dx, 18 * dy)
            glEnd()
            glColor3f(1.0, 213.0 / 255, 0.0)
            glBegin(GL_QUADS)
            glVertex2f(dx, 19 * dy)
            glVertex2f(dx, 20 * dy)
            glVertex2f(2 * dx, 20 * dy)
            glVertex2f(2 * dx, 19 * dy)
            glEnd()
        else:
            glColor3f(1.0, 128.0 / 255, 0.0)
            glBegin(GL_QUADS)
            glVertex2f(8 * dx, 20 * dy)
            glVertex2f(8 * dx, 21 * dy)
            glVertex2f(9 * dx, 21 * dy)
            glVertex2f(9 * dx, 20 * dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(6 * dx, 20 * dy)
            glVertex2f(6 * dx, 21 * dy)
            glVertex2f(7 * dx, 21 * dy)
            glVertex2f(7 * dx, 20 * dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(7 * dx, 21 * dy)
            glVertex2f(7 * dx, 22 * dy)
            glVertex2f(8 * dx, 22 * dy)
            glVertex2f(8 * dx, 21 * dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(7 * dx, 19 * dy)
            glVertex2f(7 * dx, 20 * dy)
            glVertex2f(8 * dx, 20 * dy)
            glVertex2f(8 * dx, 19 * dy)
            glEnd()
            glColor3f(1.0,213.0/255,0.0)
            glBegin(GL_QUADS)
            glVertex2f(7 * dx, 20 * dy)
            glVertex2f(7 * dx, 21 * dy)
            glVertex2f(8 * dx, 21 * dy)
            glVertex2f(8 * dx, 20 * dy)
            glEnd()
    def setlife(self,estate):
        """
        Cambia su estado de vivo
        :param estate: boolean
        :return: None
        """
        self.vivo=estate
    def gettime(self):
        """
        Da el tiempo en el cual se creo
        :return: num
        """
        return self.t
    def getlife(self):
        """
        Retorna True si el objeto vive
        :return: boolean
        """
        return self.vivo
    def getcenter(self):
        """
        Entrega el centro como una tupla (x,y)
        :return: tuple
        """
        return self.centro.cartesianas()
    def getpos(self):
        """
        Entrega la posicion como una tupla (x,y)
        :return: tuple
        """
        return self.pos.cartesianas()
    def Cambio_change(self):
        """
        Genera el cambio en el dibujo segun el tiempo que le queda.
        :return: None
        """
        self.cambio=True
    def getcambio(self):
        """
        Retorna si el cambio en la figura fue hecho o no
        :return: boolean
        """
        return self.cambio
    def plustime(self,t):
        """
        agrega tiempo adicional a la explosion, este depende de la pausa
        :param t: num
        :return: None
        """
        self.t+=t
    def settime(self,t):
        """
        Setter para el parametro t inicial
        :param t: num
        :return:None
        """
        self.t=t