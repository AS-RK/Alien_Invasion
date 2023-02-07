import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage the bullets"""
    def __init__(self, ai_game):
        """Create the bullet at the top of the ship"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #creat a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """MOve the bullet up the screen."""
        #upgrade the decimal position of the bullet.
        self.y -= self.settings.bullet_speed

        #Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet to the screen"""
        pygame.draw.rect(self.screen, self.color , self.rect) 