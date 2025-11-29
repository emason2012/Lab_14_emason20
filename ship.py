'''
Alien Invasion
Ethan Mason
11/11
this code is responsible for placing the ship on screen as well as what boundries it has with movement and size
'''
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal


class Ship:
    """Player-controlled ship that moves vertically and fires bullets to the right."""

    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal') -> None:
        """Initialize the ship sprite, its position, and its arsenal."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundries = self.screen.get_rect()

        # Load and rotate the ship image so it faces right.
        original_image = pygame.image.load(self.settings.ship_file)
        rotated_image = pygame.transform.rotate(original_image, -90)
        self.image = pygame.transform.scale(
            rotated_image,
            (self.settings.ship_h, self.settings.ship_w),
        )

        self.rect = self.image.get_rect()
        self._center_ship()

        # Vertical movement flags: True when arrow keys are pressed.
        self.moving_up = False
        self.moving_down = False

        self.arsenal = arsenal

    def _center_ship(self) -> None:
        """Position the ship vertically centered on the left edge of the screen."""
        self.rect.midleft = self.boundries.midleft
        self.y = float(self.rect.y)

    def update(self) -> None:
        """Update the ship's position and its arsenal projectiles."""
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self) -> None:
        """Move the ship up or down within the screen boundaries."""
        temp_speed = self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.boundries.bottom:
            self.y += temp_speed
        if self.moving_up and self.rect.top > self.boundries.top:
            self.y -= temp_speed

        self.rect.y = self.y

    def draw(self) -> None:
        """Draw the ship and its bullets to the screen."""
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self) -> bool:
        """Fire a bullet from the front of the ship if ammo limit allows."""
        return self.arsenal.fire_bullet()

    def check_collisions(self, other_groups) -> bool:
        """Check for collisions between the ship and any sprite in other_groups."""
        if pygame.sprite.spritecollideany(self, other_groups):
            self._center_ship()
            return True
        return False
    