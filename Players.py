import pygame
from Costants import BG_WIDTH, WIDTH, CAR_WIDTH, CAR_HEIGHT

class Player:
    def __init__(self, image, x, y, speed):
        self.image = image
        self.x = x
        self.y = y
        self.speed = speed
        self.car_width = image.get_width()
        self.car_height = image.get_height()

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        if self.x < BG_WIDTH or self.x + self.car_width > WIDTH - BG_WIDTH:
            return True 

        return False

    def check_collision(self, enemy_cars):
        player_rect = pygame.Rect(self.x, self.y, self.car_width, self.car_height)

        for ex, ey, _ in enemy_cars:
            enemy_rect = pygame.Rect(ex, ey, self.car_width, self.car_height)
            if player_rect.colliderect(enemy_rect):
                return True

        return False