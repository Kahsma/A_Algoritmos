import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Masyu Game")

# Load data from entrada.txt
board_data = []
with open("entrada.txt", "r") as file:
    for line in file:
        row = line.strip().split()
        board_data.append(row)

# Calculate the size of each cell
num_rows = int(board_data[0][0])
num_cols = int(board_data[0][1])
cell_width = window_width // num_cols
cell_height = window_height // num_rows

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic

    # Render graphics
    window.fill((255, 255, 255))  # Fill the window with white color

    # Draw the board
    for row in range(num_rows):
        for col in range(num_cols):
            cell_type = int(board_data[row + 1][col + 1])
            if cell_type == 1:
                color = (255, 255, 255)  # White pearl
            elif cell_type == 2:
                color = (0, 0, 0)  # Black pearl
            else:
                color = (0, 0, 0)  # Default color for other cells
            pygame.draw.rect(window, color, (col * cell_width, row * cell_height, cell_width, cell_height))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()