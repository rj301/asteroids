"""
Create a shot object to function as projectiles being fired in the game
"""

import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        """
        Draw shot (bullet) on screen as a circle
        :param screen: Screen object
        :return: None
        """
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            self.position,
            self.radius,
            LINE_WIDTH
        )

    def update(self, dt):
        """
        Update shot (bullet) position
        :param dt: delta time (amount of time since last frame drawn)
        :return: None
        """
        self.position += self.velocity * dt