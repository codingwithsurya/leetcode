class SparseVector:
    def __init__(self, nums: List[int]):
        # index -> non zero elements 
        self.non_zero_elements = {}
        for i,elem in enumerate(nums):
            if elem != 0:
                self.non_zero_elements[i] = elem

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0 
        for index, elem in self.non_zero_elements.items():
            if index in vec.non_zero_elements:
                res += elem * vec.non_zero_elements[index]
        return res
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)