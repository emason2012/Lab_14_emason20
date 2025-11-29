
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
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    """A projectile fired horizontally from the front of the ship."""

    def __init__(self, game: 'AlienInvasion'):
        """Create a new bullet originating from the ship's right side."""
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings

        # Load, rotate, and scale the bullet image to fire horizontally.
        original_image = pygame.image.load(self.settings.bullet_file)
        rotated_image = pygame.transform.rotate(original_image, -90)
        self.image = pygame.transform.scale(
            rotated_image,
            (self.settings.bullet_h, self.settings.bullet_w),
        )

        self.rect = self.image.get_rect()
        self.rect.midright = game.ship.rect.midright

        self.x = float(self.rect.x)

    def update(self) -> None:
        """Move the bullet horizontally to the right."""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self) -> None:
        """Draw the bullet onto the screen."""
        self.screen.blit(self.image, self.rect)