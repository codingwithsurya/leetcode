class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diff_to_index = {0:-1} # mapping the diff at index i -> index i
        diff = 0
        res = 0 

        for i in range(len(nums)):
            if nums[i] == 0:
                diff -= 1
            else:
                diff += 1
            
            # if we have seen this diff before 
            # update max length as 
            # (current_index - corresponding diff index)
            if diff in diff_to_index:
                res = max(res, i - diff_to_index[diff])
            else:
                diff_to_index[diff] = i
            
        return res
            