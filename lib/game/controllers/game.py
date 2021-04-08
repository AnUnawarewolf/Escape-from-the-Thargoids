import pygame
from ..constants import WIDTH, HEIGHT, P_SHOOT_COOLDOWN
# Player
from ..models.player import PlayerShip
from ..models.player_laser import PlayerLaser
from .player_controller import PlayerController
# Enemies
from ..models.enemy_ship import EnemyShip
from .enemy_controller import EnemyController
# Views
from ..views.main_view import MainView
# Score
from ...models.score import Score
from ...models.score_manager import ScoreManager

class GameController():
    """ Game's main controller """
    def __init__(self):
        pygame.init()
        # Game's window
        self._window = pygame.display.set_mode((WIDTH, HEIGHT))
        # Player instance
        self._player = PlayerShip()
        # Player's lasers
        self._player_controller = PlayerController(self._player)
        # Clock
        self._clock = pygame.time.Clock()
        # Enemy
        self._first_enemy = EnemyShip()
        self._enemy_controller = EnemyController(self._first_enemy)
        # Views
        self._main_view = MainView(self._window, self._player, 
            self._player_controller.lasers, self._enemy_controller.enemies)
        # Score
        self._score = Score()
        self._score.name = "HAHAHAHAHAHAHAHA"
        self._score_manager = ScoreManager()

    def execute(self):
        """ Contains the game's main logic and loop """
        running = True
        while running:
            self._score.km = round(pygame.time.get_ticks() / 1000, 2)
            self._window.fill((0, 0, 0))
            self._clock.tick(60)

            # Closing the game
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    self._score_manager.add_score(self._score)
                    self._score_manager.save()
                    running = False

            # Player movement
            keys = pygame.key.get_pressed()
            self._player_controller.action(keys)

            # Enemies
            self._enemy_controller.spawn()

            for laser in self._player_controller.lasers:
                for enemy in self._enemy_controller.enemies:
                    if pygame.sprite.collide_mask(laser, enemy):
                        # Increase scores
                        self._score.kills += 1
                        self._score.kill_score += 1

                        laser.kill()
                        enemy.kill()
            
            for enemy in self._enemy_controller.enemies:
                if pygame.sprite.collide_mask(self._player, enemy):
                    enemy.kill()

            self._enemy_controller.enemies.update()
            self._player_controller.lasers.update()
            # Update screen
            self._main_view.update()

if __name__ == "__main__":
    controller = GameController()
    controller.execute()