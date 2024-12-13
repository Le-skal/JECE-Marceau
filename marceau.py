import pygame
import random

class Marceau:
    def __init__(self, screen_width, screen_height, size, horizontal_movement=False):
        self.x = random.randint(0, screen_width - size)
        self.y = random.randint(-100, -size)
        self.size = size
        self.speed = random.randint(3, 6)
        self.horizontal_speed = random.choice([-2, 2]) if horizontal_movement else 0

    def fall(self, screen_width):
        self.y += self.speed
        self.x += self.horizontal_speed
        if self.x < 0 or self.x > screen_width - self.size:
            self.horizontal_speed *= -1

    def draw(self, screen, image):
        screen.blit(image, (self.x, self.y))

    def is_caught(self, player):
        player_rect = pygame.Rect(player.x, player.y, player.size, player.size)
        marceau_rect = pygame.Rect(self.x, self.y, self.size, self.size)
        return player_rect.colliderect(marceau_rect)
