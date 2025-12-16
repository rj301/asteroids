import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
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

    # Game loop
    while True:
        log_state()

        # Check if user has closed the game window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()

        # Pause game loop for 1/60th of a second
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
