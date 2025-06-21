class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_sum = defaultdict(int) # sum -> count 
        prefix_sum[0] = 1
        running_sum = 0

        for num in nums:
            running_sum += num
            if running_sum - k in prefix_sum:
                res += prefix_sum[running_sum - k]
            prefix_sum[running_sum] = prefix_sum.get(running_sum, 0) + 1
        return res