from tkinter import NE
import pygame
import random
from pila_grafica import pilaGrafica

NEGRO = (0,0,0)
BLANCO = (255,255,255)
VERDE = (0,255,0)
ROJO = (255,0,0)
AZUL = (0,0,255)

PELOTAS = 6

def main():
    pygame.init()

    dimensiones = [700,500]
    pantalla = pygame.display.set_mode(dimensiones)
    pygame.display.set_caption("Mete Bolas!!")
    
    cerrar = False
    reloj = pygame.time.Clock()

    pila1 = pilaGrafica(10,60,80,400)
    pila2 = pilaGrafica(120,60,80,400)
    pila3 = pilaGrafica(230,60,80,400)
    pila4 = pilaGrafica(340,60,80,400)
    posx = 0
    posy = 0
    pelota_en_juego = NEGRO
    maximo_pelotas = 8
    bandera = False

    def que_color(valor):
        if valor == 0:
            color = NEGRO
        elif valor == 1:
            color = VERDE
        elif valor == 2:
            color = ROJO
        elif valor == 3:
            color = AZUL
        return color
    
    def elimina_3(pila):
        contador = 1
        color = BLANCO
        temporal = pilaGrafica(0,0,0,0)
        while not pila.pila_vacia():
            color = pila.quitar()
            temporal.insertar(color)
            if pila.topePila() == color:
                contador += 1
                if contador == 3:
                    pila.quitar()
                    temporal.quitar()
                    temporal.quitar()
                    contador = 1
            else:
                contador = 1
        while not temporal.pila_vacia():
            pila.insertar(temporal.quitar())

    def reiniciar():
        t = []
        for i in range(PELOTAS * 4):
            t.append(i % 4)
        random.shuffle(t)

        for i in range(PELOTAS):
            color = que_color(t.pop(0))
            pila1.insertar(color)
        for i in range(PELOTAS):
            color = que_color(t.pop(0))
            pila2.insertar(color)
        for i in range(PELOTAS):
            color = que_color(t.pop(0))
            pila3.insertar(color)
        for i in range(PELOTAS):
            color = que_color(t.pop(0))
            pila4.insertar(color)

    def dibujar_pila(pantalla, pila):
        
        elimina_3(pila)
        pygame.draw.rect(pantalla, NEGRO,[pila.x1,pila.y1,pila.ancho,pila.alto],2)
        elementos = pila.elementos()
        ptemp = pilaGrafica(pila.x1,pila.y1,pila.ancho,pila.alto)

        while not pila.pila_vacia():
            ptemp.insertar(pila.quitar())

        while not ptemp.pila_vacia():
            elementos = ptemp.elementos()
            pelota = ptemp.quitar()
            pila.insertar(pelota)
            pygame.draw.circle(pantalla, pelota, [pila.x1+40,pila.y1+25+((elementos-1)*50)],20) 

    reiniciar()          
    

    while not cerrar:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cerrar = True
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                posx = pos[0]
                posy = pos[1]
                if not bandera :
                    if posx >= pila1.x1 and posx < pila1.x1+pila1.ancho and not pila1.pila_vacia():
                        pelota_en_juego = pila1.quitar()
                        bandera = True
                    elif posx >= pila2.x1 and posx < pila2.x1+pila2.ancho and not pila2.pila_vacia():
                        pelota_en_juego = pila2.quitar()
                        bandera = True
                    elif posx >= pila3.x1 and posx < pila3.x1+pila3.ancho and not pila3.pila_vacia():
                        pelota_en_juego = pila3.quitar()
                        bandera = True
                    elif posx >= pila4.x1 and posx < pila4.x1+pila4.ancho and not pila4.pila_vacia():
                        pelota_en_juego = pila4.quitar()
                        bandera = True
                else:
                    if posx >= pila1.x1 and posx < pila1.x1+pila1.ancho and pila1.elementos() < maximo_pelotas:
                        pila1.insertar(pelota_en_juego)
                        pelota_en_juego = BLANCO
                        bandera = False
                    elif posx >= pila2.x1 and posx < pila2.x1+pila2.ancho and pila2.elementos() < maximo_pelotas:
                        pila2.insertar(pelota_en_juego)
                        pelota_en_juego = BLANCO
                        bandera = False
                    elif posx >= pila3.x1 and posx < pila3.x1+pila3.ancho and pila3.elementos() < maximo_pelotas:
                        pila3.insertar(pelota_en_juego)
                        pelota_en_juego = BLANCO
                        bandera = False
                    elif posx >= pila4.x1 and posx < pila4.x1+pila4.ancho and pila4.elementos() < maximo_pelotas:
                        pila4.insertar(pelota_en_juego)
                        pelota_en_juego = BLANCO
                        bandera = False
        pantalla.fill(BLANCO)
        dibujar_pila(pantalla,pila1)
        dibujar_pila(pantalla,pila2)
        dibujar_pila(pantalla,pila3)
        dibujar_pila(pantalla,pila4)
        pygame.draw.circle(pantalla,pelota_en_juego,[30,20],20)
        pygame.display.flip()

        reloj.tick(180)
    
    pygame.quit()

if __name__ == "__main__":
    main()