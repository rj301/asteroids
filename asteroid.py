"""
Create asteroid class inheriting from CircleShape
"""

import pygame, random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        """
        Draw asteroid on screen as a circle
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
        Update asteroid position
        :param dt: delta time (amount of time since last frame drawn)
        :return: None
        """
        self.position += self.velocity * dt

    def split(self):
        # Kill current asteroid
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")

        # Find velocities of new asteroids
        new_path_angle = random.uniform(20, 50)
        first_velocity = self.velocity.rotate(new_path_angle)
        second_velocity = self.velocity.rotate(-1 * new_path_angle)

        # Find size and position of new asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        spawn_x, spawn_y = self.position.x, self.position.y

        # Create new asteroids
        first_asteroid = Asteroid(spawn_x, spawn_y, new_radius)
        second_asteroid = Asteroid(spawn_x, spawn_y, new_radius)
        first_asteroid.velocity = first_velocity * 1.2
        second_asteroid.velocity = second_velocity * 1.2
