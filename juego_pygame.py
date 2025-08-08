import pygame
import random

# Inicialización de Pygame
pygame.init()

# Dimensiones de la ventana
ANCHO = 800
ALTO = 600

# Clase Jugador
class Jugador:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.velocidad = 5

    def mover(self, direccion):
        if direccion == "izquierda":
            self.x -= self.velocidad
        elif direccion == "derecha":
            self.x += self.velocidad
        elif direccion == "arriba":
            self.y -= self.velocidad
        elif direccion == "abajo":
            self.y += self.velocidad

        # Limitar el movimiento dentro de los límites de la ventana
        if self.x < 0:
            self.x = 0
        elif self.x > ANCHO - 50:  # 50 es el tamaño del jugador
            self.x = ANCHO - 50

        if self.y < 0:
            self.y = 0
        elif self.y > ALTO - 50:  # 50 es el tamaño del jugador
            self.y = ALTO - 50

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.x, self.y, 50, 50))

# Clase Enemigo
class Enemigo:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.velocidad = 3

    def mover(self):
        self.x += random.choice([-self.velocidad, self.velocidad])
        self.y += random.choice([-self.velocidad, self.velocidad])

        # Limitar el movimiento dentro de los límites de la ventana
        if self.x < 0:
            self.x = 0
        elif self.x > ANCHO - 50:  # 50 es el tamaño del enemigo
            self.x = ANCHO - 50

        if self.y < 0:
            self.y = 0
        elif self.y > ALTO - 50:  # 50 es el tamaño del enemigo
            self.y = ALTO - 50

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.x, self.y, 50, 50))

# Crear la ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego Pygame con POO")

# Crear objetos
jugador = Jugador(375, 275, (255, 0, 0))  # Jugador rojo en el centro
enemigo = Enemigo(100, 100, (0, 255, 0))  # Enemigo verde

# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    
    # Obtener las teclas presionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jugador.mover("izquierda")
    if teclas[pygame.K_RIGHT]:
        jugador.mover("derecha")
    if teclas[pygame.K_UP]:
        jugador.mover("arriba")
    if teclas[pygame.K_DOWN]:
        jugador.mover("abajo")
    
    # Mover el enemigo
    enemigo.mover()
    

    # Detectar colisiones
    if (jugador.x < enemigo.x + 50 and jugador.x + 50 > enemigo.x and
        jugador.y < enemigo.y + 50 and jugador.y + 50 > enemigo.y):
        print("¡Colisión!")
        corriendo = False  # Detener el juego en caso de colisión
    
    # Dibujar objetos en pantalla
    pantalla.fill((0, 0, 0))  # Fondo negro
    jugador.dibujar(pantalla)  # Dibujar el jugador
    enemigo.dibujar(pantalla)  # Dibujar el enemigo

    # Actualizar la pantalla
    pygame.display.flip()

# Finalizar Pygame
pygame.quit()
