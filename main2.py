from grid3 import Cell

with open('grid.txt') as f:
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
    global object
    object = [[0 for x in range(len(grid))] for y in range(len(grid))]
    for y in range(len(grid)):
        for x in range(len(grid)):
            object[y][x] = Cell(y, x, grid[y][x]-128, len(grid))
    return

def update_object(g):
    global object
    for y in reversed(range(len(g))):
        for x in range(len(g)):
            object[y][x].extra = 0
            for y2, x2 in object[y][x].followers():
                cell = object[y2][x2]
                cell.update()
                if not cell.selected :
                    continue
                object[y][x].extra += cell.total()
            object[y][x].update()
    return

def object2grid(g):
    grid = [[0 for x in range(len(g))] for y in range(len(g))]
    for y in range(len(grid)):
        for x in range(len(grid)):
            value = object[y][x].total()
            print(object[y][x].selected)
            if not object[y][x].selected:
                value = 0
            grid[y][x] = value
    return grid

def select(g):
    unselected = []
    selected = []
    total = 0
    for y in reversed(range(len(g))):
        for x in range(len(g)):
            if object[y][x].selected and possible(object[y][x]):
                selected.append([y, x, object[y][x].value ])
                total += object[y][x].value
            else:
                unselected.append([y, x, object[y][x].value])
    return selected, total, unselected

def possible(cell):
    for y, x in cell.followed():
        if not object[y][x].selected:
            return False
        else:
            continue
    return True

grid = grid_convert(grid_data)
print_grid(grid)
make_object(grid)
update_object(grid)
print_grid(grid)
grid_object = object2grid(grid)
print_grid(grid_object)


selected, total , unselected = select(grid)
update_object(grid)
selected, total , unselected = select(grid)
print(total)
print(len(selected))
print(selected)
print(unselected)

