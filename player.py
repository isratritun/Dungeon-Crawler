import pygame
from gameobject import GameObject

GREEN  = (0, 255, 0)

class Player(GameObject):
    def __init__(self, gridx, gridy, tile_width, tile_height, color = GREEN):
        # Calculate the initial pos manually using grid system tiles
        x = gridx * tile_width
        y = gridy * tile_height
        super().__init__(gridx, gridy, x, y, tile_width, tile_height, color)

    def draw(self, surface):
        ## TODO: need to update
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.tile_width, self.tile_height))

    def update(self):
        pass