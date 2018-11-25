from CC3501Utils import *
import math as m
import random as rand
class Power(Figura):
    def __init__(self,pos: Vector,tipo: str):
        self.vivo=True
        self._tomado=False
        self.t0=0
        self.tipo=tipo
        self.index=-1
        self.duracion=0
        self.coloracion_camisa=(1.0,1.0,1.0)
        if tipo=="rango":
            rgb=(242.0/255,199.0/255,30.0/255)
            self.index=0
            self.duracion= 15000.0
            self.coloracion_camisa=(239.0/255,113.0/255,3.0/255)
        if tipo=="pared":
            rgb=(240.0/255,113.0/255,16.0/255)
            self.index=1
            self.duracion = 10000.0
            self.coloracion_camisa=(208.0/255,77.0/255,29.0/255)
        if tipo=="bomba":
            rgb=(16.0/255,83.0/255,240.0/255)
            self.index=2
            self.duracion=10000.0
            self.coloracion_camisa=(0.0,0.5,1.0)
        if tipo=="inmortal":
            rgb=(236.0/255,126.0/255,185.0/255)
            self.index=3
            self.duracion=5000.0
            self.coloracion_camisa=(239.0/255,168.0/255,3.0/255)
        if tipo=="cadena":
            rgb=(1.0,1.0,1.0)
            self.duracion=15000.0
            self.coloracion_camisa=(0.0,0.0,0.0)
            self.index=4
        self.centro=Vector(pos.x+(53.0/2),pos.y+(46.0/2))
        super().__init__(pos,rgb)
    def getcenter(self):
        """
        Da el centro en cartesianas
        :return: tuple
        """
        return self.centro.cartesianas()
    def figura(self):
        """
        Dibuja si el power up no a sido tomado
        :return:
        """
        if not self._tomado:
            (r,g,b)=self.color
            glColor3f(0.0,0.0,0.0)
            dx=53.0/22
            dy=46.0/19
            cx=12*dx
            cy=11*dy
            rx=9*dx
            ry=7*dy
            alpha=0.0
            i=0.1
            #primer cuarto
            glBegin(GL_TRIANGLE_FAN)
            glVertex2f(cx,cy)
            while alpha<=(m.pi/2)+0.2:
                glVertex2f(cx+rx*m.cos(alpha),cy+ry*m.sin(alpha))
                alpha+=i
            glEnd()
            #segundo cuarto:
            rx=11*dx
            alpha=m.pi/2
            glBegin(GL_TRIANGLE_FAN)
            glVertex2f(cx,cy)
            while alpha <= m.pi+0.2:
                glVertex2f(cx + rx * m.cos(alpha), cy + ry * m.sin(alpha))
                alpha += i
            glEnd()
            #tercer cuarto:
            ry=9*dy
            alpha=m.pi
            glBegin(GL_TRIANGLE_FAN)
            glVertex2f(cx,cy)
            while alpha <= (3*m.pi / 2)+0.2:
                glVertex2f(cx + rx * m.cos(alpha), cy + ry * m.sin(alpha))
                alpha += i
            glEnd()
            #cuarto parte:
            alpha=3*m.pi/2
            rx=9*dx
            glBegin(GL_TRIANGLE_FAN)
            glVertex2f(cx,cy)
            while alpha <= (2*m.pi)+0.2:
                glVertex2f(cx + rx * m.cos(alpha), cy + ry * m.sin(alpha))
                alpha += i
            glEnd()
            #############
            ###Pastel####
            #############
            #primera parte
            glColor3f(230.0/255,182.0/255,84.0/255)
            angle=m.pi
            rx=10*dx
            ry = 8* dy
            alpha = m.pi
            glBegin(GL_TRIANGLE_FAN)
            glVertex2f(cx, cy)
            while alpha <= (3 * m.pi / 2) + 0.2:
                glVertex2f(cx + rx * m.cos(alpha), cy + ry * m.sin(alpha))
                alpha += i
            glEnd()
            # segunda parte:
            alpha = 3 * m.pi / 2
            rx = 8 * dx
            glBegin(GL_TRIANGLE_FAN)
            glVertex2f(cx, cy)
            while alpha <= (2 * m.pi) + 0.2:
                glVertex2f(cx + rx * m.cos(alpha), cy + ry * m.sin(alpha))
                alpha += i
            glEnd()
            ##############
            ###Frosting###
            ##############
            glColor3f(r,g,b)
            alpha=0.0
            rx=8*dx
            ry=6*dy
            # primer cuarto
            glBegin(GL_TRIANGLE_FAN)
            glVertex2f(cx, cy)
            while alpha <= (m.pi / 2) + 0.2:
                glVertex2f(cx + rx * m.cos(alpha), cy + ry * m.sin(alpha))
                alpha += i
            glEnd()
            rx=10*dx
            # segundo cuarto:
            alpha = m.pi / 2
            glBegin(GL_TRIANGLE_FAN)
            glVertex2f(cx, cy)
            while alpha <= m.pi + 0.2:
                glVertex2f(cx + rx * m.cos(alpha), cy + ry * m.sin(alpha))
                alpha += i
            glEnd()
            # tercer cuarto:
            ry = 4 * dy
            alpha = m.pi
            glBegin(GL_TRIANGLE_FAN)
            glVertex2f(cx, cy)
            while alpha <= (3 * m.pi / 2) + 0.2:
                glVertex2f(cx + rx * m.cos(alpha), cy + ry * m.sin(alpha))
                alpha += i
            glEnd()
            # cuarto parte:
            alpha = 3 * m.pi / 2
            rx = 8 * dx
            glBegin(GL_TRIANGLE_FAN)
            glVertex2f(cx, cy)
            while alpha <= (2 * m.pi) + 0.2:
                glVertex2f(cx + rx * m.cos(alpha), cy + ry * m.sin(alpha))
                alpha += i
            glEnd()
            #######################
            ###centro de la dona###
            #######################
            # negros
            glColor3f(0.0, 0.0, 0.0)
            alpha=m.pi
            rx= 4*dx-2.0
            ry = 2*dy-1.3
            glBegin(GL_TRIANGLE_FAN)
            glVertex2f(cx, cy)
            while alpha <= (2 * m.pi) + 0.2:
                glVertex2f(cx + rx * m.cos(alpha), cy + ry * m.sin(alpha))
                alpha += i
            glEnd()
            #pastel
            glColor3f(230.0 / 255, 182.0 / 255, 84.0 / 255)
            alpha=0.0
            rx=3*dx
            ry=2*dy
            glBegin(GL_TRIANGLE_FAN)
            glVertex2f(cx, cy)
            while alpha <= (m.pi) + 0.2:
                glVertex2f(cx + rx * m.cos(alpha), cy + ry * m.sin(alpha))
                alpha += i
            glEnd()
            ry=dy
            glBegin(GL_TRIANGLE_FAN)
            glVertex2f(cx, cy)
            while alpha <= (2 * m.pi) + 0.2:
                glVertex2f(cx + rx * m.cos(alpha), cy + ry * m.sin(alpha))
                alpha += i
            glEnd()
            ################
            ###decoracion###
            ################
            #naranjas
            glColor3f(1.0,128/255.0,0.0)
            glBegin(GL_QUADS)
            glVertex2f(5*dx,14*dy)
            glVertex2f(5*dx,15*dy)
            glVertex2f(6*dx,15*dy)
            glVertex2f(6*dx,14*dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(9*dx,7*dy)
            glVertex2f(9*dx,8*dy)
            glVertex2f(10*dx,8*dy)
            glVertex2f(10*dx,7*dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(15*dx,9*dy)
            glVertex2f(15*dx,10*dy)
            glVertex2f(16*dx,10*dy)
            glVertex2f(16*dx,9*dy)
            glEnd()
            #rosadas
            glColor3f(242.0/255,99.0/255,180.0/255)
            glBegin(GL_QUADS)
            glVertex2f(8*dx,15*dy)
            glVertex2f(8*dx,16*dy)
            glVertex2f(9*dx,16*dy)
            glVertex2f(9*dx,15*dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(16*dx,11*dy)
            glVertex2f(16*dx,12*dy)
            glVertex2f(17*dx,12*dy)
            glVertex2f(17*dx,11*dy)
            glEnd()
            #verde
            glColor3f(104.0/255,246.0/255,33.0/255)
            glBegin(GL_QUADS)
            glVertex2f(13*dx,14*dy)
            glVertex2f(13*dx,15*dy)
            glVertex2f(14*dx,15*dy)
            glVertex2f(14*dx,14*dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(6*dx,10*dy)
            glVertex2f(6*dx,11*dy)
            glVertex2f(7*dx,11*dy)
            glVertex2f(7*dx,10*dy)
            glEnd()
            #azules
            glColor3f(23.0/255,104.0/255,226.0/255)
            glBegin(GL_QUADS)
            glVertex2f(6*dx,12*dy)
            glVertex2f(6*dx,13*dy)
            glVertex2f(7*dx,13*dy)
            glVertex2f(7*dx,12*dy)
            glEnd()
            glBegin(GL_QUADS)
            glVertex2f(16*dx,13*dy)
            glVertex2f(16*dx,14*dy)
            glVertex2f(17*dx,14*dy)
            glVertex2f(17*dx,13*dy)
            glEnd()
    def gettomado(self):
        """
        Retorna True si el power up a sido tomado
        :return: boolean
        """
        return self._tomado
    def tomar(self,t_a):
        """
        Hace el efecto que el powe up este tomado.
        :param t_a: num
        :return: None
        """
        self._tomado=True
        self.t0=t_a
        self.centro=Vector(-100000000.0,-10000000.0)
    def setlife(self,v):
        """
        Pone el estado de vida como el booleano v
        :param v: boolean
        :return: None
        """
        self.vivo=v
    def getlife(self):
        """
        True si el power up esta vivo
        :return: boolean
        """
        return self.vivo
    def gettime(self):
        """
        Entrega el tiempo en el cual el power up es recogido
        :return: num
        """
        return self.t0
    def getduracion(self):
        """
        Retorna cuanto debe durar el efecto del powerup en el jugador
        :return:
        """
        return self.duracion
    def gettipo(self):
        """
        Da el str de tipo
        :return: str
        """
        return self.tipo
    def getindex(self):
        """
        Da el indice que le corresponde en los activos
        :return:
        """
        return self.index
    def getcoloracion(self):
        """
        Da la coloracion como tupla (r,g,b) de la camisa o vestido del jugador
        :return: tuple
        """
        return self.coloracion_camisa

    def plustime(self,dt):
        """
        Da mas tiempo a la duracion
        :param dt: num
        :return: None
        """
        if self._tomado:
            self.t0+=dt

    def gettomado(self):
        """
        Da true si power esta tomado
        :return: boolean
        """
        return self._tomado