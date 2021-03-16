class Cell:
    def __init__(self, y, x, value, n):
        self.y = y
        self.x = x
        self.value = value
        self.n = n
        self.extra = [0, 0, 0]
        self.child = 0
        self.selected = True

    def children(self):
        y = self.y + 1
        return self.make_list(y)

    def parents(self):
        y = self.y - 1
        return self.make_list(y)

    def total(self):
        total = sum(self.extra, self.value)
        return total

    def totalandchild(self):
        total = self.child + self.value
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


