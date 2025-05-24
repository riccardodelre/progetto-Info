import pygame
import sys 
from Game_over import end_screen 
from Menu import menu 
from Enemies import spawn_enemy, draw_enemy 
from Players import Player 
from Draw import draw_background, draw_lanes, draw_points 
from Costants import WIDTH, HEIGHT, FPS, CAR_WIDTH, CAR_HEIGHT, BG_WIDTH, MAX_POINTS, ACCELERATION, ENEMY_SPAWN_RATE

# Inizializza pygame
pygame.init()  

# Schermo
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gioco della Macchinina")

# Clock
clock = pygame.time.Clock()

# Macchinina del giocatore
player_lane = 2
road_x = BG_WIDTH 
road_width = WIDTH - 2 * BG_WIDTH
player_x = road_x + player_lane * (road_width // 5) + ((road_width // 5) - CAR_WIDTH) // 2
player_y = HEIGHT - CAR_HEIGHT - 20

# Altri veicoli
enemy_cars = []
enemy_timer = 0

# Menù
player_image, bg, enemy_speed, max_speed, player_speed, enemy_delay = menu( screen) 

# Player
player = Player(player_image, player_x, player_y, player_speed) 

#Vittoria
Win = True

# Main loop
cicles = 0
points = 0
running = True

while running:
    cicles += 1
    if cicles % ENEMY_SPAWN_RATE == 0:
        points += 1
    
    draw_background(screen, bg)

    # Eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            Win = False
            pygame.quit()
            sys.exit()

    # Input
    keys = pygame.key.get_pressed()
    player.move(keys) 

    # Spawning nemici
    enemy_timer += 1
    if enemy_timer >= enemy_delay:
        spawn_enemy(road_x, road_width, enemy_cars)
        enemy_timer = 0

    # Muovi nemici
    for enemy in enemy_cars:
        enemy[1] += enemy_speed

    #Rimuovi nemici fuori dallo schermo
    enemy_cars = [e for e in enemy_cars if e[1] < HEIGHT]

    # Controllo collisioni
    if player.check_collision(enemy_cars):
        running = False
        Win = False

    # Disegna corsie
    draw_lanes(screen, road_x, road_width)

    # Disegna tutto
    player.draw(screen)
    for ex, ey, img in enemy_cars:
        draw_enemy(screen, ex, ey, img) 

    # Aggiorna la velocità
    if enemy_speed < max_speed:
        enemy_speed += ACCELERATION 
    
    #Disegna punti
    draw_points(screen, points)

    #Controlla Vittoria
    if points == MAX_POINTS:
        running = False
    
    pygame.display.flip()
    clock.tick(FPS) 

# Mostra schermata finale
end_screen(screen, points, Win)

pygame.quit()
sys.exit()