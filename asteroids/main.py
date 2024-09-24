import pygame
import sys
from constants import *
from Shot import Shot
from Player import Player
from Asteroid import Asteroid
from AsteroidField import AsteroidField
from Score import Score

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
    score = Score()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updateable:
            obj.update(dt)
        
        for obj in asteroids:
            if obj.is_colliding(player):
                if player.lives == 0:
                    sys.exit()
                else:
                    player.reset()

            for bullet in shots:
                if bullet.is_colliding(obj):
                    obj.split(score)
                    bullet.kill()
        
        for obj in drawable:
            obj.draw(screen)

        scoreboard= score.font.render(f"Score: {score.value}", False, ((100,100,100)))
        lives = score.font.render(f"Lives: {player.lives}", False, ((100,100,100)))

        screen.fill("black")

        screen.blit(scoreboard, (0,0))
        screen.blit(lives, (0,50))

        pygame.display.flip()
        dt = clock.tick() / 1000

if __name__ == "__main__":
    main()