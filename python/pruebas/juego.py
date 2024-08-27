import pygame
import random
from pila_grafica import colaGrafica

NEGRO = (20,20,20)
BLANCO = (255,255,255)
VERDE = (0,255,0)
ROJO = (255,0,0)
AZUL = (0,0,255)

PELOTAS = 30

def main():

    pygame.init()

    dimensiones = [800,600]
    pantalla = pygame.display.set_mode(dimensiones)
    pygame.display.set_caption("Mete Bolas!!")
    
    cerrar = False
    reloj = pygame.time.Clock()

    pila1 = colaGrafica(10,60,80,1000)
    pila2 = colaGrafica(120,60,80,500) #rojo
    pila3 = colaGrafica(230,60,80,500) #verde
    pila4 = colaGrafica(340,60,80,500) #azul
    posx = 0
    posy = 0
    pelota_en_juego = NEGRO
    maximo_pelotas = 10
    bandera = False

    def que_color(valor):
        if valor ==0:
            color = AZUL
        elif valor == 1:
            color = VERDE
        elif valor == 2:
            color = ROJO
        return color

    def reiniciar():
        t = []
        for i in range(PELOTAS):
            t.append(i % 3)
        random.shuffle(t)

        for i in range(PELOTAS):
            color = que_color(t.pop(0))
            pila1.insertar(color)
            print(f'color {color} insertado en la cola')

    def dibujar_pila(pantalla, cola):

        pygame.draw.rect(pantalla, NEGRO,[cola.x1,cola.y1,cola.ancho,cola.alto],2)

        elementos = cola.elementos()
        ptemp = colaGrafica(cola.x1,cola.y1,cola.ancho,cola.alto)

        while not cola.cola_vacia():
            ptemp.insertar(cola.quitar())

        while not ptemp.cola_vacia():
            elementos = ptemp.elementos()
            pelota = ptemp.quitar()
            cola.insertar(pelota)
            if pelota:
                pygame.draw.circle(pantalla, pelota, [cola.x1+40,cola.y1+25+((elementos-1)*50)],20) 

    reiniciar()          
    print(f'instrucciones de uso')
    print(f'sobre la columna izquierda mete las pelotas rojas, sobre la columna del centro mete las pelotas verdes, sobre la columnda de la izquierda mete las pelotas azules')
    print(f'por favor presionar en la pelota negra para empezar el juego ')
    while not cerrar:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cerrar = True
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                posx = pos[0]
                posy = pos[1]
                if not bandera:
                    if posx >= pila1.x1 and posx < pila1.x1+pila1.ancho and pila1.elementos():
                        pelota_en_juego = pila1.quitar()
                        print(f'pelota en juego {pelota_en_juego}')
                        print(f'pelotas restantes en la cola {pila1.elementos()}')
                        if pila1.elementos() == 0:
                            print("Juego terminado")
                            cerrar = True
                        bandera = True
                else:
                    if posx >= pila1.x1 and posx < pila1.x1+pila1.ancho and pila1.elementos():
                        print(f'pelota devuelta a la pila1')
                        pila1.insertar(pelota_en_juego)
                        pelota_en_juego = BLANCO
                        bandera = False 

                    if posx >= pila2.x1 and posx < pila2.x1+pila2.ancho and pila2.elementos() < maximo_pelotas:
                        if pelota_en_juego == ROJO:
                            pila2.insertar(pelota_en_juego)
                            print(f'pelota insertada correctamente')
                            bandera = False
                        else:
                            print(f'error al insertar pelota en pila ROJO')
                       
                    elif posx >= pila3.x1 and posx < pila3.x1+pila3.ancho and pila3.elementos() < maximo_pelotas:
                        if pelota_en_juego == VERDE:
                            pila3.insertar(pelota_en_juego)
                            print(f'pelota insertada correctamente')
                            bandera = False
                        else:
                            print(f'error al insertar pelota en pila VERDE')
                    elif posx >= pila4.x1 and posx < pila4.x1+pila4.ancho and pila4.elementos() < maximo_pelotas:
                        if pelota_en_juego == AZUL:
                            pila4.insertar(pelota_en_juego)
                            print(f'pelota insertada correctamente')  
                            bandera = False
                        else:
                            print(f'error al insertar pelota en pila AZUL')
        pantalla.fill(BLANCO)
        
        dibujar_pila(pantalla,pila2)
        dibujar_pila(pantalla,pila3)
        dibujar_pila(pantalla,pila4)

        if pelota_en_juego != None:
            pygame.draw.circle(pantalla, pelota_en_juego,[50,20],20) 

        pygame.display.flip()
        reloj.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()