import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot
pygame.display.set_caption('Asteroids-TSH')


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    #Declaração de grupos
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawable_group)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable_group, drawable_group)

    AsteroidField.containers = updatable_group
    asteroid_field = AsteroidField()

    shots= pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable_group, drawable_group)
    Shot.containers = (shots, updatable_group, drawable_group)

    #O player aparecer no meio da tela
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable_group:
            obj.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game over!")
                sys.exit()
    
        screen.fill("black")

        for obj in drawable_group:
            obj.draw(screen)

        pygame.display.flip()

        #Limitador de Framerate
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()