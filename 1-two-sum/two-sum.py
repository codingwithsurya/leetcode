class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_to_index:
                return [i, num_to_index.get(complement)]
            
            num_to_index[nums[i]] = i 
        return nums
        