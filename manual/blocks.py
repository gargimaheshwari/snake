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

# Dimensions of the screen
D = 10 # resolution
W = 40 # Width
H = 30 # Height
N = 100 # number of blocks

blocks = deque() # stores the locations of the blocks

#colours for the background and the squares
BLACK = Color("black")
WHITE = Color("white")
   
def draw_rects(window): # This function draws only new squares and sends them to pygame update function
    
    dirty_rects = []
    
    for i, pos in enumerate(blocks):
        
        x_pos = ((W if (pos%W) == 0 else (pos%W))-1)*D + D/2
        y_pos = int(pos/W)*D + D/2
        dirty_rects.append(pygame.draw.rect(window, BLACK, (x_pos, y_pos, D, D), 1))
        dirty_rects.append(pygame.draw.rect(window, WHITE, (x_pos +1, y_pos+ 1, D-2, D-2)))
        
    return(dirty_rects)

def main():
    
    pygame.init()
    window = pygame.display.set_mode((D*W + D, D*H + D))
    pygame.display.set_caption("blocks on a screen")
    
    # Draw the screen
    pygame.draw.rect(window, WHITE, (0, 0, W*D + D, H*D + D))
    pygame.draw.rect(window, BLACK, (int(D/2), int(D/2), W*D, H*D))    
    pygame.display.update()
    
    clock = pygame.time.Clock()
    
    for i in range(N):
        possible_box = set(range(W*H)) - set(blocks)
        blocks.append(random.choice(list(possible_box)))
        pygame.display.update(draw_rects(window)) # Update only to draw squares
        clock.tick(30)
    
    time.sleep(0.3)
    pygame.display.quit()
    pygame.quit()
    
main()
