class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = Counter(nums)

        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in num_to_freq.items():
            bucket[freq].append(num)
        
        num_set = set()
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                num_set.add(num)
            
            if len(num_set) == k:
                return list(num_set)
        return list(num_set)


        