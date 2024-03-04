import pygame
import random
from typing import Tuple

from game_board import GameBoard
from snake import Snake
from food import Food
from view import View

class Controller():
    def __init__(self, screen_width: int, screen_height: int, cell_size: int) -> None:
        self._screen_width: int = screen_width
        self._screen_height: int = screen_height
        self._cell_size: int = cell_size
        self._score: int = 0
        self._snake: Snake = Snake(initial_position=(10,10), initial_length=3, cell_size=cell_size)
        self._game_board: GameBoard = GameBoard(screen_width, screen_height, cell_size)
        self._food: Food = Food()
        self._view: View = View()

        self._current_state = "PLAYING"

        self.place_food()

    def place_food(self) -> None:

        x, y = self.get_random_empty_cell()
        self._food.set_position(x, y)
        self._game_board.place_food(x, y)

    def get_random_empty_cell(self) -> Tuple[int, int]:
        board_cells: list[list[int]] = self._game_board.get_board_cells()
        
        empty_cell: bool = False

        while empty_cell != True:
            x: int = random.randint(0, (self._screen_width // self._cell_size) - 1)
            y: int = random.randint(0, (self._screen_height // self._cell_size) - 1)

            for position in self._snake.get_segment_positions():
                if position == (x,y):
                    break
            else:
                empty_cell = True
        return x, y
    
    def update(self, user_input) -> None:
        if self._current_state == 'PLAYING':
            if user_input == 'ESCAPE':
                self._current_state = 'PAUSE'
            else:
                self._snake.update_direction(user_input)
                self._snake.move()
                self.check_collision()
        
        elif self._current_state == 'PAUSE':
            if user_input == 'ESCAPE':
                self._current_state = 'PLAYING'
        
        elif self._current_state == 'END_GAME':
            if user_input == 'ESCAPE':
                pygame.display.quit()

    def check_collision(self) -> None:
        if self._snake.check_collision_with_food(self._food):
            self._snake.grow()
            self.place_food()
            self._score += 1
        if self._snake.check_collision_with_self():
            # Lose
            self._current_state = 'END_GAME'
    
    def draw(self, screen: pygame.Surface):

        if self._current_state == 'PLAYING':
            screen.fill((0,0,0))

            self._food.draw(screen, self._cell_size)
            self._snake.draw(screen, self._cell_size)
            self._game_board.draw(screen, self._score)

        elif self._current_state == 'END_GAME':
            self._view.draw(screen, self._score)

