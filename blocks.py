# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 01:55:59 2018

@author: Gargi
"""

import pygame
import random
from queue import deque
from pygame.color import Color
import time

d = 10
w = 40
h = 30
n = 100

snake = deque()

black = Color("black")
white = Color("white")
   
def draw_rects(window):
    
    dirty_rects = []
    
    for i, pos in enumerate(snake):
        
        x_pos = ((w if (pos%w) == 0 else (pos%w))-1)*d + d/2
        y_pos = int(pos/w)*d + d/2
        dirty_rects.append(pygame.draw.rect(window, black, (x_pos, y_pos, d, d), 1))
        dirty_rects.append(pygame.draw.rect(window, white, (x_pos +1, y_pos+ 1, d-2, d-2)))
        
    return(dirty_rects)

def main():
    
    pygame.init()
    window = pygame.display.set_mode((d*w + d, d*h + d))
    pygame.display.set_caption("blocks on a screen")

    snake.append(random.randint(1, w*h))
    
    pygame.draw.rect(window, white, (0, 0, w*d+d, h*d+d))
    pygame.draw.rect(window, black, (int(d/2), int(d/2), w*d,h*d))
    
    pygame.display.update()
    
    clock = pygame.time.Clock()
    
    for i in range(n):
        possible_box = set(range(w*h)) - set(snake)
        snake.append(random.choice(list(possible_box)))
        pygame.display.update(draw_rects(window))
        clock.tick(30)
    
    time.sleep(0.3)
    pygame.display.quit()
    pygame.quit()
    
main()