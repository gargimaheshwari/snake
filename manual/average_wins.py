# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 14:36:06 2018

@author: Gargi
"""

import pygame
import random
from queue import deque

D = 10
W = 40
H = 30
N = 1000

LEFT, RIGHT, UP, DOWN = -1, 1, -W, W
MOVES = (LEFT, RIGHT, UP, DOWN)

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
    cherry_pos_x = ((W if (cherry%W) == 0 else (cherry%W))-1)
    cherry_pos_y = int(cherry/W)
    
    snake_pos_x = ((W if (pos%W) == 0 else (pos%W))-1)
    snake_pos_y = int(pos/W)
    
    x_dist = cherry_pos_x - snake_pos_x
    y_dist = cherry_pos_y - snake_pos_y
    return((x_dist, y_dist))
    
def move_towards_centre(pos, possibles):
    for mv in possibles:
        if (pos+mv < pos) and pos+mv != 0:
            return mv

def next_step(pos, dist):
    possibles  = [mv for mv in MOVES if mv+pos not in list(snake)[:]]
    move_possibles = []
    for mv in possibles:
        if ((mv+pos)%W == 1 and pos%W == 0) or ((mv+pos)%W == 0 and pos%W == 1):
            continue
        if pos == 0 and (mv == -40 or mv == -1):
            continue
        if possible_moves(mv, pos):
            if abs(dist_to_cherry(mv+pos)[0]) <= abs(dist[0]) and abs(dist_to_cherry(mv+pos)[1]) <= abs(dist[1]):
                move_possibles.append(mv)
    if not(move_possibles):
        move_possibles.append(move_towards_centre(pos, possibles))
    return(move_possibles)

def main():
    global cherry
    global snake
    snake.append(random.randint(0, W*H-1))
    cherry = random.randint(0, W*H-1)

    clock = pygame.time.Clock()
    
    for i in range(N):
        
        if not cherry:
            possible_cherry = set(range(W*H)) - set(snake)
            if possible_cherry:
                cherry = random.choice(list(possible_cherry))
            else:
                exit()
        while cherry:
            pos = snake[0]
            dist = dist_to_cherry(pos)
            step = next_step(pos, dist)
            if step[0]:
                mv = random.choice(step)
            else:
                break
            snake.appendleft(pos + mv)
            if snake[0] != cherry:
                snake.pop()
            clock.tick(500)
            if snake[0] == cherry:
                cherry = None
        
        if not step[0]:
            break
            
    return(i+1)
    
sum = 0
pygame.init()

M = 10
for k in range(M):
    cherry = None
    snake = deque()
    sum += main()

pygame.quit()

print(sum/M)