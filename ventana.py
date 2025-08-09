import pygame
import sys

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ventana negra - Pygame")

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Clic en la X de la ventana
            pygame.quit()
            sys.exit()

    # Rellenar pantalla de negro
    pantalla.fill((0, 0, 0))

    # Actualizar pantalla
    pygame.display.flip()
    

# Pseudocódigo súper simple:

# Abrir el juego y mostrar una ventana negra.

# Crear un jugador (cuadrado rojo) y un enemigo (cuadrado verde).

# Mientras el juego esté encendido:

# Revisar si el jugador quiere cerrar la ventana.

# Revisar si el jugador presiona las flechas para moverse.

# Mover al enemigo en una dirección aleatoria.

# Ver si el jugador choca con el enemigo.

# Si choca, mostrar “Colisión” y cerrar el juego.

# Dibujar el fondo negro.

# Dibujar al jugador y al enemigo en sus posiciones.

# Actualizar la pantalla para que se vean los cambios.

# Cerrar el juego.