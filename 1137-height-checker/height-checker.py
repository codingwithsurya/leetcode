class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        i, j = 0,0 
        count = 0 
        while i < len(expected) and j < len(heights):
            if expected[i] != heights[j]:
                count += 1
            i +=1 
            j +=1 
        return count 