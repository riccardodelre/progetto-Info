import pygame
from Costants import BG_WIDTH, WIDTH, CAR_WIDTH, CAR_HEIGHT

class Player:
    def __init__(self, image, x, y, speed):
        self.image = image
        self.x = x
        self.y = y
        self.speed = speed
        self.car_width = CAR_WIDTH
        self.car_height = CAR_HEIGHT

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > BG_WIDTH:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x + self.car_width < WIDTH - BG_WIDTH:
            self.x += self.speed 

        left_limit = BG_WIDTH
        right_limit = WIDTH - BG_WIDTH - self.car_width

        if self.x < left_limit or self.x > right_limit:
            return True  

        return False

    def check_collision(self, enemy_cars):
        player_rect = pygame.Rect(self.x, self.y, self.car_width, self.car_height)
        for ex, ey, _ in enemy_cars:
            enemy_rect = pygame.Rect(ex, ey, self.car_width, self.car_height)
            if player_rect.colliderect(enemy_rect):
                return True
        return False