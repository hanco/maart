class Cell:
    def __init__(self, y, x, value, n):
        self.y = y
        self.x = x
        self.value = value
        self.extra = 0
        self.n = n
        self.selected = True

    def followers(self):
        y = self.y + 1
        return self.make_list(y)

    def followed(self):
        y = self.y - 1
        return self.make_list(y)

    def update(self, grid):
        self.extra = 0
        for y, x in self.followed():
            self.extra += grid[y][x].total() - 128
        if self.total() < 128 and self.selected:
            self.selected = False
            self.remove_followers(grid)
        return

    def remove_followers(self, grid):
        for y, x in self.followers():
            if grid[y][x].selected:
                grid[y][x].selected = False
                grid[y][x].remove_followers(grid)
        return

    def remove_selected(self, grid):
        if self.total() < 128:
            self.selected = False
            self.changed(grid)
        return

    def changed(self,grid):
        if not self.selected:
            deselect = self.followers()
            for y, x in deselect:
                if grid[y][x].selected:
                    grid[y][x].selected = False
                    grid[y][x].changed(grid)
                    for y in reversed(range(len(grid))):
                        for x in range(len(grid)):
                            grid[y][x].update(grid)
        return

    def total(self):
        total = self.value + self.extra
        return total

    def make_list(self, y):
        list = []
        if not self.on_grid(self.n, y):
            return list
        for x in range((self.x-1), (self.x+2)):
            if self.on_grid(self.n, x):
                list.append([y, x])
        return list

    def on_grid(self, n, x):
        if x >= 0 and x < n:
            return True
        return False


