from grid3 import Cell

with open('small.txt') as f:
    grid_data = [i.split() for i in f.readlines()]

print(grid_data)
selected = []
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

def select(selected, cell, value):
    checked.append([cell.y,cell.x])
    list1 = list(selected)
    list1.remove([cell.y,cell.x])
    lists = [list1, selected]
    for x in range(2):
        lists[x] = add_followers(cell, lists[x])
    values = choice(lists)
    if values[0] > values[1]:
        max_list = list1
        value += values[0]
    else:
        max_list = lists[1]
        value += values[1]
    for cell in max_list:
        if cell in checked:
            continue
        else:
            select(max_list, object[cell[0]][cell[1]], value)
    return TheList


def choice(lists):
    values = [0, 0]
    for x in range(2):
        values[x] = 0
        for cell in lists[x]:
            values[x] += object[cell[0]][cell[1]].value
    return values

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
selected = [[0, x] for x in range(len(grid))]
selection = select(selected, object[0][0], 0)
print(selection)
print(TheList)
print(len(TheList))
total = 0
for y, x in TheList:
    total += object[y][x].value
print(total)
