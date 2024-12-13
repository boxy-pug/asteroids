from circleshape import CircleShape
import pygame
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)

        if self.containers:
            for container in self.containers:
                container.add(self)



    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            new_vector1 = self.velocity.rotate(angle)
            new_vector2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            small_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            small_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            small_asteroid1.velocity = new_vector1 * 1.2
            small_asteroid2.velocity = new_vector2 * 1.2 

