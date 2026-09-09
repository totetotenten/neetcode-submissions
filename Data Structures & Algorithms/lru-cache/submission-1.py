class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = {}
        self.d[-1] = [None, -1, -1]

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        self.update(key, None)
        return self.d[key][0]
        

    def put(self, key: int, value: int) -> None:
        self.update(key, value)

        if len(self.d) > self.cap + 1:
            old = self.d[-1][2]
            old_2 = self.d[old][2]
            self.d[-1][2] = old_2
            self.d[old_2][1] = -1
            del self.d[old]
            
    
    def update(self, key: int, value):
        if key in self.d:
            prev_value, prev, next = self.d[key]
            self.d[prev][2] = next
            self.d[next][1] = prev
        if value is None:
            value = prev_value
        new = self.d[-1][1]
        self.d[new][2] = key
        self.d[key] = [value, new, -1]
        self.d[-1][1] = key

        
        
