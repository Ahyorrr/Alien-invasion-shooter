class Settings:
    """creating class for all game settings"""


    def __init__(self):
        # screen settings
        self.game_width = 1200
        self.game_height = 650
        self.bg_color = (230, 230, 230)
        self.ship_speed = 5

        # bullet settings
        self.bullet_width = 3
        self.bullet_length = 13
        self.bullet_color = (60, 60, 60)
        self.bullet_speed = 5
        self.bullet_limit = 5

        # alien settings
        self.alien_speed =1
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
