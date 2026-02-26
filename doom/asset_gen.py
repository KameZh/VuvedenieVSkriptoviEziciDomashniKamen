import pygame
import random
import os

def generate_texture():
    pygame.init()
    size = 256
    surface = pygame.Surface((size, size))
    
    # Fill with noise/bricks
    for x in range(size):
        for y in range(size):
            r = random.randint(50, 150)
            g = random.randint(50, 100)
            b = random.randint(50, 100)
            # Create a brick pattern
            if (x % 64 < 2) or (y % 64 < 2):
                r, g, b = 20, 20, 20
            
            surface.set_at((x, y), (r, g, b))
    
    os.makedirs('resources/textures', exist_ok=True)
    pygame.image.save(surface, 'resources/textures/1.png')
    print("Texture generated.")

    # Weapon
    weapon_surface = pygame.Surface((200, 300), pygame.SRCALPHA)
    pygame.draw.rect(weapon_surface, (50, 50, 50), (60, 100, 80, 200)) # barrel
    pygame.draw.rect(weapon_surface, (20, 20, 20), (50, 250, 100, 50)) # handle
    pygame.image.save(weapon_surface, 'resources/textures/weapon.png')
    print("Weapon generated.")

if __name__ == "__main__":
    generate_texture()
