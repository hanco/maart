from grid3 import Cell

with open('small.txt') as f:
    grid_data = [i.split() for i in f.readlines()]

print(grid_data)

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
    for row in reversed(objects):
        update_child(row[0].y)
        for col in reversed(row):
            total = col.total()
            if total < 0:
                col.selected = False
                remove_children(col)
        update_extra(row)

    return

def remove_children(object):
    global objects
    children = object.children()
    for child in children:
        child_object = objects[child[0]][child[1]]
        if child_object.selected:
            child_object.selected = False
            parents = child_object.parents()
            for parent in parents:
                parent_object = objects[parent[0]][parent[1]]
                if parent_object.selected:
                    for x in range(3):
                        if parent_object.x == child_object.x -(x-1):
                            parent_object.extra[x] = 0
                            parent_object.child[x] = 0
            remove_children(child_object)

    return

def update_extra(row):
    global objects
    for col in row:
        if col.selected:
            value = col.total()
            parents = col.parents()
            for parent in parents:
                parent_object = objects[parent[0]][parent[1]]
                total = parent_object.total()
                for x in range(3):
                    if parent_object.x == col.x -(x-1):
                        if total < 0:
                            if total + value >=0:
                                parent_object.extra[x] = -total
                                value += total
                            else:
                                parent_object.extra[x] = value
                                value = 0

    return

def update_child(y):
    global objects
    row = y + 2
    if row < len(grid_data):
        grandchildren = objects[row]:
        for grandchild in grandchildren:
            if grandchild.selected:
                value = grandchild.totalandchild()
                x = grandchild.x:
                objects[row - 1][x] = value

    return

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

def check_children():
    selected = []
    for row in reversed(objects):
        for col in row:
            if col.selected:
                selected.append([col.y, col.x])
                for parent in col.parents():
                    if objects[parent[0]][parent[1]].selected:
                        continue
                    else:
                        return [col.y , col.x]
    return selected



grid = grid_convert(grid_data)
print_grid(grid)
make_object(grid)
start()
print(check_children())
print(values(objects))

