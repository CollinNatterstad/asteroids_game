import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x:int, y:int, radius:float) -> None:
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius
    
    def collision(self, other:object) -> bool:
        return self.position.distance_to(other.position) <= self.radius + other.radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass
