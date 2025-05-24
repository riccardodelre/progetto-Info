import pygame

class Player:
    def __init__(self, image, x, y, speed, car_width, car_height):
        self.image = image
        self.x = x
        self.y = y
        self.speed = speed
        self.car_width = car_width
        self.car_height = car_height

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self, keys, bg_width, width):
        if keys[pygame.K_LEFT] and self.x > bg_width:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x + self.car_width < width - bg_width:
            self.x += self.speed

    def check_collision(self, enemy_cars):
        player_rect = pygame.Rect(self.x, self.y, self.car_width, self.car_height)
        for ex, ey, _ in enemy_cars:
            enemy_rect = pygame.Rect(ex, ey, self.car_width, self.car_height)
            if player_rect.colliderect(enemy_rect):
                return True
        return False