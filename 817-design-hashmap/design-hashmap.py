class MyHashMap:

    def __init__(self):
        self.capacity = 100
        self.buckets = [[] for _ in range(self.capacity)]

    def __hash(self, key):
        return key % self.capacity

    def put(self, key: int, value: int) -> None:
        bucket_index = self.__hash(key)
        bucket = self.buckets[bucket_index]
        for i, (k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return 
        bucket.append((key, value))
        
    def get(self, key: int) -> int:
        bucket_index = self.__hash(key)
        bucket = self.buckets[bucket_index]

        for k,v in bucket:
            if k == key:
                return v 
        return -1 

    def remove(self, key: int) -> None:
        bucket_index = self.__hash(key)
        bucket = self.buckets[bucket_index]
        for i, (k,v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return 
            
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)