import pygame
import random
from CircleShape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "White", self.position, self.radius, width=2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        
        vector_one = self.velocity.rotate(angle)
        vector_two = self.velocity.rotate(-angle)

        smaller_radius = self.radius - ASTEROID_MIN_RADIUS
        x, y = self.position

        a1 = Asteroid(x, y, smaller_radius)
        a2 = Asteroid(x, y, smaller_radius)

        a1.velocity = vector_one * 1.2
        a2.velocity = vector_two * 1.2