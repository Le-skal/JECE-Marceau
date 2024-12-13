import pygame
import random

class Boost:
    def __init__(self, screen_width, screen_height, size):
        self.x = random.randint(0, screen_width - size)
        self.y = random.randint(-200, -size)
        self.size = size
        self.speed = 4

    def fall(self):
        self.y += self.speed

    def draw(self, screen, image):
        screen.blit(image, (self.x, self.y))

    def is_caught(self, player):
        player_rect = pygame.Rect(player.x, player.y, player.size, player.size)
        boost_rect = pygame.Rect(self.x, self.y, self.size, self.size)
        return player_rect.colliderect(boost_rect)
