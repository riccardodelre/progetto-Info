import pygame
import sys 
from Game_over import end_screen 
from Menu import menu 
from Enemies import spawn_enemy, draw_enemy 
from Players import Player

# Inizializza pygame
pygame.init()  

# Schermo
WIDTH, HEIGHT = 600, 700
LANE_WIDTH = WIDTH // 5
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gioco della Macchinina")

# Clock
clock = pygame.time.Clock()
FPS = 60

# Colori
GRAY = (50, 50, 50)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Macchinina del giocatore
bg_width = 50
car_width, car_height = 50, 100 
player_lane = 2
road_x = bg_width 
road_width = WIDTH - 2 * bg_width
player_x = road_x + player_lane * (road_width // 5) + ((road_width // 5) - car_width) // 2
player_y = HEIGHT - car_height - 20

# Altri veicoli
enemy_cars = []
enemy_timer = 0
enemy_delay = 30 

# Menù
player_image, bg, enemy_speed, max_speed, player_speed, enemy_delay = menu( screen, WIDTH, HEIGHT) 

# Player
player = Player(player_image, player_x, player_y, player_speed, car_width, car_height)

bg = pygame.transform.scale(bg, (bg_width, bg.get_height()))  # solo in larghezza
bg_sx = bg  
bg_dx = pygame.transform.flip(bg, True, False) 

points_font = pygame.font.SysFont(None, 40)     #Font per i punti 

#Vittoria
Win = True

# Main loop
cicles = 0
points = 0
running = True

while running:
    cicles += 1
    if cicles % 35 == 0:
        points += 1
    tile_width = bg_sx.get_width()
    tile_height = bg_sx.get_height()

    for y in range(0, HEIGHT, tile_height):
        screen.blit(bg_sx, (0, y))  # sinistra
        screen.blit(bg_dx, (WIDTH - bg_width, y))  # destra

    road_x = bg_width
    road_width = WIDTH - 2 * bg_width
    screen.fill(GRAY, (road_x, 0, road_width, HEIGHT))

    # Eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            Win = False
            pygame.quit()
            sys.exit()

    # Input
    keys = pygame.key.get_pressed()
    player.move(keys, bg_width, WIDTH) 

    # Spawning nemici
    enemy_timer += 1
    if enemy_timer >= enemy_delay:
        spawn_enemy(road_x, road_width, car_width, car_height, enemy_cars)
        enemy_timer = 0

    # Muovi nemici
    for enemy in enemy_cars:
        enemy[1] += enemy_speed

    # Rimuovi nemici fuori dallo schermo
    enemy_cars = [e for e in enemy_cars if e[1] < HEIGHT]

    # Controlla collisioni
    if player.check_collision(enemy_cars):
        running = False
        Win = False

    # Disegna corsie
    for i in range(1, 5):
        x = road_x + i * (road_width // 5)
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT), 2)

    # Disegna tutto
    player.draw(screen)
    for ex, ey, img in enemy_cars:
        draw_enemy(screen, ex, ey, img) 

    # Aggiorna la velocità
    if enemy_speed < max_speed:
        enemy_speed += 0.005 
    
    #Disegna punti
    if points >= 90:
        points_text = points_font.render(f"{points:03}", True, YELLOW)
    else:
        points_text = points_font.render(f"{points:03}", True, WHITE)
    
    screen.blit(points_text, (WIDTH // 2 - points_text.get_width() // 2, 10))

    #Controlla Vittoria
    if points == 100:
        running = False
    
    pygame.display.flip()
    clock.tick(FPS) 

# Mostra schermata finale
end_screen(screen, points, Win, WIDTH, HEIGHT)

pygame.quit()
sys.exit()