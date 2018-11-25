from CC3501Utils import *

class Pared(Figura):
    def __init__(self,pos,rgb=(208.0/255,77.0/255,29.0/255)):
        self.centro=Vector(pos.x+(53.0/2),pos.y+(46.0/2))
        super().__init__(pos,rgb)
    def figura(self):

        glColor3f(0.0,0.0,0.0)
        glBegin(GL_QUADS)
        glVertex2f(0.0,0.0)
        glVertex2f(0.0,46.0)
        glVertex2f(53.0,46.0)
        glVertex2f(53.0,0.0)
        glEnd()
        (r,g,b)=self.color
        glColor3f(r,g,b)
        ###############
        #primer patron#
        ###############
        dx=10.6
        dy=11.5
        yini=1.0
        for i in range(4):
            xini=0.0
            glBegin(GL_QUADS)
            glVertex2f(xini,yini)
            glVertex2f(xini,yini+dy/2-1)
            glVertex2f(xini+2*dx,yini+dy/2-1)
            glVertex2f(xini+2*dx,yini)
            glEnd()
            xini+=2*dx+1
            glBegin(GL_QUADS)
            glVertex2f(xini,yini)
            glVertex2f(xini,yini+dy/2-1)
            glVertex2f(xini+3*dx/2,yini+dy/2-1)
            glVertex2f(xini+3*dx/2,yini)
            glEnd()
            xini+=3*dx/2+1
            glBegin(GL_QUADS)
            glVertex2f(xini,yini)
            glVertex2f(xini,yini+dy/2-1)
            glVertex2f(52.0,yini+dy/2-1)
            glVertex2f(52.0,yini)
            glEnd()
            yini+=dy
        ################
        #segundo patron#
        ################
        yini = 1.0 + dy/2
        for i in range(4):
            xini=0.0
            glBegin(GL_QUADS)
            glVertex2f(xini, yini)
            glVertex2f(xini, yini + dy / 2 - 1)
            glVertex2f(xini + dx, yini + dy / 2 - 1)
            glVertex2f(xini + dx, yini)
            glEnd()
            xini +=dx + 1
            glBegin(GL_QUADS)
            glVertex2f(xini, yini)
            glVertex2f(xini, yini + dy / 2 - 1)
            glVertex2f(xini + 3 * dx / 2, yini + dy / 2 - 1)
            glVertex2f(xini + 3 * dx / 2, yini)
            glEnd()
            xini += 3 * dx / 2 + 1
            glBegin(GL_QUADS)
            glVertex2f(xini, yini)
            glVertex2f(xini, yini + dy / 2 - 1)
            glVertex2f(53.0, yini + dy / 2 - 1)
            glVertex2f(53.0, yini)
            glEnd()
            yini+=dy
    def getpos(self):
        return self.pos.cartesianas()
    def getcenter(self):
        return self.centro.cartesianas()