import pygame
from .constants import TILE_SIZE
import core.constants as cst
from utils.tilemap_generator import generate_tilemap_from_path

class Map:
    def __init__(self, grid_path):
        self.grid_path = grid_path
        self.width = max(x for x, y in grid_path) + 1
        self.height = max(y for x, y in grid_path) + 1
        self.tilemap = generate_tilemap_from_path(grid_path, self.width, self.height)


    def draw(self, surface):
        for y, row in enumerate(self.tilemap):
            for x, tile in enumerate(row):
                image = cst.TILE_TYPES.get(tile)
                if image:
                    surface.blit(image, (x * TILE_SIZE * 2, y * TILE_SIZE * 2))
