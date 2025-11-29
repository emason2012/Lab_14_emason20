'''
Alien Invasion
Ethan Mason
11/11
this code is respnsible for the arsenal for the ship in which it creates the laser, makes sure there arent too many rounds on the 
screen depending on what the setting is set for and removing off screen bullets
'''
from bullet import Bullet
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Arsenal:
    """Manage creation, updating, and drawing of the ship's bullets."""

    def __init__(self, game: 'AlienInvasion'):
        """Initialize an empty arsenal tied to the given game."""
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self) -> None:
        """Update bullet positions and remove any off-screen bullets."""
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self) -> None:
        """Remove bullets that have moved past the right edge of the screen."""
        screen_rect = self.game.screen.get_rect()
        for bullet in self.arsenal.copy():
            if bullet.rect.left >= screen_rect.right:
                self.arsenal.remove(bullet)

    def draw(self) -> None:
        """Draw all active bullets in the arsenal."""
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self) -> bool:
        """Create a new bullet if the maximum on-screen limit is not reached."""
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False
