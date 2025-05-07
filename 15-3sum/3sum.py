class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        num_set = set() 
        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1

            while start < end:
                cur_sum = nums[i] + nums[start] + nums[end]
                if cur_sum == 0:

                    num_set.add((nums[i], nums[start], nums[end]))
                    start += 1
                    end -= 1
                elif cur_sum < 0:
                    start += 1
                elif cur_sum > 0:
                    end -= 1
        return list(num_set)