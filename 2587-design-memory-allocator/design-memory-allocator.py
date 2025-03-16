class Allocator:

    def __init__(self, n: int):
        self.message = [0] * n

        

    def allocate(self, size: int, mID: int) -> int:
        consecutive_free = 0

        for i in range(len(self.message)):
            if self.message[i] == 0:
                consecutive_free += 1
                if consecutive_free == size:
                    start_idx = i - size + 1
                    for j in range(start_idx, i + 1):
                        self.message[j] = mID
                    return start_idx 
            else:
                consecutive_free = 0
        
        return -1 
    
    def freeMemory(self, mID: int) -> int:
        freed = 0
        for i in range(len(self.message)):
            if self.message[i] == mID:
                self.message[i] = 0
                freed += 1
        return freed
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)