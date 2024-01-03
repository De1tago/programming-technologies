#linear probing
class ClosedHashing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        if self.table[index] is None:
            self.table[index] = (key, value)
        else:
            # Linear Probing
            while self.table[index] is not None:
                index = (index + 1) % self.size
            self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size

        return None

    def delete(self, key):
        index = self.hash_function(key)

        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return
            index = (index + 1) % self.size

    def display(self):
        for i in range(self.size):
            if self.table[i] is not None:
                print(f"Key: {self.table[i][0]}, Value: {self.table[i][1]}")
hash_table = ClosedHashing(5)

hash_table.insert(1, "apple")
hash_table.insert(2, "banana")
hash_table.insert(7, "orange")
hash_table.insert(8, "grape")
hash_table.insert(11, "watermelon")

hash_table.display()

print(hash_table.search(7))
hash_table.delete(2)

hash_table.display()
