# Snake Game with Pygame

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class Cube(object):
    rows = 0
    w = 0
    def __init__(self, start, dirnx = 1, dirny = 0, color = (255,0,0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes = False):
        pass

class Snake(object):
    body = []
    turns = {}
    def __init__(self, color, pos):
        self.color = color,
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dirnx = 0 # Can be -1, 0, 1
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                
                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move[turn[0], turn[1]]
                if i == len(self.body):
                    self.turns.pop(p)
            else:
                if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows - 1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows -1: c.pos = (0, c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows - 1: c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0], c.rows -1)
                else: 
                    c.move(c.dirnx, c.dirny)


    def reset(self, pos):
        pass

    def add_cube(self):
        pass

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)

def draw_grid(w, rows, surface):
    size_between = w // rows

    x = 0
    y = 0

    for i in range(rows):
        x += size_between
        y += size_between

        pygame.draw.line(surface, (255, 255, 255),(x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255),(0, y), (w, y))

def redraw_window(width, rows, surface):
    surface.fill((0,0,0))
    draw_grid(width, rows, surface )
    pygame.display.update()

def random_snack(rows, items):
    pass

def message_box(subject, content):
    pass

def main():
    width = 500
    height = 500
    
    rows = 20

    win = pygame.display.set_mode((width, height))

    s = Snake((255, 0, 0), (10,10))

    flag = True
    clock = pygame.time.Clock()

    while flag:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False

        pygame.time.delay(50)
        clock.tick(10)

        redraw_window(width, rows,win)

    pygame.quit()

if __name__ == '__main__':
    main()