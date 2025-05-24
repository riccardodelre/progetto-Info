import pygame 

YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

def draw_background(screen, bg, bg_width, WIDTH, HEIGHT):
    bg = pygame.transform.scale(bg, (bg_width, bg.get_height())) 
    bg_sx = bg  
    bg_dx = pygame.transform.flip(bg, True, False)

    GRAY = (50, 50, 50)
    
    tile_width = bg.get_width()
    tile_height = bg.get_height()
    for y in range(0, HEIGHT, tile_height):
        screen.blit(bg_sx, (0, y))
        screen.blit(bg_dx, (WIDTH - bg_width, y))
    road_x = bg_width
    road_width = WIDTH - 2 * bg_width
    screen.fill(GRAY, (road_x, 0, road_width, HEIGHT))

def draw_lanes(screen, road_x, road_width, height):
    for i in range(1, 5):
        x = road_x + i * (road_width // 5)
        pygame.draw.line(screen, WHITE, (x, 0), (x, height), 2) 

def draw_points(screen, points, width): 
    points_font = pygame.font.SysFont(None, 40)     
    color = YELLOW if points >= 90 else WHITE
    text = points_font.render(f"{points:03}", True, color)
    screen.blit(text, (width // 2 - text.get_width() // 2, 10))