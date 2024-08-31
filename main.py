import pygame
from utils.constants import *
from utils.player import Player
from utils.asteroid import Asteroid
from utils.asteroid_field import AsteroidField
from utils.shot import Shot


def main():
    # board 
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    # sprite groups
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # class containers 
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    _ = AsteroidField()

    dt = 0 
    run = True

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    while run:
        screen.fill("black")

        for sprite in updatable:
            sprite.update(dt=dt)

        for sprite in drawable:
            sprite.draw(screen=screen)

        for sprite in asteroids:
            if sprite.collision(player):
                print("Game Over!")
                exit()
        
        for shot in shots:
            for asteroid in asteroids:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000            
        pygame.display.flip()

if __name__ == "__main__":
    main()

