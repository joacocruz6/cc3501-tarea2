from CC3501Utils import *
class Fondo(Figura):
    def __init__(self,pos=Vector(0.0,0.0),rgb=(138.0/255,138.0/255,138.0/255)):
        super().__init__(pos,rgb)
    def figura(self):
        """
        Dibuja el fondo
        :return: None
        """
        ancho=15
        alto=13
        dx=53.0
        dy=46.0
        (r,g,b)=self.color
        for i in range(ancho):
            for j in range(alto):
                glColor3f(83.0/255,83.0/255,85.0/255)
                glBegin(GL_QUADS)
                glVertex2f(i*dx,j*dy)
                glVertex2f(i*dx,j*dy+dy)
                glVertex2f(i*dx+dx,j*dy+dy)
                glVertex2f(i*dx+dx,j*dy)
                glEnd()
                glColor3f(r,g,b)
                glBegin(GL_QUADS)
                glVertex2f(i * dx+2.0, j * dy+2.0)
                glVertex2f(i * dx+2.0, j * dy + dy-2.0)
                glVertex2f(i * dx + dx-2.0, j * dy + dy-2.0)
                glVertex2f(i * dx + dx-2.0, j * dy+2.0)
                glEnd()