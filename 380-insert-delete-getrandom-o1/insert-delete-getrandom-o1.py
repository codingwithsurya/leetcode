class RandomizedSet:

    def __init__(self):
        self.values = []
        self.store = {} # value -> indices 

    def insert(self, val: int) -> bool:
        if val in self.store:
            return False
        
        self.values.append(val)
        self.store[val] = len(self.values) - 1
        return True 

    def remove(self, val: int) -> bool:
        if val not in self.store:
            return False 
        
        idx_to_remove = self.store[val]
        last_idx = len(self.values) - 1
        last_val = self.values[last_idx]
        self.values[last_idx], self.values[idx_to_remove] = self.values[idx_to_remove], self.values[last_idx]

        self.store[last_val] = idx_to_remove

        self.values.pop()
        del self.store[val]

        return True
        

    def getRandom(self) -> int:
        return random.choice(self.values)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()