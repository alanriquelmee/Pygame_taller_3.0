import pygame
import random

# Inicialización de Pygame
# inicializa los modulos de los aspectos del juego, como la pantalla, sonido, eventos, etc.
pygame.init()

# Dimensiones de la ventana
ANCHO = 800
ALTO = 600

# Crear la ventana, toma una tupla que representa el tamaño de la ventana en pixeles
pantalla = pygame.display.set_mode((ANCHO, ALTO))
# establece el titulo que aparecera en la barra superior
pygame.display.set_caption("Juego Pygame con POO")


# Clase Jugador
class Jugador:
    # self.x = atributo de la clase
    # x valor que se le da al atributo
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.velocidad = 5


    #Eje X: Aumenta a la derecha y disminuye a la izquierda.
    #Eje Y: Aumenta hacia abajo y disminuye hacia arriba.
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
        #dibuja un rectangulo en la pantalla 
        # panalla es el objeto donde se dibuja el rectangulo
        #self.color es el color del rectangulo que se dibujara
        #self x ... posicion y tamaño del rectangulo 50x50 es el tamaño
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



# Crear objetos
jugador = Jugador(375, 275, (255, 0, 0))  # Jugador rojo en el centro
enemigo = Enemigo(100, 100, (0, 255, 0))  # Enemigo verde

# Bucle principal
corriendo = True
while corriendo:
    #eventos de la cola de eventos, cierre de ventana, pulsaciones, clicks.
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    
    # Obtener las teclas presionadas
    #Obtiene el estado de todas las teclas del teclado. Esta función devuelve una lista de valores (True o False), donde cada valor corresponde a si una tecla está presionada o no. Por ejemplo, si la tecla de flecha izquierda está presionada, el valor en la lista correspondiente a esa tecla será True.
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
    #Lo que hace esta condición es verificar si los dos rectángulos (el del jugador y el del enemigo) se superponen en alguna de las cuatro direcciones: izquierda, derecha, arriba o abajo. 
    if (jugador.x < enemigo.x + 50 and jugador.x + 50 > enemigo.x and
        jugador.y < enemigo.y + 50 and jugador.y + 50 > enemigo.y):
        print("¡Colisión!")
        corriendo = False  # Detener el juego en caso de colisión
    
    # Dibujar objetos en pantalla
    pantalla.fill((0, 0, 0))  # Fondo negro
    jugador.dibujar(pantalla)  # Dibujar el jugador
    enemigo.dibujar(pantalla)  # Dibujar el enemigo

    # Actualizar la pantalla, todo lo que se dibuja en el buffer se muestra en la ventana
    #El buffer es una zona de memoria donde se dibujan todos los objetos antes de mostrarse en la ventana
    pygame.display.flip()

# Finalizar Pygame
# Finaliza todos los módulos de Pygame y cierra cualquier recurso que esté usando
pygame.quit()


