
from CC3501Utils import *
from Bombs import *
from Vista import *
from Pared import *
from Player import *
from Explosion import *
from PDes import *
from Enemy import *
from Win import *
from Power import *
import pygame
import math as m
import random as rand

#################################################################
#######MODULO DE FUNCIONES AUXILIARES PARA EL BOMBERMAN
#################################################################





###################
######choques######
###################
def chocaPared(p,l_pared,l_destructibles,direccion,dx,dy):
    """
    True si esta chocando una pared
    :param p: Player or Enemy
    :param l_pared: List (listas de paredes)
    :param direccion: str
    :param dx: float
    :param dy: float
    :return: boolean
    """
    (x,y)=p.getcenter()
    epsilon=20
    if direccion=="arriba":
        y+=dy
    if direccion=="abajo":
        y-=dy
    if direccion=="izquierda":
        x-=dx
    if direccion=="derecha":
        x+=dx
    for j in l_pared:
        (z,w)=j.getcenter()
        if abs(z-x)<epsilon and abs(w-y)<epsilon:
            return True
    for j in l_destructibles:
        (z,w)=j.getcenter()
        if abs(z-x)<epsilon and abs(w-y)<epsilon:
            return True
    return False

def chocar(obj1,obj2):
    """
    True si objeto 1 y objeto 2 chocan
    :param obj1: Object
    :param obj2: Object
    :return: boolean
    """
    (x,y)=obj1.getcenter()
    (z,w)=obj2.getcenter()
    epsilon=20
    return abs(z-x)<epsilon and abs(w-y)<epsilon

def frenteEnemigo(p,l_enemigos,direccion,dx,dy):
    """
    True si p esta en frente de un enemigo
    :param p: Enemy or Player
    :param l_enemigos: list(Enemy)
    :param direccion: str
    :param dx: float
    :param dy: float
    :return: boolean
    """
    (x,y)=p.getcenter()
    epsilon=20
    if direccion=="arriba":
        y+=dy
    if direccion=="abajo":
        y-=dy
    if direccion=="izquierda":
        x-=dx
    if direccion=="derecha":
        x+=dx
    for enemigo in l_enemigos:
        (z,w)=enemigo.getcenter()
        if abs(z-x)<epsilon and abs(w-y)<epsilon:
            return True
    return False

def moverEnemigo(l_enemigos,l_pared,l_destructibles,l_bombas,dificultad,dx,dy):
    """
    Mueve los enemigos a posiciones adyacentes aleatorias
    :param enemigo: Enemy
    :param l_pared: list
    :param l_destructibles: list
    :param dx: float
    :param dy: float
    :return: none
    """
    n=100
    if dificultad=="medio":
        n=50
    if dificultad=="dificil":
        n=25
    if dificultad=="extremo":
        n=5
    direcciones = ["arriba", "abajo", "izquierda", "derecha"]
    for enemigo in l_enemigos:
        aux=[]
        for e in l_enemigos:
            if e!=enemigo:
                aux.append(e)
        j=rand.randint(0,n)
        if j<4:
            dire=direcciones[j]
            if not chocaPared(enemigo,l_pared,l_destructibles,dire,dx,dy) and not chocaBomba(enemigo,l_bombas,dire,dx,dy) and not frenteEnemigo(enemigo,aux,dire,dx,dy):
                if dire=="arriba":
                    enemigo.movery(1)
                if dire=="abajo":
                    enemigo.movery(-1)
                if dire=="izquierda":
                    enemigo.moverx(-1)
                if dire=="derecha":
                    enemigo.moverx(1)
def chocaBorde(p,l_borde,direccion,dx,dy):
    """
    True si el player o enemy apunta hacia un borde del laberinto
    :param p: Player or Enemy
    :param l_borde: List
    :param direccion: str
    :param dx: num
    :param dy: num
    :return: boolean
    """
    (x, y) = p.getcenter()
    epsilon = 20
    if direccion == "arriba":
        y += dy
    if direccion == "abajo":
        y -= dy
    if direccion == "izquierda":
        x -= dx
    if direccion == "derecha":
        x += dx
    for j in l_borde:
        (z, w) = j.getcenter()
        if abs(z - x) < epsilon and abs(w - y) < epsilon:
            return True
    return False

#####################
######power ups######
#####################
#mecanicas:
def dis_prox_espacio(p,l_paredes,l_borde,l_destructibles,l_bomba,direccion,dx,dy):
    """
    Da cuantos pasos debe hacer el jugador para llegar al proximo sin una pared o bomba, sirve para los power ups de saltos
    :param p: Player
    :param l_paredes: list
    :param l_bordes: list
    :param l_destructibles: list
    :param l_bomba: list
    :param direccion: str
    :param dx:num
    :param dy:num
    :return:int
    """
    i=1
    inc=1
    (x,y)=p.getpos()
    aux=Player(Vector(x,y))
    if direccion=="abajo" or direccion=="izquierda":
        i=-1
        inc=-1
    while True:
        if chocaBorde(aux, l_borde, direccion, dx, dy):
            i = 0
            break
        if not chocaPared(aux,l_paredes,l_destructibles,direccion,dx,dy) and not chocaBomba(aux,l_bomba,direccion,dx,dy):
            break
        if direccion == "derecha":
            aux.moverx(1)
        if direccion == "arriba":
            aux.movery(1)
        if direccion == "abajo":
            aux.movery(-1)
        if direccion == "izquierda":
            aux.moverx(-1)
        i+=inc
    return i
#generacion:
def generate_pwup(l_pw,l_players,l_paredes,l_win,l_bombas,l_enemigos,dx,dy):
    """
    Genera un power up al azar en una posicion al azar
    :param l_pw: list
    :param l_players: list
    :param l_paredes: list
    :param l_win: list
    :param l_bombas: list
    :param l_enemigos: list
    :param dx: num
    :param dy: num
    :return: None
    """
    tipos=["rango","pared","bomba","inmortal","cadena"]
    k=rand.randint(0,4)
    tipe=tipos[k]
    while True:
        i=rand.randint(0,14)
        j=rand.randint(0,12)
        pw=Power(Vector(i*dx,j*dy),tipe)
        poner=True
        for pared in l_paredes:
            if chocar(pared,pw):
                poner=False
        for power in l_pw:
            if chocar(pw,power):
                poner=False
        for jugador in l_players:
            if chocar(jugador,pw):
                poner=False
        for win in l_win:
            if chocar(win,pw):
                poner=False
        for bomb in l_bombas:
            if chocar(bomb,pw):
                poner=False
        for enemigo in l_enemigos:
            if chocar(enemigo,pw):
                poner=False
        if poner:
            l_pw.append(pw)
            break
#obtencion,duracion y obtencion
def obtener_pwup(p: Player,l_power_ups,l_obtenidos,l_activados,t_a,sound=None):
    """
    Mecanica para obtener un power up
    :param p: Player
    :param l_power_ups: list
    :param l_obtenidos: list
    :param l_activados: list
    :param t_a: num
    :param sound: wav or None
    :return: None
    """
    prob=rand.randint(0,100)
    for pw in l_power_ups:
        if chocar(p,pw):
            if prob <= 40 and sound != None:
                pygame.mixer.Sound.play(sound)
            pw.tomar(t_a)
            l_obtenidos.append(pw)
            i=pw.getindex()
            l_activados[i]=True
def duracion_pwup(l_power_ups,l_activados,t_a):
    """
    Ve si el power up debe parar o no
    :param l_power_ups: list
    :param l_activados: list
    :param t_a: num
    :return: None
    """
    for pw in l_power_ups:
        tomado=pw.gettomado()
        if tomado:
            tiempo=pw.gettime()
            duracion=pw.getduracion()
            dif= abs(tiempo-t_a)
            if dif>=duracion:
                pw.setlife(False)
                i=pw.getindex()
                l_activados[i]=False
            else:
                i=pw.getindex()
                l_activados[i]=True
def pwup_color(p: Player,l_power_ups,l_activados):
    """
    Cambia el color de la camisa o el vestido
    :param p: Player
    :param l_power_ups: list
    :param l_activados: list
    :return: None
    """
    for pw in l_power_ups:
        i=pw.getindex()
        if l_activados[i]:
            (r,g,b)=pw.getcoloracion()
            p.setcoloracion((r,g,b))
    inactivos=True
    for efecto in l_activados:
        if efecto:
            inactivos=False
    if inactivos:
        p.normalizar_camisa()

###################
######bombas#######
###################
def chocaBomba(p,l_bombas,direccion,dx,dy):
    """
    Ve si el jugador o enemigo va a chocar con una bomba ( o apunta hacia ella)
    :param p: Player or Enemy
    :param l_bombas: list
    :param direccion: str
    :param dx: num
    :param dy: num
    :return: boolean
    """
    (x,y)=p.getcenter()
    epsilon=20
    if direccion=="arriba":
        y+=dy
    if direccion=="izquierda":
        x-=dx
    if direccion=="abajo":
        y-=dy
    if direccion=="derecha":
        x+=dx
    for bomba in l_bombas:
        (z,w)=bomba.getcenter()
        if abs(z-x)<epsilon and abs(w-y)<epsilon:
            return True
    return False

def ponerBomba(l_bombas,jugador,direccion,t):
    """
    pone una bomba en la direccion en que se mira
    :param l_bombas: List
    :param jugador: Player
    :param direccion: str
    :param t: float
    :return: none
    """
    (px,py)=jugador.getpos()
    if direccion=="derecha":
        l_bombas.append(Bombs(Vector(px+53.0,py),t))
    if direccion=="izquierda":
        l_bombas.append(Bombs(Vector(px-53.0,py),t))
    if direccion=="arriba":
        l_bombas.append(Bombs(Vector(px,py+46.0),t))
    if direccion=="abajo":
        l_bombas.append(Bombs(Vector(px,py-46.0),t))
def explosion_bombas(l_explosiones,l_bombas,l_paredes,rango,t_a,sonido=None):
    """
    Ve que bombas deben explotar y genera las explosiones correspondientes
    :param l_explosiones: list
    :param l_bombas: list
    :param l_paredes: list
    :param rango: boolean
    :param t_a: num
    :param sonido: wav or None
    :return: None
    """
    dx=53.0
    dy=46.0
    for bomba in l_bombas:
        t0=bomba.gettime()
        dt=t_a-t0
        if dt>=3000.0:
            if sonido!=None:
                pygame.mixer.Sound.play(sonido)
            (x,y)=bomba.getcenter()
            xp=x-dx/2
            yp=y-dy/2
            e=Explosion(t_a,Vector(xp,yp))
            (e_arriba,ar)=(Explosion(t_a,Vector(xp,yp+dy)),True)
            (e_izq,iz)=(Explosion(t_a,Vector(xp-dx,yp)),True)
            (e_abajo,aba)=(Explosion(t_a,Vector(xp,yp-dy)),True)
            (e_der,der)=(Explosion(t_a,Vector(xp+dx,yp)),True)
            for pared in l_paredes:
                if chocar(e_arriba,pared):
                    ar=False
                if chocar(e_izq,pared):
                    iz=False
                if chocar(e_abajo,pared):
                    aba=False
                if chocar(e_der,pared):
                    der=False
            l_explosiones.append(e)
            if ar:
                l_explosiones.append(e_arriba)
            if iz:
                l_explosiones.append(e_izq)
            if aba:
                l_explosiones.append(e_abajo)
            if der:
                l_explosiones.append(e_der)
            #si tengo el power up:
            if rango:
                if ar:
                    (p_arriba,ar2)=(Explosion(t_a,Vector(xp,yp+2*dy)),True)
                if iz:
                    (p_izq,iz2)=(Explosion(t_a,Vector(xp-2*dx,yp)),True)
                if aba:
                    (p_aba,aba2)=(Explosion(t_a,Vector(xp,yp-2*dy)),True)
                if der:
                    (p_der,der2)=(Explosion(t_a,Vector(xp+2*dx,yp)),True)
                for pared in l_paredes:
                    if ar:
                        if chocar(p_arriba,pared):
                            ar2 = False
                    if iz:
                        if chocar(p_izq, pared):
                            iz2 = False
                    if aba:
                        if chocar(p_aba, pared):
                            aba2 = False
                    if der:
                        if chocar(p_der, pared):
                            der2 = False
                if ar:
                    if ar2:
                        l_explosiones.append(p_arriba)
                if iz:
                    if iz2:
                        l_explosiones.append(p_izq)
                if aba:
                    if aba2:
                        l_explosiones.append(p_aba)
                if der:
                    if der2:
                        l_explosiones.append(p_der)
            bomba.setlife(False)

        if dt>=1000.0 and not bomba.getcambio():
            bomba.color=(63.0/255,63.0/255,63.0/255)
            bomba.Cambio_change()
def explotar(l_objetos,l_exp):
    """
    Ve que objetos son alcanzados por la explosion y los mata
    :param l_objetos: list
    :param l_exp: list
    :return: None
    """
    for obj in l_objetos:
        for exp in l_exp:
            if chocar(obj,exp):
                obj.setlife(False)
def choque_players(l_players,l_enemigo):
    """
    Ve si un enemigo esta chocando con un jugador
    :param l_players: list
    :param l_enemigo: list
    :return: None
    """
    for enemigo in l_enemigo:
        for p in l_players:
            if chocar(p,enemigo):
                p.setlife(False)
def cadena_explosiones(l_explosiones,l_bombas,sonido,l_paredes,rango,t_a):
    """
    Ve si hay que hacer una cadena de explosiones con el power up
    :param l_explosiones: list
    :param l_bombas: list
    :param sonido: wav or None
    :param l_paredes: list
    :param rango:boolean
    :param t_a: num
    :return: boolean
    """
    respuesta=False
    for explosion in l_explosiones:
        for bomba in l_bombas:
            if chocar(explosion,bomba):
                bomba.settime(4000)
                respuesta=True
    explosion_bombas(l_explosiones,l_bombas,l_paredes,rango,t_a,sonido)
    return respuesta
######################
######creacion########
######################
def creaciondestructibles(l_destructibles,l_players,dificultad,dx,dy):
    """
    Crea las paredes destructibles iniciales en posiciones aleatorias
    :param l_destructibles: List
    :param l_players: Player
    :param dx: num
    :param dy: num
    :return:
    """
    pos_players=[]
    for p in l_players:
        (x,y)=p.getcenter()
        pos_players.append((x,y))
        pos_players.append((x+dx,y))
        pos_players.append((x-dx,y))
        pos_players.append((x,y+dy))
        pos_players.append((x,y-dy))
        pos_players.append((x + 2*dx, y))
        pos_players.append((x - 2*dx, y))
        pos_players.append((x, y + 2*dy))
        pos_players.append((x, y - 2*dy))
    numeros=[]

    n_min=5
    n_max=20
    if dificultad=="medio":
        n_min=15
        n_max=25
    if dificultad=="dificil":
        n_min=25
        n_max=28
    if dificultad=="extremo":
            n_min=30
            n_max=30
    n_destructibles=rand.randint(n_min,n_max)
    i=0;
    while i<n_destructibles:
        y=rand.randrange(1,11)
        if y%2==0:
            x=rand.randrange(1,13,2)
        if y%2!=0:
            x=rand.randrange(1,13)
        if (x,y) in numeros:
            continue
        else:
            pared=PDes(Vector(x*dx,y*dy))
            if pared.getcenter() in pos_players:
                continue
            else:
                numeros.append((x,y))
                l_destructibles.append(pared)
                i+=1

def creacionenemigos(l_enemigos,l_destructibles,l_players,dificultad,dx,dy):
    """
    Crea n enemigos en posiciones aleatorias, segun la dificultad escogida
    :param l_enemigos:List
    :param l_destructibles: List
    :param l_players: List
    :param dx: num
    :param dy: num
    :return: None
    """
    pos_players=[]
    for p in l_players:
        (x,y)=p.getpos()
        pos_players.append(p)
        pos_players.append(Player(Vector(x+dx,y)))
        pos_players.append(Player(Vector(x - dx, y)))
        pos_players.append(Player(Vector(x, y+dy)))
        pos_players.append(Player(Vector(x, y-dy)))
        pos_players.append(Player(Vector(x + 2*dx, y)))
        pos_players.append(Player(Vector(x - 2*dx, y)))
        pos_players.append(Player(Vector(x, y+2*dx)))
        pos_players.append(Player(Vector(x , y-2*dy)))
    max=4
    min=4
    if dificultad=="medio":
        min=7
        max=10
    if dificultad=="dificil":
        min=10
        max=13
    if dificultad=="extremo":
        if len(l_players)==2:
            min=14
            max=14
        else:
            min=15
            max=15
    n_enemigos = rand.randint(min,max)
    i = 0;
    while i < n_enemigos:
        y = rand.randrange(1, 11)
        if y % 2 == 0:
            x = rand.randrange(1, 13, 2)
        if y % 2 != 0:
            x = rand.randrange(1, 13)
        else:
            tipe=rand.randint(1,2)
            enemigo=Enemy(Vector(x*dx, y*dy),tipe)
            poner=True
            for p in pos_players:
                if chocar(enemigo,p):
                    poner=False
            for destructible in l_destructibles:
                if chocar(enemigo,destructible):
                    poner=False
            for e in l_enemigos:
                if chocar(enemigo,e):
                    poner=False
            if poner:
                l_enemigos.append(enemigo)
                i += 1

def creacionposganar(l_destructibles: list,l_win):
    """
    genera la posicion de victoria dentro de una caja destructible al azar
    :param l_destructibles: list
    :param l_win: list
    :return: None
    """
    i=rand.randrange(0,len(l_destructibles)-1)
    des=l_destructibles[i]
    l_win.append(Win(des.pos))
#############################
###Creacion de mas niveles###
#############################
def creacionnivel(l_win,l_powers,l_enemigos,l_paredes,l_destructibles,l_players,l_bombas,dificultad,dx,dy):
    """
    Crea un nivel nuevo al azar
    :param l_win: list
    :param l_powers: list
    :param l_enemigos: list
    :param l_paredes: list
    :param l_destructibles: list
    :param l_players: list
    :param l_bombas: list
    :param dificultad: str
    :param dx: num
    :param dy: num
    :return: None
    """
    creaciondestructibles(l_destructibles,l_players,dificultad,dx,dy)
    creacionenemigos(l_enemigos,l_destructibles,l_players,dificultad,dx,dy)
    creacionposganar(l_destructibles,l_win)
    generate_pwup(l_powers,l_players,l_paredes,l_win,l_bombas,l_enemigos,dx,dy)
    generate_pwup(l_powers, l_players, l_paredes, l_win, l_bombas, l_enemigos, dx, dy)
####################
######limpieza######
####################
def ganaste(l_win,l_player):
    """
    True si algun jugador toco la posicion de victoria
    :param l_win: list
    :param l_player: list
    :return: boolean
    """
    p=l_win[0]
    for jugador in l_player:
        if chocar(jugador,p):
            return True
    return False
def lexp(l_explosiones,t_a):
    """
    Modifica el estado de las explosiones
    :param l_explosiones: List
    :param t_a: num
    :return: none
    """
    for exp in l_explosiones:
        t0=exp.gettime()
        dt=t_a-t0
        if dt>=500.0:
            exp.setlife(False)
def limpiar(arr):
    """
    Borra los elementos que no estan en escena (o no estan vivos)
    :param arr: List
    :return: none
    """
    n=len(arr)
    aux=[]
    for i in range(n):
        elemento=arr.pop(0)
        if elemento.getlife():
            aux.append(elemento)
    for b in aux:
        arr.append(b)