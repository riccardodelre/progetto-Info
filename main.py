import pygame
import random
import sys


pygame.init()


WIDTH, HEIGHT = 500, 700
LANE_WIDTH = WIDTH // 5
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gioco della Macchinina")


WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
RED = (200, 0, 0)
BLUE = (0, 0, 200)


clock = pygame.time.Clock()
FPS = 60

car_width, car_height = 40, 80
player_lane = 2
player_x = player_lane * LANE_WIDTH + (LANE_WIDTH - car_width) // 2
player_y = HEIGHT - car_height - 20
player_speed = 5

enemy_cars = []
enemy_timer = 0
enemy_delay = 40
enemy_speed = 5

def draw_player(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, car_width, car_height))

def draw_enemy(x, y):
    pygame.draw.rect(screen, RED, (x, y, car_width, car_height))

def spawn_enemy():
    lane = random.randint(0, 4)
    x = lane * LANE_WIDTH + (LANE_WIDTH - car_width) // 2
    y = -car_height
    enemy_cars.append([x, y])

def check_collision(px, py):
    player_rect = pygame.Rect(px, py, car_width, car_height)
    for ex, ey in enemy_cars:
        enemy_rect = pygame.Rect(ex, ey, car_width, car_height)
        if player_rect.colliderect(enemy_rect):
            return True
    return False

def is_out_of_bounds(px):
    return px < 0 or px + car_width > WIDTH

running = True
while running:
    screen.fill(GRAY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    enemy_timer += 1
    if enemy_timer >= enemy_delay:
        spawn_enemy()
        enemy_timer = 0

    for enemy in enemy_cars:
        enemy[1] += enemy_speed

    enemy_cars = [e for e in enemy_cars if e[1] < HEIGHT]

    if check_collision(player_x, player_y) or is_out_of_bounds(player_x):
        print("Game Over")
        pygame.quit()
        sys.exit()

    for i in range(1, 5):
        pygame.draw.line(screen, WHITE, (i * LANE_WIDTH, 0), (i * LANE_WIDTH, HEIGHT), 2)

    draw_player(player_x, player_y)
    for ex, ey in enemy_cars:
        draw_enemy(ex, ey)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()