from circleshape import CircleShape
import pygame
from constants import * 


class Shot(CircleShape):
    containers = None
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

        if Shot.containers:
            for container in Shot.containers:
                container.add(self)


    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += self.velocity * dt


