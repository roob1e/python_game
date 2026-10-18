import pygame
from settings import TILE

game_map = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

def build_walls() -> list:
    walls = []
    for row_index, row in enumerate(game_map):
        for col_index, cell in enumerate(row):
            if cell == 1:
                x = col_index * TILE
                y = row_index * TILE
                walls.append(pygame.Rect(x, y, TILE, TILE))

    return walls