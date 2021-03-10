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

    def update(self):
        if self.total() < 0 and self.selected:
            self.selected = False
        return

    def remove_selected(self, grid):
        if self.total() < 0:
            self.selected = False
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


