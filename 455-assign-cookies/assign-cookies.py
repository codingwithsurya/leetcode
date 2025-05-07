class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i,j = 0,0
        content = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                content += 1
                i += 1
                j += 1
            else:
                j += 1
        
        return content

        '''
        7.8.9,10

        5.6.7.8
        '''
        