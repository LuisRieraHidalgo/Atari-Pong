
import pygame
#Inicar pygames

clock = pygame.time.Clock()

import random

pygame.init()

fuente = pygame.font.Font(None, 36)
fuente_grande = pygame.font.Font(None,72)

pantalla = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Atari Pong")
import random
direcciones = [
    (5, 1),
    (5, 2),
    (5, 3),
    (5, -1),
    (5, -2),
    (5, -3),
    (-5, 1),
    (-5, 2),
    (-5, 3),
    (-5, -1),
    (-5, -2),
    (-5, -3)
]
#Variables

pelota_x = 400
pelota_y = 300

raqueta1_x = 30
raqueta1_y = 300

raqueta2_X = 760
raqueta2_Y = 300

raqueta_ancho = 20
raqueta_alto = 100

velocidad_x = 1
velocidad_y = -1

marcador_jugadoruno = 0
marcador_jugadordos = 0


ejecutando = True

while ejecutando:
    pantalla.fill((0, 0, 0 ))        
                 
    teclas = pygame.key.get_pressed()
#movimiento jugador 1
    if teclas[pygame.K_w] and raqueta1_y > 0:
        raqueta1_y = raqueta1_y - 5
    
    
    if teclas[pygame.K_s] and raqueta1_y < 500:
        raqueta1_y = raqueta1_y +5
#movimiento jugador 2
    if teclas[pygame.K_UP]  and raqueta2_Y > 0:       
        raqueta2_Y = raqueta2_Y -5

    if teclas[pygame.K_DOWN] and raqueta2_Y < 500:
        raqueta2_Y = raqueta2_Y + 5
#mostrar ganador 
    if marcador_jugadoruno >= 15:
       ejecutando = False

    if marcador_jugadordos >= 15:
       ejecutando = False
        
 #direccion de la pelota direcciones =
       
    texto_jugador1 = fuente.render(
    "J1: " + str(marcador_jugadoruno),
    True,
    (255,255,255)
    )

    texto_jugador2 = fuente.render(
    "J2: " + str(marcador_jugadordos),
    True,
    (255,255,255)
)

    pelota_x = pelota_x + velocidad_x
    pelota_y = pelota_y + velocidad_y

    if pelota_y <= 0:
        velocidad_y = 5
    if pelota_y >= 600:
        velocidad_y = -5
#Marcacion y reinicio de la pelota
    if pelota_x >= 800:
        marcador_jugadoruno = marcador_jugadoruno + 1
        pelota_x = 400
        pelota_y = 300
        direccion = random.choice(direcciones)
        velocidad_x = direccion[0]
        velocidad_y = direccion[1]
    if pelota_x <= 0 :
        marcador_jugadordos = marcador_jugadordos + 1
        pelota_x=400
        pelota_y=300
        direccion = random.choice(direcciones)
        velocidad_x = direccion[0]
        velocidad_y = direccion[1]
 

    #colison raqueta-pelota
    #raquetaizquierda
    if (pelota_x - 10 <= raqueta1_x + raqueta_ancho) and \
       (pelota_x - 10 >= raqueta1_x) and \
       (pelota_y >= raqueta1_y) and \
       (pelota_y <= raqueta1_y + raqueta_alto):

       velocidad_x = velocidad_x * -1
       pelota_x = raqueta1_x + raqueta_ancho + 10

    #raquetaderecha
    if (pelota_x + 10 >= raqueta2_X) and \
       (pelota_y >= raqueta2_Y) and \
       (pelota_y <= raqueta2_Y + raqueta_alto):

       velocidad_x = velocidad_x * -1

       pelota_x = raqueta2_X - 10
    
 

    
   

    pygame.draw.circle(
    pantalla,
    (255,255,255),
    (pelota_x, pelota_y),
    10
    )
    pygame.draw.line(
    pantalla,
    (255,255,255),
    (400,0),
    (400,600),
    3
    )

    pygame.draw.rect(
    pantalla,
    (255,255,255),
    (raqueta1_x, raqueta1_y, raqueta_ancho, raqueta_alto)
    )

    pygame.draw.rect(
    pantalla,
    (255,255,255),
    (raqueta2_X, raqueta2_Y, raqueta_ancho, raqueta_alto)
    )
    pantalla.blit(texto_jugador1, (150, 20))

    pantalla.blit(texto_jugador2, (560,20))

    clock.tick(60)

    pygame.display.update()

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            ejecutando = False
pygame.quit()