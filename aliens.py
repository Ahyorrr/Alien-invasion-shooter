import pygame

from pygame.sprite import Sprite


class Aliens(Sprite):
    """creating a class to manage all alien assets"""
    def __init__(self, ai):
        """initializing aliens and setting it's position"""

        super().__init__()
        self.screen = ai.screen
        self.settings = ai.settings

        # loading alien image
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # setting alien's position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""

        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.settings.alien_speed *
                   self.settings.fleet_direction)
        self.rect.x = self.x
