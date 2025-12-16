"""
Define Player class inheriting form CircleShape class
"""

import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the Player class
    def triangle(self):
        """
        Find corners of player triangle, code from Boot.dev
        :return: List of corners of player triangle
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        """
        Draw player on screen as a triangle
        :param screen: Screen object
        :return: None
        """
        pygame.draw.polygon(
            screen,
            (255, 255, 255),
            self.triangle(),
            LINE_WIDTH
        )