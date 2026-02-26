import pygame
from settings import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()

    def get_texture(self, path):
        texture = pygame.image.load(path).convert()
        return pygame.transform.scale(texture, (TEXTURE_SIZE, TEXTURE_SIZE))

    def render_game_objects(self):
        # Placeholder for sprite rendering later
        pass
    
    @staticmethod
    def get_texture_column(texture, offset_x):
        # Return a subsurface for the given column
        x = offset_x * (TEXTURE_SIZE - 1)
        return texture.subsurface(x, 0, 1, TEXTURE_SIZE)

    def draw_wall(self, depth, proj_height, offset_x, ray_index, texture_id=1):
        texture = self.wall_textures[texture_id]
        if proj_height > HEIGHT:
            # simple optimization/cropping if wall is close
            # But calculating crop for texture is tricky, skip for now or keep simple
            # If we just scale, pygame handles clipping but it's slow if huge
            pass
        
        # Calculate texture column
        # Scaling the WHOLE texture column to proj_height
        column = self.wall_textures[texture_id].subsurface(
            offset_x * (TEXTURE_SIZE - 1), 0, 1, TEXTURE_SIZE
        )
        column = pygame.transform.scale(column, (SCALE, int(proj_height)))
        
        wall_pos = (ray_index * SCALE, HALF_HEIGHT - proj_height // 2)
        self.screen.blit(column, wall_pos)

    def draw(self):
        self.render_game_objects()
        self.screen.blit(self.weapon, (WIDTH // 2 - self.weapon.get_width() // 2, HEIGHT - self.weapon.get_height()))

    def load_wall_textures(self):
        self.weapon = pygame.image.load('resources/textures/weapon.png').convert_alpha()
        self.weapon = pygame.transform.scale(self.weapon, (400, 600))
        return {
            1: self.get_texture('resources/textures/1.png'),
        }
