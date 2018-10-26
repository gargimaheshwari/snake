# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 02:15:08 2018

@author: Gargi
"""

import pygame
import random
from queue import deque
from pygame.color import Color
import time

# Dimensions of the screen
D = 10 # resolution
W = 40 # width
H = 30 # height
N = 5 # number of plays

# colours for the blocks
BLACK = Color("black")
WHITE = Color("white")
RED = Color("red")

# directions of movement for the snake
DIRECTION = {-1: "left", +1: "right", -W: "up", W: "down"}
LEFT, RIGHT, UP, DOWN = -1, 1, -W, W
MOVES = (LEFT, RIGHT, UP, DOWN)
INF = W*H +1

cherry = None
snake = deque()

def possible_moves(mv, pos):
    if mv == LEFT:
        return pos%W > 0
    if mv == RIGHT:
        return pos%W <= W - 1
    if mv == UP:
        return pos >= W
    if mv == DOWN:
        return pos < (H-1)*W

def dist_to_cherry(pos):
    cherry_pos_x = (W if (cherry%W) == 0 else (cherry%W))
    cherry_pos_y = int(cherry/W)
    
    snake_pos_x = (W if (pos%W) == 0 else (pos%W))
    snake_pos_y = int(pos/W)
    
    x_dist = cherry_pos_x - snake_pos_x
    y_dist = cherry_pos_y - snake_pos_y
    return((x_dist, y_dist))
    
def next_step(pos, dist):
    possibles  = [mv for mv in MOVES if mv+pos not in list(snake)[:]]
    move_possibles = []
    for mv in possibles:
        if possible_moves(mv, pos):
            if abs(dist_to_cherry(mv+pos)[0]) <= abs(dist[0]) and abs(dist_to_cherry(mv+pos)[1]) <= abs(dist[1]):
                move_possibles.append(mv)
    return(move_possibles)
                
    
def draw(window, previous):
    
    dirty_rects = []
    
    cherry_x = ((W if (cherry%W) == 0 else (cherry%W))-1)*D + D/2
    cherry_y = int(cherry/W)*D + D/2
    dirty_rects.append(pygame.draw.rect(window, RED, (cherry_x, cherry_y, D, D)))
    
    previous_x = ((W if (previous%W) == 0 else (previous%W))-1)*D + D/2
    previous_y = int(previous/W)*D + D/2
    dirty_rects.append(pygame.draw.rect(window, BLACK, (previous_x, previous_y, D, D)))
    
    for i, pos in enumerate(snake):
        x_pos = ((W if (pos%W) == 0 else (pos%W))-1)*D + D/2 
        y_pos = int(pos/W)*D + D/2
        dirty_rects.append(pygame.draw.rect(window, BLACK, (x_pos, y_pos, D, D)))
        dirty_rects.append(pygame.draw.rect(window, WHITE, (x_pos +1, y_pos+ 1, D-2, D-2)))
        
    return dirty_rects

def draw_over(window, last):
    dirty_rects = []
    
    for i, pos in enumerate(last):
        x_pos = ((W if (pos%W) == 0 else (pos%W))-1)*D + D/2 
        y_pos = int(pos/W)*D + D/2
        dirty_rects.append(pygame.draw.rect(window, BLACK, (x_pos, y_pos, D, D)))
    return dirty_rects

def main():
    global cherry
    global snake
    
    previous = 0
    
    pygame.init()
    window = pygame.display.set_mode((W*D + D, H*D + D))
    pygame.display.set_caption("cherry and a small snake")

    pygame.draw.rect(window, WHITE, (0, 0, W*D + D, H*D + D))
    pygame.draw.rect(window, BLACK, (int(D/2), int(D/2), W*D, H*D))
    pygame.display.update()
    
    clock = pygame.time.Clock()
    
    for i in range(N):
        cherry = random.randint(1, W*H)
        snake = deque()
        snake.append(random.randint(1, W*H))

        if not cherry:
            possible_cherry = set(range(W*H)) - set(snake)
            if possible_cherry:
                cherry = random.choice(list(possible_cherry))
            else:
                exit()
    
        while cherry:
            for pos in (list(snake)):
                dist = dist_to_cherry(pos)
                mv = random.choice(next_step(pos, dist))
                snake.appendleft(pos + mv)
                if snake[0] != cherry:
                    previous = snake.pop()
            
            pygame.display.update(draw(window, previous))
            clock.tick(10)
            if snake[0] == cherry:
                cherry = None
        else:
            last = snake
            pygame.display.update(draw_over(window, last))

    time.sleep(0.3)
    pygame.display.quit()
    pygame.quit()
    
main()