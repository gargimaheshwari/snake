# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 14:40:35 2018

@author: Gargi
"""

import pygame
import random
from queue import deque
from pygame.color import Color
import time

D = 10
W = 40
H = 30
N = 50

BLACK = Color("black")
WHITE = Color("white")
RED = Color("red")

LEFT, RIGHT, UP, DOWN = -1, 1, -W, W
MOVES = (LEFT, RIGHT, UP, DOWN)

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
    
def draw(window, previous):
    
    dirty_rects = []

    cherry_x = ((W if (cherry%W) == 0 else (cherry%W))-1)*D + D/2
    cherry_y = int(cherry/W)*D + D/2
    dirty_rects.append(pygame.draw.rect(window, RED, (cherry_x, cherry_y, D, D)))

    for i, pos in enumerate(snake):
        x_pos = ((W if (pos%W) == 0 else (pos%W))-1)*D + D/2 
        y_pos = int(pos/W)*D + D/2
        dirty_rects.append(pygame.draw.rect(window, BLACK, (x_pos, y_pos, D, D), 1))
        dirty_rects.append(pygame.draw.rect(window, WHITE, (x_pos +1, y_pos+ 1, D-2, D-2)))


    previous_x = ((W if (previous%W) == 0 else (previous%W))-1)*D + D/2
    previous_y = int(previous/W)*D + D/2
    dirty_rects.append(pygame.draw.rect(window, BLACK, (previous_x, previous_y, D, D)))
        
    return(dirty_rects)


def main():
    global cherry
    global snake

    pygame.init()
    window = pygame.display.set_mode((D*W + D, D*H + D))
    pygame.display.set_caption("cherry and a snake")
    
    pygame.draw.rect(window, WHITE, (0, 0, W*D+D, H*D+D))
    pygame.draw.rect(window, BLACK, (int(D/2), int(D/2), W*D,H*D))
    pygame.display.update()
    
    snake.append(random.randint(0, W*H-1))
    cherry = random.randint(0, W*H-1)
    clock = pygame.time.Clock()
    
    for i in range(N):
        pygame.display.set_caption("cherry and a snake \n cherry: " + str(i+1))

        previous = 0
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
                print("Snake dead at " + str(i+1) + "th cherry")
                break
            snake.appendleft(pos + mv)
            if snake[0] != cherry:
                previous = snake.pop()
            pygame.display.update(draw(window, previous))
            clock.tick(30)
            if snake[0] == cherry:
                cherry = None
        if not step[0]:
            break
    time.sleep(0.3)
    pygame.display.quit()
    pygame.quit()
    
main()
