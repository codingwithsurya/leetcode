class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for s in strs[1:]:
            while s[:len(prefix)] != prefix:
                prefix = prefix[:len(prefix) - 1]
        
        return prefix

            
        