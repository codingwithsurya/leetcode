class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_count = Counter() # char -> freq 

        l = 0
        longest = 0 
        for r in range(len(s)):
            window_count[s[r]] += 1
            max_freq = max(window_count.values()) 
            window_length = (r - l) + 1

            replacements_needed = window_length - max_freq 
            if replacements_needed > k:
                window_count[s[l]] -= 1
                l += 1
            longest = max(longest, (r-l) + 1)
        return longest 

        