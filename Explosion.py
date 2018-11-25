from CC3501Utils import *
class Explosion(Figura):
    def __init__(self,t,pos,rgb=(229.0/255,202.0/255,28.0/255)):
        self.vida=True
        self.t=t
        self.centro=Vector(pos.x+53.0/2,pos.y+46.0/2)
        super().__init__(pos,rgb)
    def figura(self):
        """
        Dibuja las primitivas de la explosion
        :return: None
        """

        dx=10.6
        dy=11.5
        ###################
        #primero a dibujar#
        ###################
        glBegin(GL_POLYGON)
        glVertex2f(1.0,2*dy)
        glVertex2f(dx,5*dy/2)
        glVertex2f(1.0,45.0)
        glVertex2f(3*dx/2,3*dy)
        glVertex2f(5*dx/2,45.0)
        glVertex2f(7*dx/2,3*dy)
        glVertex2f(52.0,45.0)
        glVertex2f(4*dx,5*dy/2)
        glVertex2f(52.0,2*dy)
        glVertex2f(4*dx,3*dy/2)
        glVertex2f(52.0,1.0)
        glVertex2f(7*dx/2,dy)
        glVertex2f(5*dx/2,1.0)
        glVertex2f(3*dx/2,dy)
        glVertex2f(1.0,1.0)
        glVertex2f(dx,3*dy/2)
        glEnd()
        glColor3f(138.0/255,138.0/255,138.0/255)
        glBegin(GL_TRIANGLES)
        glVertex2f(1.0,1.0)
        glVertex2f(1.0,2*dy)
        glVertex2f(2*dx/3,3*dy/2)
        glEnd()
        glBegin(GL_TRIANGLES)
        glVertex2f(1.0,2*dy)
        glVertex2f(2*dx/3,5*dy/2)
        glVertex2f(1.0,45.0)
        glEnd()
        ###################
        #segundo a dibujar#
        ###################
        glColor3f(249.0/255,135.0/255,21.0/255)
        glBegin(GL_TRIANGLES)
        glVertex2f(3*dx/2,2*dy)
        glVertex2f(3*dx/2,3*dy)
        glVertex2f(3*dx/2+dx,3*dy)
        glEnd()
        glBegin(GL_TRIANGLES)
        glVertex2f(3*dx/2+dx,3*dy)
        glVertex2f(7*dx/2,3*dy)
        glVertex2f(7*dx/2,2*dy)
        glEnd()
        glBegin(GL_TRIANGLES)
        glVertex2f(7*dx/2,2*dy)
        glVertex2f(7*dx/2,dy)
        glVertex2f(5*dx/2,dy)
        glEnd()
        glBegin(GL_TRIANGLES)
        glVertex2f(5*dx/2,dy)
        glVertex2f(3*dx/2,dy)
        glVertex2f(3*dx/2,2*dy)
        glEnd()
        #segundos triangulos naranjos
        glBegin(GL_TRIANGLES)
        glVertex2f(3*dx/2,5*dy/2)
        glVertex2f(3*dx/2,3*dy/2)
        glVertex2f(dx,2*dy)
        glEnd()
        glBegin(GL_TRIANGLES)
        glVertex2f(2*dx,3*dy)
        glVertex2f(5*dx/2,7*dy/2)
        glVertex2f(3*dx,3*dy)
        glEnd()
        glBegin(GL_TRIANGLES)
        glVertex2f(7*dx/2,5*dy/2)
        glVertex2f(4*dx,2*dy)
        glVertex2f(7*dx/2,3*dy/2)
        glEnd()
        glBegin(GL_TRIANGLES)
        glVertex2f(3*dx,dy)
        glVertex2f(5*dx/2,dy/2)
        glVertex2f(2*dx,dy)
        glEnd()
        ##################
        #ultimo a dibujar#
        ##################
        xini=3*dx/2
        yini=2*dy
        glColor3f(0.8,0.0,0.0)
        glBegin(GL_QUADS)
        glVertex2f(xini,yini)
        glVertex2f(xini+dx,yini+dy)
        glVertex2f(xini+2*dx,yini)
        glVertex2f(xini+dx,yini-dy)
        glEnd()
    def getcenter(self):
        """
        Da el centro de la figura como tupla
        :return: tuple
        """
        return self.centro.cartesianas()
    def getlife(self):
        """
        Da el estado de vida de la explosion
        :return: None
        """
        return self.vida
    def gettime(self):
        """
        Da el tiempo en que la explosion fue creada
        :return:
        """
        return self.t
    def setlife(self,life):
        """
        Recibe un nuevo estado de vida para el objeto
        :param life: boolean
        :return: None
        """
        self.vida=life
    def getpos(self):
        """
        Da la posicion en cartesianas
        :return: tuple
        """
        return self.pos.cartesianas()
