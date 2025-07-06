class Solution:
    def frequencySort(self, s: str) -> str:
        charToFreq = Counter(s)
        res = "" 
        for char, freq in sorted(charToFreq.items(), key=lambda x: x[1], reverse=True):
            res += char * freq
        return res
