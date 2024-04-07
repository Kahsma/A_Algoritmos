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
                    
                elif tablero[y][x] == 2:  # Si es una perla negra
                    print("Clic en perla negra en posición:", (x+1, y+1))
                    
                elif tablero[y][x] == 0:  # Si es una casilla vacía
                    print("Clic en casilla vacía en posición:", (x+1, y+1))
                    if casilla_seleccionada is not None:  # Verificar si hay una casilla seleccionada
                        # Realizar la acción correspondiente según la casilla seleccionada
                        tablero[casilla_seleccionada[1]][casilla_seleccionada[0]] = 3  # Colocar línea en la casilla seleccionada
                        casilla_seleccionada = None  # Desmarcar la casilla seleccionada
                    else:
                        casilla_seleccionada = (x, y)  # Marcar la casilla como seleccionada
                elif tablero[y][x] == 3:  # Si es una línea
                    print("Clic en línea en posición:", (x+1, y+1))
                    tablero[y][x]
