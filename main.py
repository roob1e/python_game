import sys
import pygame

from settings import TILE, SPEED, FPS, PLAYER_SIZE
from level import game_map, build_walls

pygame.init()

coins = [
    pygame.Rect(TILE * 2 + 15, TILE * 1 + 15, 10, 10),
    pygame.Rect(TILE * 4 + 15, TILE * 1 + 15, 10, 10),
    pygame.Rect(TILE * 2 + 15, TILE * 3 + 15, 10, 10)
]
score = 0

walls = build_walls()

WIDTH = len(game_map[0]) * TILE
HEIGHT = len(game_map) * TILE

player_rect = pygame.Rect(TILE * 1, TILE * 1, PLAYER_SIZE, PLAYER_SIZE)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for wall in walls:
        pygame.draw.rect(screen, (50, 50, 200), wall)

    keys = pygame.key.get_pressed()
    new_rect = player_rect.copy()

    if keys[pygame.K_LEFT]:
        new_rect.x -= SPEED
    if keys[pygame.K_RIGHT]:
        new_rect.x += SPEED
    if keys[pygame.K_UP]:
        new_rect.y -= SPEED
    if keys[pygame.K_DOWN]:
        new_rect.y += SPEED

    collided = False
    for wall in walls:
        if new_rect.colliderect(wall):
            collided = True
            break

    if not collided:
        player_rect = new_rect

    pygame.draw.rect(screen, (0, 200 ,0), player_rect)

    for coin in coins[:]:
        if player_rect.colliderect(coin):
            coins.remove(coin)
            score += 1

    for coin in coins:
        pygame.draw.rect(screen, (255, 220, 0), coin)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()