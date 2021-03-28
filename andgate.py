# Project 1: Logic gates using Conway's game of life

import pygame, sys, random, numpy as np
import time
size=(w,h)=1500,700
pygame.init()
win=pygame.display.set_mode(size)
clock=pygame.time.Clock()
s=10
cols,rows=int(win.get_width()/s), int(win.get_height()/s)
print(rows,cols)

glider_gun=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
 [0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
inverted_glider_gun=np.flip(glider_gun,1)
grid = np.zeros((70, 150))
grid[2:17,4:46] = glider_gun
grid[2:17,44:86]= glider_gun
grid[1:16,87:129]= inverted_glider_gun

def count(grid, x, y):
    c = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            col = (y+j+cols)%cols
            row = (x+i+rows)%rows
            c += grid[row][col]
    c -= grid[x][y]
    return c

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    win.fill((0,0,0))
    grid2=grid
    for i in range(cols):
        for j in range(rows):
            x = i * s
            y = j * s
            if grid[j][i] == 1:
                pygame.draw.rect(win, (255, 255, 255), (x, y, s, s))
            elif grid[j][i] == 0:
                pygame.draw.rect(win, (0, 0, 0), (x, y, s, s))
            pygame.draw.line(win, (20, 20, 20), (x,y), (x, h))
            pygame.draw.line(win, (20, 20, 20), (x,y), (w,y))
#win.fill((0,0,0))
    new_grid = []
    for i in range(rows):
        a = []
        for j in range(cols):
            a.append(0)
        new_grid.append(a)


    for i in range(cols):
        for j in range(rows):
            if(i!=0 and j!=0 and i!=cols and j!=rows):
                neighbors = count(grid, j, i)
                state = grid[j][i]
                if state == 0 and neighbors == 3 :
                    new_grid[j][i] = 1
                elif state == 1 and (neighbors < 2 or neighbors > 3):
                    new_grid[j][i] = 0
                else:
                    new_grid[j][i] = state
    grid = new_grid
    pygame.display.flip()
    clock.tick(70)
