class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum_arr = []
        num_sum = 0
        for n in nums:
            num_sum += n
            self.prefix_sum_arr.append(num_sum)
        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sum_arr[right]
        return self.prefix_sum_arr[right] - self.prefix_sum_arr[left - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)