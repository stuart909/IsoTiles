from tkinter import *
import pygame

class Tile:
    def __init__(self, x, y, screen_width, screen_height, camera_height, grid_width, grid_height):
        self.x = x
        self.y = y
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.camera_height = camera_height
        self.grid_width = grid_width
        self.grid_height = grid_height

    def draw(self, screen, offset_x, offset_y, zoom):
        tile_width = self.grid_width // zoom
        tile_height = self.grid_height // zoom
        x = (self.x * tile_width) + (tile_width // 2) + offset_x
        y = (self.y * tile_height) + (tile_height // 2) + self.camera_height * zoom + offset_y

        if x >= 0 and x <= self.screen_width and y >= 0 and y <= self.screen_height:
            pygame.draw.polygon(screen, BLACK, [
                [x, y],
                [x + tile_width // 2, y - tile_height // 2],
                [x + tile_width, y],
                [x + tile_width // 2, y + tile_height // 2]
            ], 1)





if __name__ == "__main__":
    pygame.init()
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    screen_width = 1800
    screen_height = 1000

    rows = 100
    columns = 100

    screen = pygame.display.set_mode((screen_width, screen_height))
    done = False
    clock = pygame.time.Clock()

    offset_x = 0
    offset_y = 0
    zoom = 1
    tiles = [Tile(x, y, screen_width, screen_height, 40, 90, 50) for x in range(rows) for y in range(columns)]
    while not done:
        clock.tick(60)

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            offset_y += 10
        elif pressed[pygame.K_DOWN]:
            offset_y -= 10
        elif pressed[pygame.K_LEFT]:
            offset_x += 10
        elif pressed[pygame.K_RIGHT]:
            offset_x -= 10
        if pressed[pygame.K_EQUALS] or pressed[pygame.K_KP_PLUS]:
            zoom = min(2, zoom + 0.025)
        elif pressed[pygame.K_MINUS] or pressed[pygame.K_KP_MINUS]:
            zoom = max(0.25, zoom - 0.025)

        screen.fill(WHITE)
        
        for tile in tiles:
            tile.draw(screen, offset_x, offset_y, zoom)

        pygame.display.flip()
        
    pygame.quit()
