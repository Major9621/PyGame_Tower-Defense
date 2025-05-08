def generate_tilemap_from_path(grid_path, width, height):
    tilemap = [['G' for _ in range(width)] for _ in range(height)]

    for i in range(len(grid_path) - 1):
        x1, y1 = grid_path[i]
        x2, y2 = grid_path[i + 1]

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                tilemap[y][x1] = 'P'
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                tilemap[y1][x] = 'P'

    return tilemap
