import pygame
import random
import sys

# Inizializza pygame
pygame.init()  

# Schermo
WIDTH, HEIGHT = 500, 700
LANE_WIDTH = WIDTH // 5
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gioco della Macchinina")

player_images = [
    pygame.image.load("1_player.png").convert_alpha(),
    pygame.image.load("2_player.png").convert_alpha(),
    pygame.image.load("3_player.png").convert_alpha(),
    pygame.image.load("4_player.png").convert_alpha(),
    pygame.image.load("5_player.png").convert_alpha(),
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
# Colori
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
RED = (200, 0, 0)
BLUE = (0, 0, 200)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Macchinina del giocatore
car_width, car_height = 45, 90 
player_lane = 2
player_x = player_lane * LANE_WIDTH + (LANE_WIDTH - car_width) // 2
player_y = HEIGHT - car_height - 20
player_speed = 7 

player_images = [pygame.transform.scale(img, (car_width, car_height)) for img in player_images]

player_image  = random.choice(player_images)     
enemy_images = [pygame.transform.scale(img, (car_width, car_height)) for img in enemy_images]

# Altri veicoli
enemy_cars = []
enemy_timer = 0
enemy_delay = 40
enemy_speed = 5

def draw_player(x, y, image):
    screen.blit(image, (x, y))

def draw_enemy(x, y, image):
    screen.blit(image, (x, y))

def spawn_enemy():
    lane = random.randint(0, 4)
    x = lane * LANE_WIDTH + (LANE_WIDTH - car_width) // 2
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
    return px < 0 or px + car_width > WIDTH 

# Selezione macchina
selected_index = 0
selecting = True

while selecting:
    screen.fill(GRAY)

    # Mostra macchina selezionata al centro
    selected_image = player_images[selected_index]
    screen.blit(selected_image, (WIDTH // 2 - car_width // 2, HEIGHT // 2 - car_height // 2))

    pygame.display.flip()

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
                selecting = False

# Main loop
running = True
while running:
    screen.fill(GRAY)

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
        pygame.draw.line(screen, WHITE, (i * LANE_WIDTH, 0), (i * LANE_WIDTH, HEIGHT), 2)

    # Disegna tutto
    draw_player(player_x, player_y, player_image) 
    for ex, ey, img in enemy_cars:
        draw_enemy(ex, ey, img)

    pygame.display.flip()
    clock.tick(FPS) 

pygame.quit()