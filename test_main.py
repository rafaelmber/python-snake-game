import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class Cube():
    def __init__(self, start, dirnx = 1, dirny = 0, color = (255,0,0)):
        self.pos: pygame.Vector2 = pygame.Vector2(start)
        self.color = color
        self.width = 10

    def move(self, dirnx, dirny):
        if dirnx == -1:
            self.pos.x -= self.width
        if dirnx == 1:
            self.pos.x += self.width
        if dirny == -1:
            self.pos.y -= self.width
        if dirny == 1:
            self.pos.y += self.width

    def draw(self, surface, eyes = False):
        if eyes:
            pygame.draw.rect(surface, (200,0,0), (self.pos.x, self.pos.y, self.width, self.width))
        else:
            pygame.draw.rect(surface, self.color, (self.pos.x, self.pos.y, self.width, self.width))

class Snake():
    def __init__(self, color, pos = (250, 250)):
        self.color = color
        self.turn = {}
        self.body = []
        self.head = Cube(pos)
        self.body.append(self.head)
        self.width = 10
    
    def draw(self, surface):
        for idx, cube in enumerate(self.body):
            if idx == 0:
                cube.draw(surface, True)
            else:
                cube.draw(surface)

    def move(self, dirnx: int, dirny: int):
        window_size = pygame.display.get_window_size()
        for cube in self.body:
            if dirnx < 0 and cube.pos.x <= 0: cube.pos.x = window_size[0] - self.width
            elif dirnx > 0 and cube.pos.x >= window_size[0]- self.width: cube.pos.x = 0
            elif dirny < 0 and cube.pos.y <= 0: cube.pos.y = window_size[0] - self.width
            elif dirny > 0 and cube.pos.y >= window_size[1] - self.width: cube.pos.y = 0
            else: cube.move(dirnx, dirny)

    def add_cube(self):
        pass

def random_snack(snack_xcor, snack_ycor):
    width = 10
    screen = pygame.display.get_surface()
    pygame.draw.rect(screen, (255, 255, 255), (snack_xcor, snack_ycor,width,width))

def main():

    pygame.init()
    window_size = (500,500)
    screen = pygame.display.set_mode(window_size)
    clock = pygame.time.Clock()
    running = True
    dt = 0

    width = 10
    s: Snake = Snake((255, 0, 0))
    
    snack_xcor = (random.randint(0,window_size[0] - width) // width) * width
    snack_ycor = (random.randint(0,window_size[1] - width) // width) * width
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            s.move(-1,0)
        elif keys[pygame.K_RIGHT]:
            s.move(1, 0)
        elif keys[pygame.K_UP]:
            s.move(0, -1)
        elif keys[pygame.K_DOWN]:
            s.move(0, 1)



        screen.fill((0,0,0))
        random_snack(snack_xcor, snack_ycor)

        s.draw(screen)
        pygame.display.flip()
        dt = clock.tick(10) / 1000

    pygame.quit()

if __name__ == '__main__':
    main()