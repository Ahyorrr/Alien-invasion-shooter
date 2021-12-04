import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """making a class for all of bullet's attributes"""
    def __init__(self, ai):
        """creating a bullet at ship's current position"""
        super().__init__()
        self.screen = ai.screen
        self.settings = ai.settings
        self.color = ai.settings.bullet_color

        # drawing bullet
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_length)
        self.rect.midtop = ai.ship.rect.midtop

        # converting bullet position to float
        self.y = float(self.rect.y)

    def update(self):
        # moving bullet up the screen
        self.y -= self.settings.bullet_speed
        # converting back
        self.rect.y = self.y

    def draw_bullets(self):
        """draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)