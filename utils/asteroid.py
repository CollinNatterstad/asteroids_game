import pygame
import random
from utils.circle_shape import CircleShape
from utils.constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius) -> None:
        super().__init__(x=x, y=y, radius=radius)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, radius=self.radius, center=self.position, width=2, color="white")

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(a=20, b=50)
        
        a = self.velocity.rotate(angle)
        b = self.velocity.rotate(angle*-1)

        asteroid = Asteroid(x=self.position.x, y=self.position.y, radius=self.radius-ASTEROID_MIN_RADIUS)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(x=self.position.x, y=self.position.y, radius=self.radius-ASTEROID_MIN_RADIUS)
        asteroid.velocity = b * 1.2
        
    
    def update(self, dt):
        self.position += self.velocity * dt