import pygame
import random
from typing import Tuple

class Food:
    def __init__(self) -> None:
        self._position: Tuple[int, int]= (100,100) # random
        self.color = (0, 255, 255)
        
    def set_position(self, x: int, y: int) -> None:
        self._position = (x, y)

    def get_position(self):
        return self._position

    def draw(self, screen: pygame.Surface, cell_size) -> None:
        radius = cell_size // 2
        x = self._position[0] * cell_size + radius
        y = self._position[1] * cell_size + radius
        pygame.draw.circle(screen, self.color, (x,y), radius) 

