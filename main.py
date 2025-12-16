"""
Guided project froom Boot.dev to create a simple asteroids game and practice OOP
"""

import pygame
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

    # Create player object in center of screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game loop
    while True:
        log_state()

        # Check if user has closed the game window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()

        # Pause game loop for 1/60th of a second
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
