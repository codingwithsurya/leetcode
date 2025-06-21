class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write_idx = 0
        for read_idx in range(1, len(nums)):
            # whenever we see a new num 
            if nums[write_idx] != nums[read_idx]:
                write_idx += 1
                nums[write_idx] = nums[read_idx]
        return write_idx + 1