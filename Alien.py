
'''
Alien Invasion
Ethan Mason
11/11
this code is respnsible for making the bullet that is fried from arsenal as well as controlling bullet speed and direction
'''
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    """A single alien in the invading fleet."""

    def __init__(self, fleet: 'AlienFleet', x: float = 0, y: float = 0):
        """Initialize an alien at the given x, y position within its fleet."""
        super().__init__()
        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        rotated_image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.alien_w, self.settings.alien_h),
        )

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self) -> None:
        """Move the alien horizontally according to fleet direction and speed."""
        temp_speed = self.settings.fleet_speed
        self.x += temp_speed * self.fleet.fleet_direction
        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self) -> bool:
        """Return True if the alien has hit the left or right edge."""
        return self.rect.left <= self.boundries.left

    def draw_alien(self) -> None:
        """Draw the alien on the screen."""
        self.screen.blit(self.image, self.rect)