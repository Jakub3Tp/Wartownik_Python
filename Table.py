import random

class Table:
    def __init__(self, size=50, min=1, max=100):
        self.size = size
        self.min = min
        self.max = max
        self.n = []
        self.Fill()

    def Fill(self):
        self.n = [random.randint(self.min, self.max) for i in range(self.size)]

    def Search(self, value):
        for i, element in enumerate(self.n):
            if element == value:
                return i
        return -1

    def get_n(self):
        return self.n