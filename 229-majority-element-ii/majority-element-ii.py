class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cutoff = len(nums) // 3

        num_to_freq = Counter(nums) 
        
        res = []
        for num, freq in num_to_freq.items():
            if freq > cutoff:
                res.append(num)
        
        return res
        