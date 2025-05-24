import pygame 
from Costants import WIDTH, HEIGHT, BG_WIDTH, WHITE, YELLOW, GRAY

def draw_background(screen, bg):
    bg = pygame.transform.scale(bg, (BG_WIDTH, bg.get_height())) 
    bg_sx = bg  
    bg_dx = pygame.transform.flip(bg, True, False)

    tile_width = bg.get_width()
    tile_height = bg.get_height()
    for y in range(0, HEIGHT, tile_height):
        screen.blit(bg_sx, (0, y))
        screen.blit(bg_dx, (WIDTH - BG_WIDTH, y))
    road_x = BG_WIDTH
    road_width = WIDTH - 2 * BG_WIDTH
    screen.fill(GRAY, (road_x, 0, road_width, HEIGHT))

def draw_lanes(screen, road_x, road_width):
    for i in range(1, 5):
        x = road_x + i * (road_width // 5)
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT), 2) 

def draw_points(screen, points): 
    points_font = pygame.font.SysFont(None, 40)     
    color = YELLOW if points >= 90 else WHITE
    text = points_font.render(f"{points:03}", True, color)

    lane_index = 1 
    lane_width = WIDTH // 5
    x = lane_index * lane_width + (lane_width - text.get_width()) // 2 + 20

    screen.blit(text, (x, 10))

def draw_speed(screen, enemy_speed):
    font_speed = pygame.font.SysFont(None, 30)
    speed = int(enemy_speed * 10)
    text = font_speed.render(f"{speed:03} Km/h", True, WHITE)
    x = WIDTH * 3 // 5 - 5  
    y = 10
    screen.blit(text, (x, y))