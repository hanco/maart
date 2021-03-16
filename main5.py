from grid3 import Cell
from more_itertools import powerset
from copy import deepcopy

with open('grid.txt') as f:
    grid_data = [i.split() for i in f.readlines()]

print(grid_data)
unselected = []

def print_grid(x):
    for i in range(len(x)):
        line = x[i]
        regel =""
        for y in line:
            regel += (" "*6 + (str(y)))[-6:]
        print(regel)

def grid_convert(g):
    grid = [[0 for x in range(len(g))] for y in range(len(g))]
    for x in range(len(g)):
        for y in range(len(g)):
            grid[x][y] = int(g[x][y], 16)
    return grid

def make_object(grid):
    global objects
    objects = [[0 for x in range(len(grid))] for y in range(len(grid))]
    for y in range(len(grid)):
        for x in range(len(grid)):
            objects[y][x] = Cell(y, x, grid[y][x]-128, len(grid))
    return

def start():
    global objects, unselected
    for line in reversed(objects):
        choicelist = []
        for x in line:
            if x.total() < 0:
                unselected.append([x.y, x.x])
                x.selected = False
            else:
                choicelist.append([x.y, x.x])
        choicelist= list(powerset(choicelist))
        unselected = choice(choicelist, line[0].y)
        for row, col in unselected:
            object = objects[row][col]
            if object.selected:
                object.selected = False
        for line in  reversed(objects):
            for obj in line:
                extra = 0
                followers = obj.followers()
                for row, col in followers:
                    follower = objects[row][col]
                    if follower.selected:
                        extra += follower.total()
                obj.extra = extra

    return

def choice(choicelist, y):
    maxscore = [0, []]
    for row in choicelist:
        lines = deepcopy(objects[-(y*len(objects)):])
        if row:
            for col in row:
                if col:
                    lines[col[0]][col[1]].selected = False
        for row in range(len(lines)):
            for obj in lines[row]:
                if not obj.selected:
                    followers = obj.followers()
                    for y, x in followers:
                        if lines[y][x].selected:
                            lines[y][x].selected = False
        score = values(lines)
        if score > maxscore[0]:

            maxscore[0] = score
            maxscore[1] = unselect(lines)
    print(maxscore[0])
    return maxscore[1]

def values(lines):
    score = 0
    for row in lines:
        for col in row:
            if col.selected:
                score += col.value

    return score

def unselect(lines):
    u = []
    for row in lines:
        for col in row:
            if not col.selected:
                u.append([col.y, col.x])

    return u


grid = grid_convert(grid_data)
print_grid(grid)
make_object(grid)
start()
print(unselected)
for row in objects:
    for col in row:
        if [col.y, col.x] not in unselected:
            col.selected = True
        else:
            col.selected = False
print(values(objects))

