"""
Guided project froom Boot.dev to create a simple asteroids game and practice OOP
"""

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player


def main():
    """
    Initiate the game and run game loop
    :return: None
    """
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize PyGame
    pygame.init()

    # Create game clock
    game_clock = pygame.time.Clock()
    dt = 0

    # Get a new instance of a GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create groups to manage game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Add player and NPC objects to both groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    # Create player object in center of screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Create asteroid field object
    asteroid_field = AsteroidField()

    # Game loop
    while True:
        log_state()

        # Check if user has closed the game window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Draw background
        screen.fill("black")

        # Update objects
        updatable.update(dt)

        # Draw objects
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()

        # Pause game loop for 1/60th of a second
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
