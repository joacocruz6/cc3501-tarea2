from CC3501Utils import *
import math as m
class Win(Figura):

    def __init__(self,pos,rgb=(232.0/255,174.0/255,14.0/255)):
        self.centro=Vector(pos.x+53.0/2,pos.y+46.0/2)
        super().__init__(pos,rgb)
    def figura(self):
        """
        Dibuja la figura de la clase
        :return: None
        """

        dx=53.0/11
        dy=46.0/13
        (r,g,b)=self.color
        ############
        ###Espuma###
        ############
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_POLYGON)
        glVertex2f(2 * dx, 9 * dy)
        glVertex2f(2 * dx, 10 * dy)
        glVertex2f(dx, 10 * dy)
        glVertex2f(dx, 12 * dy)
        glVertex2f(8 * dx, 12 * dy)
        glVertex2f(8 * dx, 10 * dy)
        glVertex2f(7 * dx, 10 * dy)
        glVertex2f(7 * dx, 9 * dy)
        glEnd()
        #vaso del schop
        glColor3f(149.0/255,206.0/255,239.0/255)
        glBegin(GL_QUADS)
        glVertex2f(dx,dy)
        glVertex2f(dx,10*dy)
        glVertex2f(2*dx,10*dy)
        glVertex2f(2*dx,dy)
        glEnd()
        glBegin(GL_QUADS)
        glVertex2f(2*dx,dy)
        glVertex2f(2*dx,2*dy)
        glVertex2f(7*dx,2*dy)
        glVertex2f(7*dx,dy)
        glEnd()
        glBegin(GL_QUADS)
        glVertex2f(7*dx,dy)
        glVertex2f(7*dx,10*dy)
        glVertex2f(8*dx,10*dy)
        glVertex2f(8*dx,dy)
        glEnd()
        #mango del schop
        glBegin(GL_QUADS)
        glVertex2f(8*dx,8*dy)
        glVertex2f(8*dx,9*dy)
        glVertex2f(10*dx,9*dy)
        glVertex2f(10*dx,8*dy)
        glEnd()
        glBegin(GL_QUADS)
        glVertex2f(8*dx,3*dy)
        glVertex2f(8*dx,4*dy)
        glVertex2f(10*dx,4*dy)
        glVertex2f(10*dx,3*dy)
        glEnd()
        glBegin(GL_QUADS)
        glVertex2f(9*dx,4*dy)
        glVertex2f(9*dx,8*dy)
        glVertex2f(10*dx,8*dy)
        glVertex2f(10*dx,4*dy)
        glEnd()
        #bajo del schop
        glColor3f(116.0/255,186.0/255,226.0/255)
        glBegin(GL_QUADS)
        glVertex2f(2*dx,2*dy)
        glVertex2f(2*dx,3*dy)
        glVertex2f(7*dx,3*dy)
        glVertex2f(7*dx,2*dy)
        glEnd()

        #############
        ###cerveza###
        #############
        glColor3f(r,g,b)
        glBegin(GL_QUADS)
        glVertex2f(2*dx,3*dy)
        glVertex2f(2*dx,9*dy)
        glVertex2f(7*dx,9*dy)
        glVertex2f(7*dx,3*dy)
        glEnd()
    def getcenter(self):
        return self.centro.cartesianas()