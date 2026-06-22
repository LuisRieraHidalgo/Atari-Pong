
import pygame
#Inicar pygames

clock = pygame.time.Clock()


pygame.init()

fuente = pygame.font.Font(None, 36)

pantalla = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Atari Pong")
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
    print("limpiando")               

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

    if pelota_x >= 800:
        marcador_jugadoruno = marcador_jugadoruno + 1
        pelota_x = 400
        pelota_y = 300

   

    pygame.draw.circle(
    pantalla,
    (255,255,255),
    (pelota_x, pelota_y),
    10
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
    pantalla.blit(texto_jugador1, (50, 50))

    pantalla.blit(texto_jugador2, (650,50))

    clock.tick(60)

    pygame.display.update()

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            ejecutando = False

pygame.quit()