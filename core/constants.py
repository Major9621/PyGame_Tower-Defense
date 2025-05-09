import pygame

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 51, 0)
YELLOW = (248, 193, 7)
ORANGE = (255, 102, 0)
BLUE = (0, 0, 255)
GRAY = (100, 100, 100)
BROWN = (150, 75, 0)
PURPLE = (102, 0, 51)

# Screen dimensions
SCREEN_WIDTH = 832
SCREEN_HEIGHT = 512

# Game settings
FPS = 60
PATH_WIDTH = 40

TILE_SIZE = 32
TILESET_PATH = "assets/map/tile_map_textures.png"

def load_tiles_from_tileset(path, tile_size):
    tileset = pygame.image.load(path).convert_alpha()
    print("Tileset loaded:", tileset.get_size())
    tiles = []
    tileset_width, tileset_height = tileset.get_size()

    for y in range(0, tileset_height, tile_size):
        row = []
        for x in range(0, tileset_width, tile_size):
            rect = pygame.Rect(x, y, tile_size, tile_size)
            tile = tileset.subsurface(rect)
            scaled_tile = pygame.transform.scale2x(tile)
            row.append(scaled_tile)
        tiles.append(row)
    return tiles


TILE_TYPES = {}

def init_tile_types(path):
    global TILE_TYPES
    tiles = load_tiles_from_tileset(path, TILE_SIZE)
    TILE_TYPES = {
        'G': tiles[3][1],
        'P': tiles[4][0],
    }

# Enemy settings
ENEMY_RADIUS = 30
