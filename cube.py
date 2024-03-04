import pygame
from typing import Tuple

class Cube:
    def __init__(self, position: Tuple[int, int], direction: Tuple[int, int]):
        self._position: Tuple[int, int] = position
        self._direction: Tuple[int, int] = direction
        self._color: Tuple[int, int, int] = (255, 0, 0)

    def move(self, direction: Tuple[int, int]) -> None:
        self._direction = direction
        x = self._position[0] + self._direction[0]
        y = self._position[1] + self._direction[1]
        self._position = (x, y)

    def get_position(self) -> Tuple[int, int]:
        return self._position
    
    def set_position(self, position: Tuple[int, int]) -> None:
        self._position = position
    
    def get_direction(self) -> Tuple[int, int]:
        return self._direction

    def draw(self, screen: pygame.Surface ,cell_size: int,  eyes: bool = False) -> None:
        x = self._position[0] * cell_size
        y = self._position[1] * cell_size
        if eyes:
            pygame.draw.rect(screen, (150, 0, 0), (x, y, cell_size, cell_size))
        else:
            pygame.draw.rect(screen, self._color, (x,y, cell_size, cell_size))