from grid3 import Cell

with open('small.txt') as f:
    grid_data = [i.split() for i in f.readlines()]

print(grid_data)
selected = [[y, x] for y in range(len(grid_data)) for x in range(len(grid_data))]
checked = []
TheList = []

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
    global object
    object = [[0 for x in range(len(grid))] for y in range(len(grid))]
    for y in range(len(grid)):
        for x in range(len(grid)):
            object[y][x] = Cell(y, x, grid[y][x]-128, len(grid))
    return

def select(selected):
    l = list(selected)
    if l:
        y, x= l[0]
        if not object[y][x].followers():
            if object[y][x].value < 0:
                l.remove([y, x])
        else:
            l.remove([y, x])
            unselect = remove_followers([y, x], l)
            select = choice([unselect, selected])

    return select


def choice(lists):
    values = [0, 0]
    for x in range(2):
        for cell in lists[x]:
            values[x] += object[cell[0]][cell[1]].value
    if values[0] > values[1]:
        return lists[0]
    return lists[1]

def remove_followers(cell, selected):
    unselect = list(selected)
    followers = object[cell[0]][cell[1]].followers()
    for y, x in followers:
        if [y, x] in unselect:
            unselect.remove([y, x])
            unselect = remove_followers([y, x], unselect)
    return unselect

def add_followers(cell , selected):
    line = cell.y
    for y, x in selected:
        if y == line:
            followers = object[y][x].followers()
            for Y, X in followers:
                remove = []
                followed = object[Y][X].followed()
                for c in followed:
                    if c in selected:
                        continue
                    else:
                        remove.append([Y, X])
                for c in remove:
                    if c in followers:
                        followers.remove(c)
            for cell in followers:
                if not cell in selected:
                    selected.append(cell)
    return selected


grid = grid_convert(grid_data)
print_grid(grid)
make_object(grid)
selection = select(selected)
print(selection)
print(TheList)
print(len(TheList))
total = 0
for y, x in TheList:
    total += object[y][x].value
print(total)
