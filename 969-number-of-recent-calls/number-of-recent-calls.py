class RecentCounter:

    def __init__(self):
        self.queue = deque()

        

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < (t - 3000):
            self.queue.popleft()
        
        return len(self.queue)


'''

[642, 1849, 4921

'''
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)