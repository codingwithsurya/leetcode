class Solution:
    def maxProduct(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        max_1, max_2 = 0,0
        for d in digits:
            if d > max_1:
                max_2 = max_1
                max_1 = d
            elif int(d) > max_2:
                max_2 = d 
        return max_1 * max_2
        
        