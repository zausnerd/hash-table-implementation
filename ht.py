
class HashTable:
    class Entry:
        def __init__(self, key=None, val=None):
            self.key = key
            self.val = val
            self.next = None

    def __init__(self, capacity=100):
        self.size = 0
        self.capacity = capacity
        self.table = [None for i in range(0, self.capacity)]

    def get_load_factor(self):
        return self.size / self.capacity

    def get_idx(self, key):
        return hash(key) % self.capacity

    def get(self, key):
        entry = self.table[self.get_idx(key)]
        while entry is not None:
            if entry.key == key:
                return entry.val
            entry = entry.next
        raise KeyError(key)

    def set(self, key, val):
        idx = self.get_idx(key)
        entry = self.table[idx]
        if entry is not None and entry.key == key:
            entry.val = val
            return
        if self.table[idx] is None:
            self.table[idx] = self.Entry(key, val)
        else:
            while entry.next is not None:
                if entry.key == key:
                    entry.val = val
                    return
                entry = entry.next
            entry.next = self.Entry(key, val)
        self.size += 1
        if self.get_load_factor() >= 0.5:
            self.resize()
        return

    def delete(self, key):
        idx = self.get_idx(key)
        if self.table[idx] is None:
            raise KeyError(key)
        else:
            entry = self.table[idx]
            if entry.key == key:
                self.table[idx] = entry.next
                self.size -= 1
                return
            while entry is not None:
                next_entry = entry.next
                if next_entry is not None and next_entry.key == key:
                    entry.next = next_entry.next
                    self.size -= 1
                    return
                entry = entry.next
            raise KeyError(key)

    def resize(self):
        old_table = self.table
        self.table = [None for i in range(0, self.capacity * 2)]
        self.capacity = self.capacity * 2
        self.size = 0
        for element in old_table:
            if element is not None:
                entry = element
                while entry is not None:
                    self.set(entry.key, entry.val)
                    entry = entry.next
