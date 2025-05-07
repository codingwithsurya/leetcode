class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        write, count = 1, 1
        for i in range(1, len(nums)):
            # found a dup
            if nums[i] == nums[i - 1]:
                count +=1 
            else:
                count = 1
            
            if count <= 2:
                nums[write] = nums[i]
                write += 1
        return write
