class CollectionClass:
    def __init__(self, items):
        self.items = items

    def items(self):
        self.items

    def delete_all(self):
        while len(self.items) > 0:
            item = self.items.pop()
            item.delete()
        return True
