import pygame
import sys
from constants import *
from Shot import Shot
from Player import Player
from Asteroid import Asteroid
from AsteroidField import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updateable, drawable)
    Player.containers = (updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, drawable, updateable)

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()

    dt = 0
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for obj in updateable:
            obj.update(dt)
        
        for obj in asteroids:
            if obj.is_colliding(player):
                print(f"Game Over! Score: {score}")
                sys.exit() 

            for bullet in shots:
                if bullet.is_colliding(obj):
                    obj.split()
                    bullet.kill()
                    score += 1
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick() / 1000

if __name__ == "__main__":
    main()