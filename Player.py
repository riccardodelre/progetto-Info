import pygame

def draw_player(x, y, image, screen):
    screen.blit(image, (x, y))

def check_collision(px, py, enemy_cars, car_width, car_height):
    player_rect = pygame.Rect(px, py, car_width, car_height)
    for ex, ey, _ in enemy_cars:
        enemy_rect = pygame.Rect(ex, ey, car_width, car_height)
        if player_rect.colliderect(enemy_rect):
            return True
    return False

def is_out_of_bounds(px, bg_width, width, car_width):
    return px < bg_width or px + car_width > (width - bg_width)