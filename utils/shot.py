import pygame
from utils.circle_shape import CircleShape
from utils.constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, radius=self.radius, center=self.position, width=2, color="white")
    
    def update(self, dt):
        self.position += self.velocity * dt