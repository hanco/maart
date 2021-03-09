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
    global object
    object = [[0 for x in range(len(grid))] for y in range(len(grid))]
    for y in range(len(grid)):
        for x in range(len(grid)):
            object[y][x] = Cell( y , x , grid[y][x]-128, len(grid))
    return

def select(g):
    unselected = []
    max = 0
    for y in reversed(range(len(g))):
        for x in range(len(g)):
                      if object[y][x].selected:
                selected.append([y, x, object[y][x].value ])
                total += object[y][x].value - 128
            else:
                unselected.append([y, x, object[y][x].value])



grid = grid_convert(grid_data)
print_grid(grid)
make_object(grid)
update_object(grid)

#remove(object)
#update_object(grid)
#remove(object)
#gridnew = grid_object(len(grid))
#print_grid(gridnew)
select , total , unselect = select(grid)
print(total)
print(len(select))
print(select)
print(unselect)

