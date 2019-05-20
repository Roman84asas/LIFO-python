class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueu(self, item):
        self.items.insert(0, item)

    def dequeu(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
