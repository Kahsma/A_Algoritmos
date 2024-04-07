import pprint
import pygame
import sys

def crear_tablero_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()

    # Obtener el tamaño del tablero
    tamano = int(lineas[0])
    tablero = [[0] * tamano for _ in range(tamano)]

    # Leer las coordenadas y tipos de perlas
    for linea in lineas[1:]:
        fila, columna, tipo_perla = map(int, linea.strip().split(','))
        tablero[fila-1][columna-1] = tipo_perla

    return tablero

def dibujar_tablero(screen, tablero, grid_size):    
    # Dibujar cuadrícula
    for x in range(len(tablero[0])):
        for y in range(len(tablero)):
            pygame.draw.rect(screen, NOTEBOOK_YELLOW, (x * grid_size, y * grid_size, grid_size, grid_size))
            pygame.draw.rect(screen, BLACK, (x * grid_size, y * grid_size, grid_size, grid_size), 1)

    # Dibujar elementos
    for y in range(len(tablero)):
        for x in range(len(tablero[y])):
            if tablero[y][x] == 1:  # Perla blanca
                pygame.draw.circle(screen, (255, 255, 255), ((x * grid_size) + (grid_size // 2), (y * grid_size) + (grid_size // 2)), 10)
            elif tablero[y][x] == 2:  # Perla negra
                pygame.draw.circle(screen, (0, 0, 0), ((x * grid_size) + (grid_size // 2), (y * grid_size) + (grid_size // 2)), 10)
            elif tablero[y][x] == 3:  # Línea
                pygame.draw.line(screen, (0, 0, 0), (x * grid_size + grid_size // 2, y * grid_size + grid_size // 2),
                                 ((x + 1) * grid_size, y * grid_size + grid_size // 2), 3)
            elif tablero[y][x] == 4:  # Perla blanca con línea
                pygame.draw.circle(screen, (255, 255, 255), ((x * grid_size) + (grid_size // 2), (y * grid_size) + (grid_size // 2)), 10)
                pygame.draw.line(screen, (0, 0, 0), (x * grid_size + grid_size // 2, y * grid_size + grid_size // 2),
                                 ((x + 1) * grid_size, y * grid_size + grid_size // 2), 3)
            elif tablero[y][x] == 5:  # Perla negra con línea
                pygame.draw.circle(screen, (0, 0, 0), ((x * grid_size) + (grid_size // 2), (y * grid_size) + (grid_size // 2)), 10)
                pygame.draw.line(screen, (0, 0, 0), (x * grid_size + grid_size // 2, y * grid_size + grid_size // 2),
                                 ((x + 1) * grid_size, y * grid_size + grid_size // 2), 3)
                
            # Verificar líneas adyacentes y conectarlas visualmente
            if tablero[y][x] == 3 or tablero[y][x] == 4 or tablero[y][x] == 5:  # Línea
                if x > 0 and tablero[y][x-1] == tablero[y][x]:  # Línea a la izquierda
                    pygame.draw.line(screen, (0, 0, 0), (x * grid_size + grid_size // 2, y * grid_size + grid_size // 2),
                                     ((x - 1) * grid_size + grid_size // 2, y * grid_size + grid_size // 2), 3)
                if y > 0 and tablero[y-1][x] == tablero[y][x]:  # Línea arriba
                    pygame.draw.line(screen, (0, 0, 0), (x * grid_size + grid_size // 2, y * grid_size + grid_size // 2),
                                     (x * grid_size + grid_size // 2, (y - 1) * grid_size + grid_size // 2), 3)




pygame.init()

# Constantes
WIDTH, HEIGHT = 600, 600
GRID_SIZE = WIDTH // 11  # Calculamos el tamaño de la cuadrícula en función del ancho de la pantalla y el tamaño del tablero
NOTEBOOK_YELLOW = (255, 219, 111)
BLACK = (0, 0, 0)

# Nombre del archivo de entrada
nombre_archivo = 'entrada.txt'

# Crear el tablero a partir del archivo
tablero = crear_tablero_desde_archivo(nombre_archivo)
pprint.pprint(tablero)
# Crear la ventana del juego
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tablero desde Archivo")

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Detección de clics
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Si se hace clic izquierdo
            pos = pygame.mouse.get_pos()
            x, y = pos[0] // GRID_SIZE, pos[1] // GRID_SIZE  # Convertir posición de pantalla a posición en la matriz
            if 0 <= x < len(tablero[0]) and 0 <= y < len(tablero):  # Verificar que la posición esté dentro del tablero
                if tablero[y][x] == 1:  # Si es una perla blanca
                    print("Clic en perla blanca en posición:", (x+1, y+1))
                    tablero[y][x] = 4  # Convertir perla blanca en perla blanca con línea
                elif tablero[y][x] == 2:  # Si es una perla negra
                    print("Clic en perla negra en posición:", (x+1, y+1))
                    tablero[y][x] = 5  # Convertir perla negra en perla negra con línea
                elif tablero[y][x] == 0:  # Si es una casilla vacía
                    print("Clic en casilla vacía en posición:", (x+1, y+1))
                    tablero[y][x] = 3  # Colocar el valor 4 en la casilla vacía para una perla blanca con línea
                elif tablero[y][x] == 3:  # Si es una línea
                    print("Clic en línea en posición:", (x+1, y+1))
                    tablero[y][x] = 0  # Eliminar la línea de la casilla
                    pprint.pprint(tablero)
                elif tablero[y][x] == 4:
                    print("Clic en perla blanca con línea en posición:", (x+1, y+1))
                    tablero[y][x] = 1
                elif tablero[y][x] == 5:
                    print("Clic en perla negra con línea en posición:", (x+1, y+1))
                    tablero[y][x] = 2

    screen.fill(NOTEBOOK_YELLOW)

    # Dibujar el tablero
    dibujar_tablero(screen, tablero, GRID_SIZE)
    

    pygame.display.flip()
