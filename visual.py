import pygame

pygame.init()
pygame.font.init()

FPS = 60

WIDTH, HEIGHT = 900, 900

ROWS, COLS = 10, 10

SQUARE_HEIGHT = HEIGHT // ROWS
SQUARE_WIDTH = WIDTH // COLS

OUTLINE_COLOR = (46, 139, 87)
OUTLINE_THICKNESS = 6
BACKGROUND_COLOR = (135, 206, 235)
FONT_COLOR = (0,0,0)

FONT = pygame.font.SysFont("comicsans", 60, bold=True)
MOVE_VEL = 20

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Piotr Bekier s198173")

def mouse_click_coordinates(position):
    x, y = position

    return (x * COLS // WIDTH, y * ROWS // HEIGHT)

def To_window_cordinates(position):
    x, y = position

    OFFSET = (SQUARE_WIDTH // 2, SQUARE_HEIGHT // 2)

    return (x * SQUARE_WIDTH + OFFSET[0], y * SQUARE_HEIGHT + OFFSET[1])

def draw_grid(window):
    for row in range(1, ROWS):
        y = row * SQUARE_HEIGHT
        pygame.draw.line(window, OUTLINE_COLOR, (0, y), (WIDTH, y), OUTLINE_THICKNESS)

    for col in range(1, COLS):
        x = col * SQUARE_WIDTH
        pygame.draw.line(window, OUTLINE_COLOR, (x, 0), (x, HEIGHT), OUTLINE_THICKNESS)

    pygame.draw.rect(window, OUTLINE_COLOR, (0,0, WIDTH, HEIGHT), OUTLINE_THICKNESS)

def draw(window):
    window.fill(BACKGROUND_COLOR)
    draw_grid(window)
    pygame.display.update()

def function(window):
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_coordinates = mouse_click_coordinates(pygame.mouse.get_pos())
                print(f'x: {mouse_coordinates[0]}\t y: {mouse_coordinates[1]}', end="\t\t")
                window_coordinates = To_window_cordinates(mouse_coordinates)
                print(f'x: {window_coordinates[0]}\t y: {window_coordinates[1]}')
                text = FONT.render("W", 1, FONT_COLOR)
                text_rect = text.get_rect(center=window_coordinates)
                window.blit(text, text_rect)
                pygame.display.update()
            else:
                draw(window)

    pygame.quit()


function(WINDOW)