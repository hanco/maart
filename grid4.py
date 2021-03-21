class Cell:
    def __init__(self, y, x, value):
        self.y = y
        self.x = x
        self.value = value
        self.selected = False

    def children(self, n):
        y = self.y + 1
        return self.make_list(y, n)

    def parents(self, n):
        y = self.y - 1
        return self.make_list(y, n)

    def make_list(self, y, n):
        list = []
        if not self.on_grid(n, y):
            return list
        for x in range((self.x-1), (self.x+2)):
            if self.on_grid(n, x):
                list.append([y, x])
        return list

    def on_grid(self, n, x):
        if x >= 0 and x < n:
            return True
        return False


