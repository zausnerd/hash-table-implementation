
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
        ptr = self.table[self.get_idx(key)]
        while ptr != None:
            if ptr.key == key:
                return ptr.val
            ptr = ptr.next
        raise KeyError(key)

    def set(self, key, val):
        idx = self.get_idx(key)
        ptr = self.table[idx]
        if ptr != None and ptr.key == key:
            ptr.val = val
            return
        if self.table[idx] == None:
            self.table[idx] = self.Entry(key, val)
        else:
            while ptr.next != None:
                if ptr.key == key:
                    ptr.val = val
                    return
                ptr = ptr.next
            ptr.next = self.Entry(key, val)
        self.size += 1    
        if self.get_load_factor() >= 0.5:
            self.resize()
        return

    def delete(self, key):
        idx = self.get_idx(key)
        if self.table[idx] == None:
            raise KeyError(key)
        else:
            ptr = self.table[idx]
            if ptr.key == key:
                self.table[idx] = ptr.next
                self.size -= 1
                return
            while ptr != None:
                next_ptr = ptr.next
                if next_ptr != None and next_ptr.key == key:
                    ptr.next = next_ptr.next
                    self.size -= 1 
                    return
                ptr = ptr.next
            raise KeyError(key)            
    
    def resize(self):
        old_table = self.table
        self.table = [None for i in range(0, self.capacity * 2)]
        self.capacity = self.capacity * 2
        self.size = 0
        for element in old_table:
            if element != None:
                ptr = element
                while ptr != None:
                    self.set(ptr.key, ptr.val)
                    ptr = ptr.next

