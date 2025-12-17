"""
Define Player class inheriting form CircleShape class
"""

import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, PLAYER_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SPEED, PLAYER_TURN_SPEED, SHOT_RADIUS, \
    PLAYER_SHOOT_COOLDOWN_SECONDS
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0

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

    def rotate(self, dt):
        """
        Update the direction the player is facing
        :param dt: delta time (amount of time since last frame drawn)
        :return: None
        """
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        """
        Move the player forward or backward
        :param dt: delta time (amount of time since last frame drawn)
        :return: None
        """
        player_direction_vector = pygame.Vector2(0, 1).rotate(self.rotation)
        player_velocity = player_direction_vector * PLAYER_SPEED * dt
        self.position += player_velocity

    def update(self, dt):
        """
        Update player position when key pressed, starter code from Boot.dev
        Reduce cooldown on player shot timer
        :param dt: delta time (amount of time since last frame drawn)
        :return: None
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-1 * dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-1 * dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        # Only decrement cooldown if not already <= 0 to prevent cooldown
        # overflow or bugs if player doesn't shoot for a very long time
        # If game loop requires player to shoot fast enough to prevent this
        # or die, then the check can be removed
        if self.shot_cooldown > 0:
            self.shot_cooldown -= dt

    def shoot(self):
        """
        Fire a shot from the player
        :return: None
        """
        if self.shot_cooldown <= 0:
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            shot.velocity = velocity
            self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS

