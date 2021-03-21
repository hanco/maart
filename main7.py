from grid4 import Cell

with open('grid.txt') as f:
    grid_data = [i.split() for i in f.readlines()]

print(grid_data)
n = len(grid_data)

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
    global objects
    for y in range(n):
        for x in range(n):
            object = objects[y][x]
            if object.value > 0:
                object.selected = True
            elif children_selected:
                object.selected = True

    return

def try_remove():
    global objects
    for y in reversed(range(n)):
        for x in range(n):
            object = objects[y][x]
            if object.value < 0:
                remove_list = all_selected_children(y, x)
                if listvalue(remove_list) > 0:
                    continue
                else:
                    for Y, X in remove_list:
                        objects[Y][X].selected = False
    print(values(objects))

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

def all_selected_children(y, x):
    allchildren = [[y, x]]
    for row in range(y, n):
        a = x-(row-y)
        if a < 0:
            a = 0
        b = x+(row-y) + 1
        if b > n:
            b = n
        for col in range(a, (b)):
            if objects[row][col].selected:
                allchildren.append([row, col])

    return allchildren

def values(grid):
    score = 0
    for row in grid:
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

if __name__ == '__main__':
    grid = grid_convert(grid_data)
    print_grid(grid)
    make_object(grid)
    start()
    print(values(objects))
    try_remove()
    print(values(objects))
    try_remove()
    print_objects(objects)
    print(objects[2][10].selected)
