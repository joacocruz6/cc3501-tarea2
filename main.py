import os
import random
import pygame
from CC3501Utils import *
from Pared import *
from Vista import *
from Player import *
from Enemy import *
from BUtils import *
from Explosion import *
from Bombs import *
from PDes import *
from Fondo import *
from Power import *
import random as ran
import math as m
os.environ['SDL_VIDEO_CENTERED'] = '1'
def main(argv):
    ancho=800
    alto=600
    dx=53.0
    dy=46.0
    #################################################
    ##cargar sonidos del juego
    #################################################
    pygame.mixer.init()
    pygame.mixer.music.load("Mr. Blue Sky 8 bit.mp3")
    level_passed=pygame.mixer.Sound("Collect_Point_01.wav")
    beer1=pygame.mixer.Sound("beer01.wav")
    beerm=pygame.mixer.Sound("beer09m.wav")
    beermyh=pygame.mixer.Sound("beer04.wav")
    any_key=pygame.mixer.Sound("computer_any_key.wav")
    doh=pygame.mixer.Sound("doh1_y.wav")
    donut=pygame.mixer.Sound("doughnut.wav")
    fault=pygame.mixer.Sound("fault.wav")
    margegroan=pygame.mixer.Sound("groan2.wav")
    scoreman=pygame.mixer.Sound("man_v_machine.wav")
    flanders1=pygame.mixer.Sound("okie_dokie.wav")
    flanders2=pygame.mixer.Sound("recommend_you.wav")
    ralph1=pygame.mixer.Sound("ralphsnes.wav")
    ralph2=pygame.mixer.Sound("ralphplaydate.wav")
    bombsound=pygame.mixer.Sound("Hit_03.wav")
    #################################################
    pygame.mixer.Sound.play(any_key)
    dificultad=input("Nivel de dificultad, facil medio dificil o extremo: ")
    assert dificultad=="facil" or dificultad=="medio" or dificultad=="dificil" or dificultad== "extremo"
    cant=int(input("cantidad de jugadores (1 o 2): "))
    assert cant==1 or cant==2
    # cantidad de niveles a jugar
    nivelactual = 1
    niveles = int(input("Cantidad de niveles a jugar?: "))
    assert niveles >= 1
    inp= input("¿Ir Cambiando la dificultad? ")
    assert inp=="si" or inp=="no"
    cambiar_niveles= inp=="si"
    if cambiar_niveles:
        ratio=int(input("¿Cada cuantos niveles? "))
        assert ratio>0
        contador=0
        dificultad_max = input("¿Hasta que dificultad? ")
        assert dificultad_max=="medio" or dificultad_max=="dificil" or dificultad_max=="extremo"
    print("Nivel 1")
    init(ancho,alto,"Homeroman")
    #################################################
    ##Musica del fondo
    #################################################
    pygame.mixer.music.play(-1, 0.0)
    #################################################
    fondo=Fondo()
    direccion="arriba"
    paredes=[] #contenedor de paredes
    borde=[] #contenedor de las paredes del borde, para no generar el bug del salto
    for i in range(16):
        p1=Pared(Vector(53.0*i,0.0))
        p2=Pared(Vector(53.0*i,554))
        paredes.append(p1)
        paredes.append(p2)
        borde.append(p1)
        borde.append(p2)
    for j in range(14):
        p1=Pared(Vector(0.0,46*j))
        p2=Pared(Vector(747,46.0*j))
        paredes.append(p1)
        paredes.append(p2)
        borde.append(p1)
        borde.append(p2)
    for i in range(7):
        for j in range(6):
            paredes.append(Pared(Vector(dx*(2*i),dy*(2*j))))
    clock=pygame.time.Clock()
    #seteo los estados de los power ups
    power_ups=[False,False,False,False,False] #lista efecto de los power ups
    powers=[] #contenedor de los power ups
    powers_obtenidos=[]
    enemigos=[]
    bombas=[]#contenedor de bombas general
    if cant==2:
        bombas1=[] #bombas segundo player
        bombas2=[] #bombas segundo player
    explosiones=[] #contenedor de explosiones
    players=[] #contenedor de jugadores.
    destructibles=[] #contenedor de muros destructibles
    beacon=[]
    jugador=Player(Vector(dx*13,dy*11)) #jugador
    players.append(jugador)
    if cant==2:
        jugador2=Player(Vector(dx,11*dy),numero=2)
        players.append(jugador2)
        power_ups2=[False,False,False,False,False]
        direccion2="arriba"
        powers_obtenidos2=[]
    #procesos de creacion
    creaciondestructibles(destructibles,players,dificultad,dx,dy)
    creacionenemigos(enemigos,destructibles,players,dificultad,dx,dy)
    creacionposganar(destructibles,beacon)
    generate_pwup(powers,players,paredes,beacon,bombas,enemigos,dx,dy)
    generate_pwup(powers, players, paredes, beacon, bombas, enemigos, dx, dy)
    vista=Vista() #vista
    t0=pygame.time.get_ticks()
    t0_flanders=pygame.time.get_ticks()
    run=True
    pause= False #el juego parte no pausado
    while run:
        t=pygame.time.get_ticks()
        rango=power_ups[0]
        sobre_muros=power_ups[1]
        sobre_bombas=power_ups[2]
        inmortal=power_ups[3]
        cadena=power_ups[4]
        cant_pwup=len(powers)
        if cant==2:
            rango2=power_ups2[0]
            sobre_muros2=power_ups2[1]
            sobre_bombas2=power_ups2[2]
            inmortal2=power_ups2[3]
            cadena2=power_ups2[4]
        for event in pygame.event.get():
            #botton x de la ventana
            if event.type==QUIT:
                run=False
            keys=pygame.key.get_pressed()
            if keys[K_p]:
                if not pause:
                    t_pause=pygame.time.get_ticks()
                    pygame.mixer.music.pause()
                pause=True
            if keys[K_r]:
                dt = abs(t - t_pause)
                for bomba in bombas:
                    bomba.plustime(dt)
                for pw in powers_obtenidos:
                    pw.plustime(dt)
                if cant == 2:
                    for bomba1 in bombas1:
                        bomba1.plustime(dt)
                    for bomba2 in bombas2:
                        bomba2.plustime(dt)
                    for pw in powers_obtenidos2:
                        pw.plustime(dt)
                    t0_flanders = dt + t0_flanders
                pygame.mixer.music.unpause()
                pause=False
                t_pause=0
            if pause:
                # vuelco de cache en pantalla
                vista.dibujar(powers, fondo, players, paredes, destructibles, bombas, enemigos, explosiones, beacon,ancho, alto)  # dibujo
                pygame.display.flip()
                pygame.time.wait(int(1000 / 60))  # 60 fps
                continue

            if not pause:
                if cant==1: #si hay solo un jugador--->controles un jugador
                    if keys[pygame.K_RIGHT]:
                        if not chocaPared(jugador,paredes,destructibles,direccion,dx,dy)and not chocaBomba(jugador,bombas,direccion,dx,dy)and direccion=="derecha":
                            jugador.moverx(1)
                        elif direccion=="derecha" and chocaPared(jugador,paredes,destructibles,direccion,dx,dy) and sobre_muros:
                            i=dis_prox_espacio(jugador,paredes,borde,destructibles,bombas,direccion,dx,dy)
                            jugador.moverx(i)
                        elif direccion=="derecha" and chocaBomba(jugador,bombas,direccion,dx,dy) and sobre_bombas:
                            i=dis_prox_espacio(jugador,paredes,borde,destructibles,bombas,direccion,dx,dy)
                            jugador.moverx(i)
                        direccion="derecha"
                    if keys[pygame.K_LEFT]:
                        if not chocaPared(jugador,paredes,destructibles,direccion,dx,dy) and not chocaBomba(jugador,bombas,direccion,dx,dy) and direccion=="izquierda":
                            jugador.moverx(-1)
                        elif direccion=="izquierda" and chocaPared(jugador,paredes,destructibles,direccion,dx,dy) and sobre_muros:
                            i=dis_prox_espacio(jugador,paredes,borde,destructibles,bombas,direccion,dx,dy)
                            jugador.moverx(i)
                        elif direccion=="izquierda" and chocaBomba(jugador,bombas,direccion,dx,dy) and sobre_bombas:
                            i=dis_prox_espacio(jugador,paredes,borde,destructibles,bombas,direccion,dx,dy)
                            jugador.moverx(i)
                        direccion="izquierda"
                    if keys[pygame.K_DOWN]:
                        if not chocaPared(jugador,paredes,destructibles,direccion,dx,dy) and not chocaBomba(jugador,bombas,direccion,dx,dy) and direccion=="abajo":
                            jugador.movery(-1)
                        elif direccion=="abajo" and chocaPared(jugador,paredes,destructibles,direccion,dx,dy) and sobre_muros:
                            i=dis_prox_espacio(jugador,paredes,borde,destructibles,bombas,direccion,dx,dy)
                            jugador.movery(i)
                        elif direccion=="abajo" and chocaBomba(jugador,bombas,direccion,dx,dy) and sobre_bombas:
                            i=dis_prox_espacio(jugador,paredes,borde,destructibles,bombas,direccion,dx,dy)
                            jugador.movery(i)
                        direccion="abajo"
                    if keys[pygame.K_UP]:
                        if not chocaPared(jugador,paredes,destructibles,direccion,dx,dy) and not chocaBomba(jugador,bombas,direccion,dx,dy) and direccion=="arriba":
                            jugador.movery(1)
                        elif direccion=="arriba" and chocaPared(jugador,paredes,destructibles,direccion,dx,dy) and sobre_muros:
                            i=dis_prox_espacio(jugador,paredes,borde,destructibles,bombas,direccion,dx,dy)
                            jugador.movery(i)
                        elif direccion=="arriba" and chocaBomba(jugador,bombas,direccion,dx,dy) and sobre_bombas:
                            i=dis_prox_espacio(jugador,paredes,borde,destructibles,bombas,direccion,dx,dy)
                            jugador.movery(i)
                        direccion="arriba"
                    if keys[K_a]:
                        if not chocaPared(jugador,paredes,destructibles,direccion,dx,dy)and not chocaBomba(jugador,bombas,direccion,dx,dy) and not frenteEnemigo(jugador,enemigos,direccion,dx,dy):
                            ponerBomba(bombas,jugador,direccion,t)
                if cant==2:
                    vida1=jugador.vida
                    vida2=jugador2.vida
                    ################################
                    ###movimientos primer player####
                    ################################
                    if event.type == KEYDOWN:

                        if event.key== K_RIGHT and vida1:
                            if not chocaPared(jugador,paredes,destructibles,direccion,dx,dy)and not chocaBomba(jugador,bombas,direccion,dx,dy)and direccion=="derecha":
                                jugador.moverx(1)
                            elif direccion=="derecha" and chocaPared(jugador,paredes,destructibles,direccion,dx,dy) and sobre_muros:
                                i=dis_prox_espacio(jugador,paredes,borde,destructibles,bombas,direccion,dx,dy)
                                jugador.moverx(i)
                            elif direccion=="derecha" and chocaBomba(jugador,bombas,direccion,dx,dy) and sobre_bombas:
                                i=dis_prox_espacio(jugador,paredes,borde,destructibles,bombas,direccion,dx,dy)
                                jugador.moverx(i)
                            direccion="derecha"
                        if event.key == K_LEFT and vida1:
                            if not chocaPared(jugador,paredes,destructibles,direccion,dx,dy) and not chocaBomba(jugador,bombas,direccion,dx,dy) and direccion=="izquierda":
                                jugador.moverx(-1)
                            elif direccion=="izquierda" and chocaPared(jugador,paredes,destructibles,direccion,dx,dy) and sobre_muros:
                                i=dis_prox_espacio(jugador,paredes,borde,destructibles,bombas,direccion,dx,dy)
                                jugador.moverx(i)
                            elif direccion=="izquierda" and chocaBomba(jugador,bombas,direccion,dx,dy) and sobre_bombas:
                                i=dis_prox_espacio(jugador,paredes,borde,destructibles,bombas,direccion,dx,dy)
                                jugador.moverx(i)
                            direccion="izquierda"
                        if event.key == K_DOWN and vida1:
                            if not chocaPared(jugador,paredes,destructibles,direccion,dx,dy) and not chocaBomba(jugador,bombas,direccion,dx,dy) and direccion=="abajo":
                                jugador.movery(-1)
                            elif direccion=="abajo" and chocaPared(jugador,paredes,destructibles,direccion,dx,dy) and sobre_muros:
                                i=dis_prox_espacio(jugador,paredes,borde,destructibles,bombas,direccion,dx,dy)
                                jugador.movery(i)
                            elif direccion=="abajo" and chocaBomba(jugador,bombas,direccion,dx,dy) and sobre_bombas:
                                i=dis_prox_espacio(jugador,paredes,borde,destructibles,bombas,direccion,dx,dy)
                                jugador.movery(i)
                            direccion="abajo"
                        if event.key == K_UP and vida1:
                            if not chocaPared(jugador,paredes,destructibles,direccion,dx,dy) and not chocaBomba(jugador,bombas,direccion,dx,dy) and direccion=="arriba":
                                jugador.movery(1)
                            elif direccion=="arriba" and chocaPared(jugador,paredes,destructibles,direccion,dx,dy) and sobre_muros:
                                i=dis_prox_espacio(jugador,paredes,borde,destructibles,bombas,direccion,dx,dy)
                                jugador.movery(i)
                            elif direccion=="arriba" and chocaBomba(jugador,bombas,direccion,dx,dy) and sobre_bombas:
                                i=dis_prox_espacio(jugador,paredes,borde,destructibles,bombas,direccion,dx,dy)
                                jugador.movery(i)
                            direccion="arriba"
                        ################################
                        ###movimientos segundo player###
                        ################################
                        if event.key == K_d and vida2:
                            if not chocaPared(jugador2,paredes,destructibles,direccion2,dx,dy)and not chocaBomba(jugador2,bombas,direccion2,dx,dy)and direccion2=="derecha":
                                jugador2.moverx(1)
                            elif direccion2=="derecha" and chocaPared(jugador2,paredes,destructibles,direccion2,dx,dy) and sobre_muros2:
                                i=dis_prox_espacio(jugador2,paredes,borde,destructibles,bombas,direccion2,dx,dy)
                                jugador2.moverx(i)
                            elif direccion2=="derecha" and chocaBomba(jugador2,bombas,direccion2,dx,dy) and sobre_bombas2:
                                i=dis_prox_espacio(jugador2,paredes,borde,destructibles,bombas,direccion2,dx,dy)
                                jugador2.moverx(i)
                            direccion2="derecha"
                        if event.key == K_a and vida2:
                            if not chocaPared(jugador2,paredes,destructibles,direccion2,dx,dy) and not chocaBomba(jugador2,bombas,direccion2,dx,dy) and direccion2=="izquierda":
                                jugador2.moverx(-1)
                            elif direccion2=="izquierda" and chocaPared(jugador2,paredes,destructibles,direccion2,dx,dy) and sobre_muros2:
                                i=dis_prox_espacio(jugador2,paredes,borde,destructibles,bombas,direccion,dx,dy)
                                jugador2.moverx(i)
                            elif direccion2=="izquierda" and chocaBomba(jugador2,bombas,direccion2,dx,dy) and sobre_bombas2:
                                i=dis_prox_espacio(jugador2,paredes,borde,destructibles,bombas,direccion2,dx,dy)
                                jugador2.moverx(i)
                            direccion2="izquierda"
                        if event.key == K_s and vida2:
                            if not chocaPared(jugador2,paredes,destructibles,direccion2,dx,dy) and not chocaBomba(jugador2,bombas,direccion2,dx,dy) and direccion2=="abajo":
                                jugador2.movery(-1)
                            elif direccion2=="abajo" and chocaPared(jugador2,paredes,destructibles,direccion2,dx,dy) and sobre_muros2:
                                i=dis_prox_espacio(jugador2,paredes,borde,destructibles,bombas,direccion,dx,dy)
                                jugador2.movery(i)
                            elif direccion2=="abajo" and chocaBomba(jugador2,bombas,direccion2,dx,dy) and sobre_bombas2:
                                i=dis_prox_espacio(jugador2,paredes,borde,destructibles,bombas,direccion2,dx,dy)
                                jugador2.movery(i)
                            direccion2="abajo"
                        if event.key == K_w and vida2:
                            if not chocaPared(jugador2,paredes,destructibles,direccion2,dx,dy) and not chocaBomba(jugador2,bombas,direccion2,dx,dy) and direccion2=="arriba":
                                jugador2.movery(1)
                            elif direccion2=="arriba" and chocaPared(jugador2,paredes,destructibles,direccion2,dx,dy) and sobre_muros2:
                                i=dis_prox_espacio(jugador2,paredes,borde,destructibles,bombas,direccion2,dx,dy)
                                jugador2.movery(i)
                            elif direccion2=="arriba" and chocaBomba(jugador2,bombas,direccion2,dx,dy) and sobre_bombas2:
                                i=dis_prox_espacio(jugador2,paredes,borde,destructibles,bombas,direccion2,dx,dy)
                                jugador2.movery(i)
                            direccion2="arriba"
                        #poner bombas
                        if event.key == K_BACKSPACE and vida1:
                            if not chocaPared(jugador,paredes,destructibles,direccion,dx,dy)and not chocaBomba(jugador,bombas,direccion,dx,dy) and not frenteEnemigo(jugador,enemigos,direccion,dx,dy):
                                ponerBomba(bombas,jugador,direccion,t)
                                ponerBomba(bombas1,jugador,direccion,t)
                        if event.key == K_b and vida2:
                            if not chocaPared(jugador2,paredes,destructibles,direccion2,dx,dy)and not chocaBomba(jugador2,bombas,direccion2,dx,dy) and not frenteEnemigo(jugador2,enemigos,direccion2,dx,dy):
                                ponerBomba(bombas,jugador2,direccion2,t)
                                ponerBomba(bombas2,jugador2,direccion2,t)
                moverEnemigo(enemigos,paredes,destructibles,bombas,dificultad,dx,dy)
                if abs(t0_flanders-t)>=7000 and len(enemigos)!=0:
                    sonido_f=random.randint(1,4)
                    if sonido_f==1:
                        pygame.mixer.Sound.play(flanders1)
                    if sonido_f==2:
                        pygame.mixer.Sound.play(flanders2)
                    if sonido_f==3:
                        pygame.mixer.Sound.play(ralph1)
                    if sonido_f==4:
                        pygame.mixer.Sound.play(ralph2)
                    t0_flanders=t
                if cant==1:
                    explosion_bombas(explosiones,bombas,paredes,rango,t,bombsound) #ve si las bombas explotan
                    if cadena:
                        provoco=cadena_explosiones(explosiones,bombas,bombsound,paredes,rango,t)
                if cant==2:
                    explosion_bombas(explosiones, bombas, paredes, False, t,bombsound)  # ve si las bombas explotan
                    explosion_bombas(explosiones,bombas1,paredes,rango,t)
                    explosion_bombas(explosiones,bombas2,paredes,rango2,t)
                    if cadena:
                        provoco1=cadena_explosiones(explosiones,bombas1,bombsound,paredes,rango,t)
                        if provoco1:
                            provoco=cadena_explosiones(explosiones,bombas,None,paredes,rango,t)
                    if cadena2:
                        provoco2=cadena_explosiones(explosiones,bombas2,bombsound,paredes,rango,t)
                        if provoco2:
                            provoco=cadena_explosiones(explosiones,bombas,None,paredes,rango,t)
                lexp(explosiones,t) #ve si hay  explosiones que desaparecen
                explotar(destructibles,explosiones) #explotan los destructibles
                explotar(enemigos,explosiones) #explotan los enemigos
                explotar(players,explosiones) #ve si explotamos nosotros
                choque_players(players,enemigos) #ve si tocamos a los enemigos
                #obtencion de power ups
                obtener_pwup(jugador,powers,powers_obtenidos,power_ups,t,donut)
                #efecto power up inmortalidad
                if inmortal:
                    jugador.setlife(True)
                #ver duracion de power ups
                duracion_pwup(powers,power_ups,t)
                duracion_pwup(powers_obtenidos,power_ups,t)
                pwup_color(jugador,powers_obtenidos,power_ups)
                ###############
                ###2 players###
                ###############
                if cant==2:
                    #obtencion powerups
                    duracion_pwup(powers,power_ups2,t)
                    duracion_pwup(powers_obtenidos2,power_ups2,t)
                    obtener_pwup(jugador2,powers,powers_obtenidos2,power_ups2,t)
                    pwup_color(jugador2,powers_obtenidos2,power_ups2)
                    pwup_color(jugador,powers_obtenidos,power_ups)
                    #efecto power up inmortalidad
                    if inmortal2:
                        jugador2.setlife(True)
                #generacion de powerups, no pueden haber mas de 5
                dif=abs(t-t0)
                if dif>=15000.0 and cant_pwup<=5:
                    t0=t #actualizo el tiempo
                    generate_pwup(powers, players, paredes, beacon, bombas, enemigos, dx, dy) #genero pwup
                #limpieza de arreglos
                limpiar(bombas)
                limpiar(explosiones)
                limpiar(destructibles)
                limpiar(enemigos)
                limpiar(powers)
                limpiar(powers_obtenidos)
                limpiar(players)
                if cant==2:
                    limpiar(powers_obtenidos2)
                    limpiar(bombas1)
                    limpiar(bombas2)
                # vuelco de cache en pantalla
                vista.dibujar(powers, fondo, players, paredes, destructibles, bombas, enemigos, explosiones, beacon, ancho, alto)  # dibujo
                pygame.display.flip()
                pygame.time.wait(int(1000 / 30))  # 60 fps
                #ver si ganas o pierdes:
                if len(players)==0:
                    print("Perdiste :C")
                    if cant==1:
                        pygame.mixer.Sound.play(doh)
                    if cant==2:
                        i=random.randint(1,2)
                        if i==1:
                            pygame.mixer.Sound.play(margegroan)
                        if i==2:
                            pygame.mixer.Sound.play(fault)
                    pygame.time.wait(4000)
                    run=False
                if ganaste(beacon,players):
                    if nivelactual==niveles:
                        print("Ganaste :)")
                        pygame.mixer.music.stop()
                        if cant == 1:
                            i = random.randint(0, 1)
                            if i == 1:
                                pygame.mixer.Sound.play(beer1)
                            if i == 0:
                                pygame.mixer.Sound.play(scoreman)
                        if cant == 2:
                            i = random.randint(0, 3)
                            if i == 1:
                                pygame.mixer.Sound.play(beer1)
                            if i == 0:
                                pygame.mixer.Sound.play(scoreman)
                            if i == 2:
                                pygame.mixer.Sound.play(beerm)
                            if i == 3:
                                pygame.mixer.Sound.play(beermyh)
                        pygame.time.wait(5000)
                        run=False
                    else:
                        nivelactual+=1
                        print("Nivel: "+str(nivelactual)+" de "+str(niveles))

                        if cambiar_niveles:
                            contador+=1
                            if contador==ratio:
                                if dificultad=="facil":
                                    dificultad="medio"
                                elif dificultad=="medio" and not dificultad_max=="medio":
                                    dificultad="dificil"
                                elif dificultad=="dificil" and not dificultad_max=="dificil":
                                    dificultad="extremo"
                                contador=0
                        print("Dificultad: " + dificultad)
                        pygame.mixer.Sound.play(level_passed)
                        pygame.time.wait(200)
                        for pw in powers:
                            toma=pw.gettomado()
                            if not toma:
                                pw.setlife(False)
                        limpiar(powers)
                        destructibles=[]
                        enemigos=[]
                        beacon=[]
                        bombas=[]
                        explosiones=[]
                        if cant==2:
                            bombas1=[]
                            bombas2=[]
                            for pw in powers_obtenidos:
                                toma=pw.gettomado()
                                if not toma:
                                    pw.setlife(False)
                            for pw in powers_obtenidos2:
                                toma=pw.gettomado()
                                if not toma:
                                    pw.setlife(False)
                        creacionnivel(beacon,powers,enemigos,paredes,destructibles,players,bombas,dificultad,dx,dy)
    #fin del juego
    pygame.quit()



if __name__=="__main__":
    import sys
    main(sys.argv)



