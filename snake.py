import pygame

from cube import Cube
from food import Food

# class Snake:
#     def __init__(self, initial_position, initial_length = 1) -> None:
#         self. _body:list[Cube] = []
#         self.head: Cube = Cube(initial_position)
#         # self.body.append(self.head)
#         self._body = [self.head, Cube((initial_position[0] + 10, initial_position[1])), Cube((initial_position[0] + 20, initial_position[1]))]
#         self._direction = (-1, 0)
#         self.turns = {}
#         self.color = (255,0,0)
#         self.width = 10
#         self.pending_snack = []

#     def move(self):
#         # in x direction, 0 does not move, 1 goes right, -1 goes left
#         # in y direction, 0 does not move, 1 goes up, -1 goes down
#         window_size = pygame.display.get_window_size()

#         for idx, segment in enumerate(self._body):
#             position = segment.position[:]
#             # print(f'Idx:{idx}, Direction:{segment.direction}, Position:{position},Turns:{self.turns}, Is in turns:{position in self.turns}')
#             if position in self.turns:
#                 turn = self.turns[position]
#                 segment.move(turn)
#                 if idx == len(self._body) - 1:
#                     self.turns.pop(position)
#             else:

#                 if segment.direction[0] < 0 and position[0] <= 0: 
#                     segment.position = (window_size[0] - segment.width, position[1])
#                 elif segment.direction[0] > 0 and position[0] >= window_size[0]- segment.width:
#                     segment.position = (0, position[1])
#                 elif segment.direction[1] < 0 and position[1] <= 0:
#                     segment.position = (position[0], window_size[0] - segment.width)
#                 elif segment.direction[1] > 0 and position[1] >=window_size[1] - segment.width:
#                     segment.position = (position[0], 0)
#                 else:
#                     segment.move(segment.direction)
#         if len(self.pending_snack) > 0:
#             for segment in self.body:
#                 if segment.position == self.pending_snack[0]:
#                     break
#             else:
#                 self.body.append(Cube(self.pending_snack[0], segment.direction))
#                 self.pending_snack.pop(0)

#     def update_direction(self,user_input):
#         if user_input == 'LEFT' and self._direction[0] != 1:
#             self._direction = (-1, 0)
#             self.turns[self.head.position[:]] = self._direction
#         elif user_input == 'RIGHT' and self._direction[0] != -1:
#             self._direction = (1, 0)
#             self.turns[self.head.position[:]] = self._direction
#         elif user_input == 'UP' and self._direction[1] != 1:
#             self._direction = (0, -1)
#             self.turns[self.head.position[:]] = self._direction
#         elif user_input == 'DOWN' and self._direction[1] != -1:
#             self._direction = (0, 1)
#             self.turns[self.head.position[:]] = self._direction


#     def grow(self):
#         self._body.append(self.head.position)

#     def check_collision(self):
#         """Check if snake collides with itself or the board boundaries"""
#         for idx, segment in enumerate(self.body):
#             if idx != 0 and segment.position == self.body[0].position:
#                 return True
#         return False
    
#     def check_collision_with_food(self, food: Food) -> bool:
#         food_position = food.get_position()
#         return self._body[0].position == food_position

#     def draw(self, screen):
#         for idx, segment in enumerate(self._body):
#             if idx == 0:
#                 segment.draw(screen, True)
#             else:
#                 segment.draw(screen)


class Snake:
    def __init__(self, initial_position: tuple[int, int], initial_length, cell_size) -> None:
        self._body: list[Cube] = []
        self._direction: tuple[int, int] = (1, 0)
        self.head = Cube(initial_position, self._direction)
        self._body.append(self.head)
        self._pending_food = []
        self._turns = {}
        self._cell_size = cell_size

    def move(self) -> None:

        screen_size = pygame.display.get_window_size()
        board_size_x = (screen_size[0] // self._cell_size) - 1
        board_size_y = (screen_size[1] // self._cell_size) - 1

        for idx, segment in enumerate(self._body):
            position = segment.get_position()
            if position in self._turns:
                turn = self._turns[position]

                segment.move(turn)
                if idx == len(self._body) - 1:
                    self._turns.pop(position)
            else:
                segment_dir = segment.get_direction()
                segment_pos = segment.get_position()

                if segment_dir[0] < 0 and segment_pos[0] <= 0: segment.set_position((board_size_x,segment_pos[1]))
                elif segment_dir[0] > 0 and segment_pos[0] >= board_size_x: segment.set_position((0, segment_pos[1]))
                elif segment_dir[1] < 0 and segment_pos[1] <= 0: segment.set_position((segment_pos[0], board_size_y))
                elif segment_dir[1] > 0 and segment_pos[1] >= board_size_y: segment.set_position((segment_pos[0], 0))
                else:
                    segment.move(segment_dir)

        if len(self._pending_food) > 0:
            for idx, segment in enumerate(self._body):
                if segment.get_position() == self._pending_food[0]:
                    break
            else:
                new_segment = Cube(self._pending_food[0],segment.get_direction())
                self._body.append(new_segment)
                self._pending_food.pop(0)

    def grow(self) -> None:
        self._pending_food.append(self._body[0].get_position())

    def update_direction(self, new_direction) -> None:
        if new_direction == 'UP' and self._direction != (0,1):
            self._direction = (0, -1)
            self._turns[self._body[0].get_position()] = self._direction
        elif new_direction == 'DOWN' and self._direction != (0,-1):
            self._direction = (0, 1)
            self._turns[self._body[0].get_position()] = self._direction
        elif new_direction == 'LEFT' and self._direction != (1, 0):
            self._direction = (-1, 0)
            self._turns[self._body[0].get_position()] = self._direction
        elif new_direction == 'RIGHT' and self._direction != (-1,0):
            self._direction = (1, 0)
            self._turns[self._body[0].get_position()] = self._direction
    def check_collision_with_food(self, food: Food) -> bool:
        return self._body[0].get_position() == food.get_position()
    
    def check_collision_with_self(self) -> bool:
        collision = False
        for idx, segment in enumerate(self._body):
            if idx != 0:
                if self._body[0].get_position() == segment.get_position():
                    return True
        
        return collision
    
    def get_segment_positions(self) -> list[tuple[int, int]]:
        return [segment.get_position() for segment in self._body]
    
    def draw(self, screen, cell_size):
        for segment in self._body:
            segment.draw(screen, cell_size)


