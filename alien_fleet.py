'''
Alien Invasion
Ethan Mason
11/18
this code is respnsible for controlling the alien fleet on screen
'''

import pygame
from Alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class AlienFleet:
    """Manage a fleet of alien enemies moving across the screen."""

    def __init__(self, game: 'AlienInvasion'):
        """Initialize the fleet with reference to the main game object."""
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()

    def create_fleet(self) -> None:
        """Create a full fleet of aliens on the right side of the screen."""
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        fleet_w, fleet_h = self.calculate_fleet_size(
            alien_w, screen_w, alien_h, screen_h
        )

        x_offset, y_offset = self.calculate_offsets(
            alien_w, alien_h, screen_w, fleet_w, fleet_h
        )
        self._create_rectangle_fleet(
            alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset
        )

    def _create_rectangle_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        """Create full grid with a 1-ship gap between aliens."""
        for row in range(fleet_h):
            for col in range(fleet_w):
                current_x = x_offset + col * (alien_w * 2)
                current_y = y_offset + row * (alien_h * 2)
                self._create_alien(current_x, current_y)

    def calculate_offsets(self, alien_w, alien_h, screen_w, fleet_w, fleet_h):
        """Place fleet on the right side with a small margin."""
        x_offset = screen_w - (fleet_w * alien_w * 2)
        y_offset = (self.settings.screen_h - (fleet_h * alien_h * 2)) // 2
        return x_offset, y_offset

    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):
        """Determine only a few columns, but fill vertical space as needed."""
        fleet_h = screen_h // (alien_h * 2)
        fleet_w = 5
        return fleet_w, fleet_h

    def _create_alien(self, current_x: int, current_y: int):
        """Creates the alien for each spot"""
        new_alien = Alien(self, current_x, current_y)

        self.fleet.add(new_alien)

    def _check_fleet_edges(self):
        """Checks the screen edges to make sure all aliens stay on screen"""
        alien: Alien
        for alien in self.fleet:
            if alien.rect.left <= 0:
                return True
        return False
        
    def _drop_alien_fleet(self):
        """Allows the aliens to fall in a fixed pattern"""
        for alien in self.fleet:
            alien.y += self.fleet_drop_speed
    
    def update_fleet(self):
        """Move the fleet left each frame."""
        self.fleet.update()
        

    def draw(self):
        """Draws the fleet on screen"""
        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_groups):
        """Checks for collisions with the aliens and bullets as well as aliens and sprite"""
        return pygame.sprite.groupcollide(self.fleet, other_groups, True, True)
    
    def check_fleet_bottom(self):
        """Checks if the fleet has reached the bottom of the screen"""
        alien: Alien
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_h:
                return True
        return False
    
    def check_left_side(self):
        """Return True if any alien reaches the left side of the screen."""
        for alien in self.fleet:
            if alien.rect.left <= 0:
                return True
        return False
        

    def check_destroyed_status(self):
        """Checks if the fleet has been completely destroyed."""
        return not self.fleet