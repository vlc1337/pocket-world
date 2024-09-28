import pygame

pygame.init()
width = 600
height = 400
cell_size = 20
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pixel World")

black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

grass = pygame.image.load("img/grass.png").convert_alpha()
water = pygame.image.load("img/water.png").convert_alpha()
soil = pygame.image.load("img/soil.png").convert_alpha()
shovel = pygame.image.load("img/shovel.png").convert_alpha()
grass = pygame.transform.scale(grass, (cell_size, cell_size))
water = pygame.transform.scale(water, (cell_size, cell_size))
soil = pygame.transform.scale(soil, (cell_size, cell_size))
shovel = pygame.transform.scale(shovel, (cell_size, cell_size))

images = [grass, shovel, water]
selected_image = images[0]
panel_height = 50
panel_width = width
button_width = cell_size
grid = [[None for _ in range(width // cell_size)] for _ in range(height // cell_size)]
hovered_cell = None
mouse_pressed = False
for y in range(height // cell_size):
    for x in range(width // cell_size):
        grid[y][x] = water

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[1] >= height - panel_height:
                if event.pos[0] < button_width:
                    selected_image = images[0]
                elif event.pos[0] < button_width * 2:
                    selected_image = images[1]
                elif event.pos[0] < button_width * 3 and event.pos[0] > button_width * 2:
                    selected_image = images[2]
            else:
                cell_x = event.pos[0] // cell_size
                cell_y = event.pos[1] // cell_size
                if 0 <= x < width // cell_size and 0 <= y < height // cell_size:
                    if 0 <= x < width // cell_size and 0 <= y < height // cell_size and grid[y][x] == grass and selected_image == shovel:
                        grid[y][x] = soil
                    if selected_image != shovel:
                        grid[y][x] = selected_image
            mouse_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pressed = False
        elif event.type == pygame.MOUSEMOTION:
            cell_x = event.pos[0] // cell_size
            cell_y = event.pos[1] // cell_size
            hovered_cell = (cell_x, cell_y) if event.pos[1] < height - panel_height else None
    screen.fill(white)

    for y, row in enumerate(grid):
        for x, image in enumerate(row):
            screen.blit(image, (x * cell_size, y * cell_size))

    if hovered_cell is not None and mouse_pressed:
        x, y = hovered_cell
        pygame.draw.rect(screen, yellow, (x * cell_size, y * cell_size, cell_size, cell_size), 2)
        if 0 <= x < width // cell_size and 0 <= y < height // cell_size:
            if 0 <= x < width // cell_size and 0 <= y < height // cell_size and grid[y][x] == grass and selected_image == shovel:
                grid[y][x] = soil
            if selected_image != shovel:
                grid[y][x] = selected_image
        screen.blit(selected_image, (x * cell_size, y * cell_size))

    pygame.draw.rect(screen, black, (0, height - panel_height, panel_width, panel_height))

    screen.blit(grass, (3, height - panel_height))
    screen.blit(shovel, (23, height - panel_height))
    screen.blit(water, (43, height - panel_height))
    if selected_image == grass:
        pygame.draw.rect(screen, yellow, (3, height - panel_height, button_width, button_width), 3)
    elif selected_image == shovel:
        pygame.draw.rect(screen, yellow, (23, height - panel_height, button_width, button_width), 3)
    elif selected_image == water:
        pygame.draw.rect(screen, yellow, (43, height - panel_height, button_width, button_width), 3)

    pygame.draw.rect(screen, yellow, (0, height - panel_height, panel_width, panel_height), 3)

    if hovered_cell is not None:
        x, y = hovered_cell
        pygame.draw.rect(screen, yellow, (x * cell_size, y * cell_size, cell_size, cell_size), 3)
    pygame.display.flip()

pygame.quit()