import pygame
import random
from Costants import CAR_WIDTH, CAR_HEIGHT, HEIGHT

def spawn_enemy(road_x, road_width, enemy_cars):
    
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
    enemy_images = [pygame.transform.scale(img, (CAR_WIDTH, CAR_HEIGHT)) for img in enemy_images]

    lane = random.randint(0, 4)
    x = road_x + lane * (road_width // 5) + ((road_width // 5) - CAR_WIDTH) // 2
    y = -CAR_HEIGHT
    image = random.choice(enemy_images)
    enemy_cars.append([x, y, image])

def draw_enemy(screen, x, y, image):
    screen.blit(image, (x, y))

def update_enemies(enemy_cars, enemy_speed):
    for enemy in enemy_cars:
        enemy[1] += enemy_speed
    return [e for e in enemy_cars if e[1] < HEIGHT]