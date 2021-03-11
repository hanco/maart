from grid3 import Cell

with open('grid.txt') as f:
    grid_data = [i.split() for i in f.readlines()]

print(grid_data)
selected = []
n = 20


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
            object[y][x] = Cell(y, x, grid[y][x]-128, len(grid))
    return

def select():
    global selected
    for y in range(n):
        for x in range(n):
            if available(y, x):
                if object[y][x].value >= 0:
                    selected.append([y, x])
                elif positive(y, x, value = object[y][x].value  ) >= 0:
                    selected.append([y, x])
                else:
                    continue
    return

def positive(y , x , value):

    followers = object[y][x].followers()
    for follower in followers:
        follower_value = object[follower[0]][follower[1]].value
        value += follower_value
        if value >= 0:
                return value
        elif positive(follower[0], follower[1], value) >= 0:
            return value
    return value

def available(y , x):
    followed = object[y][x].followed()
    for follow in followed:
        if follow not in selected:
            return False
    return True




grid = grid_convert(grid_data)
print_grid(grid)
make_object(grid)
select()
print(selected)
print(len(selected))
total = 0
for y, x in selected:
    total += object[y][x].value
print(total)

