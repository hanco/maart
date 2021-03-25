from grid4 import Cell
import random

with open('grid.txt') as f:
    grid_data = [i.split() for i in f.readlines()]

print(grid_data)
n = len(grid_data)
max_score = 0


def print_grid(x):
    for i in range(n):
        line = x[i]
        regel =""
        for y in line:
            regel += (" "*6 + (str(y-128)))[-6:]
        print(regel)

def grid_convert(g):
    grid = [[0 for x in range(n)] for y in range(n)]
    for x in range(n):
        for y in range(n):
            grid[x][y] = int(g[x][y], 16)
    return grid

def make_object(grid):
    global objects
    objects = [[0 for x in range(n)] for y in range(n)]
    for y in range(n):
        for x in range(n):
            objects[y][x] = Cell(y, x, grid[y][x]-128)
    return

def print_objects(objects):
    grid = [[0 for x in range(n)] for y in range(n)]
    for y in range(n):
        regel = ""
        for x in range(n):
            object = objects[y][x]
            value = object.value
            if not object.selected:
                value = 0
            grid[x][y] = value
            regel += (" "*6 + (str(value)))[-6:]
        print(regel)
    return


def start():
    global max_score , max_list
    # for y in reversed(range(n)):
    #     for x in range(n):
    #         object = objects[y][x]
    #         if object.value > 0:
    #             object.selected = True
    #         elif children_selected(object):
    #             object.selected = True
    divider = 1000
    while divider > 1:
        selected = list_of_possibles()
        row, col = random.choice(selected)
        object = objects[row][col]
        value = object.value
        if object.selected:
            value = -value
        if value > 0:
            object.selected = not object.selected
        elif -value / divider < random.random():
            object.selected = not object.selected
        divider -= 0.005
        score = values(objects)
        if score > max_score:
            max_score = score
            max_list = selecting_list()
            print(score, int(divider), max_score)
    print(max_score)

    return

def listvalue(l):
    value = 0
    for y, x in l:
        value += objects[y][x].value
    return value

def children_selected(object):
    children = object.children(n)
    for y, x in children:
        if objects[y][x].selected:
            return True
    return False

def values(grid):
    score = 0
    for row in grid:
        for col in row:
            if col.selected:
                score += col.value

    return score

def list_of_possibles():
    selected = []
    for row in range(n):
        for col in range(n):
            object = objects[row][col]
            pos = (row, col)
            if possible(object) and not object.selected:
                selected.append([row, col])
            elif object.selected and not has_children(object):
                selected.append([row, col])

    return selected

def has_children(object):
    for child in object.children(n):
        if objects[child[0]][child[1]].selected:
            return True
        else:
            continue
    return False


def possible(cell):
    for y, x in cell.parents(n):
        if not objects[y][x].selected:
            return False
        else:
            continue
    return True

def selecting_list():
    l = []
    for row in range(n):
        for col in range(n):
            if objects[row][col].selected:
                l.append((row, col))

    return l

def check_solution():
    value = 0
    for row, col in max_list:
        object = objects[row][col]
        if possible(object):
            value += object.value
        else:
            return (object.y , object.x)

    return value



if __name__ == '__main__':
    grid = grid_convert(grid_data)
    print_grid(grid)
    make_object(grid)
    start()
    start()
    start()
    start()
    print(values(objects))
    print_objects(objects)
    print(max_score)
    print(max_list)
    print(check_solution())


