import pygame

class Player:
    def __init__(self, x, y, arm_size):
        self.x = x
        self.y = y
        self.size = arm_size
        self.speed = 10
        self.boosted = False
        self.boost_duration = 0 # Duree restante du boost en frames

    def move(self, keys, screen_width, screen_height):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < screen_width - self.size:
            self.x += self.speed
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < screen_height - self.size:
            self.y += self.speed

    def apply_boost(self):
        self.boosted = True
        self.speed *= 1.25
        self.boost_duration = 90 

    def update(self):
        if self.boosted:
            self.boost_duration -= 1
            if self.boost_duration <= 0:
                self.boosted = False
                self.speed //= 1.25 # Reinitialise la vitesse

    def draw(self, screen, image):
        screen.blit(image, (self.x, self.y))
