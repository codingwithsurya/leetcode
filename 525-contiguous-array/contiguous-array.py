class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diff_to_index = {0: -1}
        diff = 0
        res = 0
        for i, n in enumerate(nums):
            if n == 0:
                diff -= 1
            else:
                diff += 1
            
            if diff in diff_to_index:
                res = max(res, i - diff_to_index[diff])
            else:
                diff_to_index[diff] = i
        return res
        