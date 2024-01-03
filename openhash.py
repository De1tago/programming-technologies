#open hashing chains
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def __hash_function(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self.__hash_function(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = Node(key, value)

    def get(self, key):
        index = self.__hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(key)

    def remove(self, key):
        index = self.__hash_function(key)
        current = self.table[index]
        previous = None
        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                return
            previous = current
            current = current.next
        raise KeyError(key)
hash_table = HashTable(10)
hash_table.put('apple', 5)
hash_table.put('banana', 7)
print(hash_table.get('apple'))  # Output: 5
print(hash_table.get('banana'))  # Output: 7
hash_table.remove('banana')
#print(hash_table.get('banana'))  # Raises KeyError
