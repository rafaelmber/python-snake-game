import pygame
from typing import Tuple
class GameBoard:
    def __init__(self, width: int, height: int, cell_size: int ) -> None:
        self._width = width
        self._height = height

        self._cell_size: int = cell_size

        self._board: list[list[int]] = [[0] * (self._width// self._cell_size) for _ in range(self._height // self._cell_size)]

    def draw(self, screen: pygame.Surface, score: int) -> None:
        window_size = screen.get_size()
        font = pygame.font.Font(None, 24)
        text = f'Score: {score}'
        text_surface = font.render(text, True, (255, 255, 255))

        screen.blit(text_surface, (window_size[0] // 2, 1))

    def place_food(self, x: int, y: int) -> None:
        self._board[y][x] = 2

    def get_board_cells(self):
        return self._board