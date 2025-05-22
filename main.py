import pygame
import random
import sys

# Inizializza pygame
pygame.init()  

# Schermo
WIDTH, HEIGHT = 600, 700
LANE_WIDTH = WIDTH // 5
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gioco della Macchinina")

player_images = [
    pygame.image.load("5_player.png").convert_alpha(),
    pygame.image.load("1_player.png").convert_alpha(),
    pygame.image.load("3_player.png").convert_alpha(),
    pygame.image.load("4_player.png").convert_alpha(),
    pygame.image.load("2_player.png").convert_alpha()
]
enemy_images = [
    pygame.image.load("1_blu.png").convert_alpha(),
    pygame.image.load("1_rosso.png").convert_alpha(),
    pygame.image.load("1_verde.png").convert_alpha(),
    pygame.image.load("2_blu.png").convert_alpha(),
    pygame.image.load("2_rosso.png").convert_alpha(),
    pygame.image.load("2_verde.png").convert_alpha(),
    pygame.image.load("3_blu.png").convert_alpha(),
    pygame.image.load("3_rosso.png").convert_alpha(),
    pygame.image.load("3_verde.png").convert_alpha(),
    pygame.image.load("4_blu.png").convert_alpha(),
    pygame.image.load("4_rosso.png").convert_alpha(),
    pygame.image.load("4_verde.png").convert_alpha(),
    pygame.image.load("5_blu.png").convert_alpha(),
    pygame.image.load("5_rosso.png").convert_alpha(),
    pygame.image.load("5_verde.png").convert_alpha(),
]

bgs = [pygame.image.load("erba_fiori.png").convert_alpha(),
      pygame.image.load("erba_verde.png").convert_alpha(),
      pygame.image.load("erba_marrone.png").convert_alpha(),
      pygame.image.load("erba_rossa.png").convert_alpha(),
      pygame.image.load("erba_gialla.png").convert_alpha()
]

# Colori
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
RED = (200, 0, 0)
BLUE = (0, 0, 200)

# Clock
clock = pygame.time.Clock()
FPS = 60

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

player_images = [pygame.transform.scale(img, (car_width, car_height)) for img in player_images]

player_image  = random.choice(player_images)     
enemy_images = [pygame.transform.scale(img, (car_width, car_height)) for img in enemy_images]

def draw_player(x, y, image):
    screen.blit(image, (x, y))

def draw_enemy(x, y, image):
    screen.blit(image, (x, y))

def spawn_enemy():
    lane = random.randint(0, 4)
    x = road_x + lane * (road_width // 5) + ((road_width // 5) - car_width) // 2
    y = -car_height
    image = random.choice(enemy_images)
    enemy_cars.append([x, y, image])

def check_collision(px, py):
    player_rect = pygame.Rect(px, py, car_width, car_height)
    for ex, ey, _ in enemy_cars:
        enemy_rect = pygame.Rect(ex, ey, car_width, car_height)
        if player_rect.colliderect(enemy_rect):
            return True
    return False

def is_out_of_bounds(px):
    return px < bg_width or px + car_width > (WIDTH-bg_width) 

# Font per il testo
title_font = pygame.font.SysFont(None, 60)      # Font grande per "MENU PRINCIPALE"
subtitle_font = pygame.font.SysFont(None, 36)   # fon per "Scegli la tua macchina"
name_font = pygame.font.SysFont(None, 28)       # font per i nomi delle macchine

#Difficoltà delle auto
car_diff = ["Molto Facile", "Facile", "Media", "Difficile", "Molto Difficile"]

# Menù principale (selezione macchina)
selected_index = 0
selecting = True

while selecting:
    screen.fill((30, 30, 30)) 
    
    main_title = title_font.render("MENU PRINCIPALE", True, RED)
    screen.blit(main_title, (WIDTH // 2 - main_title.get_width() // 2, 30))

    title_text = subtitle_font.render("Scegli la tua macchina:   Invio per confermare", True, WHITE)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))

    selected_image = player_images[selected_index]
    image_x = WIDTH // 2 - car_width // 2
    image_y = HEIGHT // 2 - car_height // 2

    car_diff_text = name_font.render(car_diff[selected_index], True, WHITE)
    screen.blit(car_diff_text, (WIDTH // 2 - car_diff_text.get_width() // 2, image_y + car_height + 15))

    pygame.draw.rect(screen, WHITE, (image_x - 5, image_y - 5, car_width + 10, car_height + 10), 2)

    screen.blit(selected_image, (image_x, image_y))

    pygame.display.flip()

    # Eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                selected_index = (selected_index - 1) % len(player_images)
            if event.key == pygame.K_RIGHT:
                selected_index = (selected_index + 1) % len(player_images)
            if event.key == pygame.K_RETURN:
                player_image = player_images[selected_index]
                
                if selected_index == 0:  # Molto facile
                    enemy_speed, max_speed, player_speed, enemy_delay  = 5, 8, 3, 40

                elif selected_index == 1:  # Facile
                    enemy_speed, max_speed, player_speed, enemy_delay  = 7, 10, 4.5, 40

                elif selected_index == 2:  # Media
                    enemy_speed, max_speed, player_speed, enemy_delay  = 9, 12, 6, 30

                elif selected_index == 3:  # Difficile
                    enemy_speed, max_speed, player_speed, enemy_delay  = 11, 14, 7.5, 30

                else:  # Molto difficile
                    enemy_speed, max_speed, player_speed, enemy_delay  = 13, 16, 9, 20

                bg = bgs[selected_index]

                selecting = False

bg = pygame.transform.scale(bg, (bg_width, bg.get_height()))  # solo in larghezza
bg_sx = bg  # non scalare in altezza
bg_dx = pygame.transform.flip(bg, True, False)

# Main loop
running = True
while running:
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

    # Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Spawning nemici
    enemy_timer += 1
    if enemy_timer >= enemy_delay:
        spawn_enemy()
        enemy_timer = 0

    # Muovi nemici
    for enemy in enemy_cars:
        enemy[1] += enemy_speed

    # Rimuovi nemici fuori dallo schermo
    enemy_cars = [e for e in enemy_cars if e[1] < HEIGHT]

    # Collisione
    if check_collision(player_x, player_y) or is_out_of_bounds(player_x):
        print("Game Over")
        pygame.quit()
        sys.exit()

    # Disegna corsie
    for i in range(1, 5):
        x = road_x + i * (road_width // 5)
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT), 2)

    # Disegna tutto
    draw_player(player_x, player_y, player_image) 
    for ex, ey, img in enemy_cars:
        draw_enemy(ex, ey, img) 

    # Aggiorna la velocità
    if enemy_speed < max_speed:
        enemy_speed += 0.005 

    pygame.display.flip()
    clock.tick(FPS) 

pygame.quit()