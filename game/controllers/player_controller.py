import pygame
import pygame.locals
from ..constants import P_SHOOT_COOLDOWN
from pygame.sprite import Sprite
from ..models.player_laser import PlayerLaser

class PlayerController():
    """ Handles logic for the player """
    def __init__(self, player):
        self.player = player
        self._last_fired = 0
        self.lasers = pygame.sprite.Group()

    def action(self, keys) -> None:
        """ Takes the keyboard inputs and decides how to move the player """
        # Right
        if keys[pygame.locals.K_RIGHT]:
            self.player.rect.x = min(self.player.rect.x + 5, 470)
            print('Key right')
        #Left
        if keys[pygame.locals.K_LEFT]:
            self.player.rect.x = max(self.player.rect.x - 5, 0)
            print('Key left')
        # Up
        if keys[pygame.locals.K_UP]:
            self.player.rect.y = max(self.player.rect.y - 5, 0)
            print('Key up')
        # Down
        if keys[pygame.locals.K_DOWN]:
            self.player.rect.y = min(self.player.rect.y + 5, 820)
            print('Key down')
        # Shoot 
        if keys[pygame.locals.K_SPACE]:
            print('Key space')
            current_ticks = pygame.time.get_ticks()
            if current_ticks > self._last_fired + P_SHOOT_COOLDOWN:
                self._last_fired = current_ticks
                self._laser = PlayerLaser((self.player.rect.x, self.player.rect.y))
                self.lasers.add(self._laser)