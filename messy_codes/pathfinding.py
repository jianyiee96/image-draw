import cv2
import cv2_util
import numpy as np

def dfs(mtx, curr_idx, x, y):   
    
    mtx[x][y] = curr_idx

    if(x != 0 and mtx[x-1][y] == 0):
        dfs(mtx, curr_idx, x-1, y)
    if(y != 0 and mtx[x][y-1] == 0):
        dfs(mtx, curr_idx, x, y-1)
    if(x != len(mtx)-1 and mtx[x+1][y] == 0):
        dfs(mtx, curr_idx, x+1, y)
    if(y != len(mtx[x])-1 and mtx[x][y+1] == 0):
        dfs(mtx, curr_idx, x, y+1)

def bfs(mtx, curr_idx, x, y):   
    
    queue = []
    queue.append((x,y))
    while queue:
        s = queue.pop(0)
        x = s[0]
        y = s[1]

        if(x != 0 and mtx[x-1][y] == 0):
            queue.append((x-1,y))
            mtx[x-1][y] = curr_idx

        if(y != 0 and mtx[x][y-1] == 0):
            queue.append((x,y-1))
            mtx[x][y-1] = curr_idx

        if(x != len(mtx)-1 and mtx[x+1][y] == 0):
            queue.append((x+1,y))
            mtx[x+1][y] = curr_idx

        if(y != len(mtx[x])-1 and mtx[x][y+1] == 0):
            queue.append((x,y+1))
            mtx[x][y+1] = curr_idx

def group_sections(mtx):
    curr_idx = 1

    for x in range(0,len(mtx)):
        for y in range(0,len(mtx[x])):
            if(mtx[x][y] == 0):
                bfs(mtx, curr_idx, x, y)
                curr_idx = curr_idx + 1
                
