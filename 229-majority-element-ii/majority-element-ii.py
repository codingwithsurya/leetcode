class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numToCount = defaultdict(int)
        n = len(nums)
        res = []

        for num in nums:
            numToCount[num] += 1

        for num, count in numToCount.items():
            if count > n // 3:
                res.append(num)
        
        return res 
        