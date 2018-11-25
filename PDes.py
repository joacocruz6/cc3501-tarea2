from CC3501Utils import *
class PDes(Figura):
    def __init__(self,pos: Vector,vida= True,rgb=(102.0/255,51.0/255,0)):
        self.vida=vida
        self.centro=Vector(pos.x+53.0/2,pos.y+46.0/2)
        super().__init__(pos,rgb)
    def figura(self):
        dx=13.25
        dy=11.5

        #cuadrado negro de base
        glColor3f(0.0,0.0,0.0)
        glBegin(GL_QUADS)
        glVertex2f(0.0,0.0)
        glVertex2f(0.0,46.0)
        glVertex2f(53.0,46.0)
        glVertex2f(53.0,0.0)
        glEnd()
        # tapita de arriba
        (r,g,b)=self.color
        glColor3f(r,g,b)
        glBegin(GL_QUADS)
        glVertex2f(1.0,45.0-dy/2)
        glVertex2f(1.0,46.0)
        glVertex2f(52.0,46.0)
        glVertex2f(52.0,45.0-dy/2)
        glEnd()
        #Tapita izquierda
        glColor3f(r,g,b)
        glBegin(GL_QUADS)
        glVertex2f(1.0,dy/2+1)
        glVertex2f(1.0,44.0-dy/2)
        glVertex2f(dx/2,44.0-dy/2)
        glVertex2f(dx/2,dy/2+1)
        glEnd()
        #Tapita derecha
        glColor3f(r,g,b)
        glBegin(GL_QUADS)
        glVertex2f(53.0-dx/2,dy/2+1)
        glVertex2f(53.0-dx/2,44.0-dy/2)
        glVertex2f(52.0,44.0-dy/2)
        glVertex2f(52.0,dy/2+1)
        glEnd()
        #Tapita abajo
        glColor3f(r,g,b)
        glBegin(GL_QUADS)
        glVertex2f(1.0,1.0)
        glVertex2f(1.0,dy/2)
        glVertex2f(52.0,dy/2)
        glVertex2f(52.0,1.0)
        glEnd()
        #Planchas de al medio:
        dy2=21.0
        #de mas abajo
        xini=dx/2+1
        yini=dy/2+1
        xfin=52.0-dx/2
        glColor3f(r,g,b)
        glBegin(GL_QUADS)
        glVertex2f(xini,yini)
        glVertex2f(xini,yini+dy2/3)
        glVertex2f(xfin,yini+dy2/3)
        glVertex2f(xfin,yini)
        glEnd()
        #almedio
        yini+=1+dy2/3
        glColor3f(r,g,b)
        glBegin(GL_QUADS)
        glVertex2f(xini,yini)
        glVertex2f(xini,yini+dy2/3)
        glVertex2f(xfin,yini+dy2/3)
        glVertex2f(xfin,yini)
        glEnd()
        #mas arriba
        yini+=1+dy2/3
        glColor3f(r,g,b)
        glBegin(GL_QUADS)
        glVertex2f(xini,yini)
        glVertex2f(xini,yini+dy2/3)
        glVertex2f(xfin,yini+dy2/3)
        glVertex2f(xfin,yini)
        glEnd()
        #ultima
        yini+=1+dy2/3
        glColor3f(r,g,b)
        glBegin(GL_QUADS)
        glVertex2f(xini, yini)
        glVertex2f(xini, yini + dy2 / 3)
        glVertex2f(xfin, yini + dy2 / 3)
        glVertex2f(xfin, yini)
        glEnd()


    def getpos(self):
        return self.pos.cartesianas()
    def getcenter(self):
        return self.centro.cartesianas()
    def setlife(self,nvida):
        self.vida=nvida
    def getlife(self):
        return self.vida