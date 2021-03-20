from grid3 import Cell

with open('grid.txt') as f:
    grid_data = [i.split() for i in f.readlines()]

print(grid_data)

def print_grid(x):
    for i in range(len(x)):
        line = x[i]
        regel =""
        for y in line:
            regel += (" "*6 + (str(y-128)))[-6:]
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
        children_value = [0, 0, 0]
        deducted = 0
        # from children_value[1]
        for col in reversed(row):
            children_value = value_of_children(col.y , col.x , children_value, deducted) # remove first_value
            total = col.total()
            if total < 0:
                if total + sum(children_value) < 0:
                    col.selected = False
                    remove_children(col)
        #update_extra(row)

    return

def value_of_children(y, x, children_value, deducted):
    if y < len(grid_data)-1:
        if x > 0:
            child = objects[y-1][x-1]
            children_value[0] = child.value + child.child[2]
        child = objects[y - 1][x]
        children_value[1] = child.value + sum(child.child)
        if x < len(grid_data)-1:
            child = objects[y - 1][x + 1]
            children_value[2] = child.value + child.child[2]
        for value in children_value:
            if value >= deducted:
                value -= deducted
                deducted = 0
            else:
                deducted -= value
                value = 0
    return children_value


    # must include old_value

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
                            parent_object.child = 0
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
                        parent_object.child[x] = value
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
        grandchildren = objects[row]
        for grandchild in grandchildren:
            if grandchild.selected:
                value = grandchild.totalandchild()
                x = grandchild.x
                objects[row - 1][x].child = value

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

grid = grid_convert(grid_data)
print_grid(grid)
make_object(grid)
start()
print(unselect(objects))
print(values(objects))

