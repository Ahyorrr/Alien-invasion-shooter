import pygame


class Ship:
    """creating a class for all of the ship's features"""

    def __init__(self, ai):
        self.screen = ai.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai.settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # setting ship's position
        self.rect.midbottom = self.screen_rect.midbottom

        # setting flags
        self.move_left = False
        self.move_right = False

        # converting rect to receive float
        self.x = float(self.rect.x)

    def update(self):
        if self.move_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        # converting back
        self.rect.x = self.x

    def blit_ship(self):
        self.screen.blit(self.image, self.rect)
