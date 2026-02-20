class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        least_len = min(len(word1), len(word2))

        for i in range(least_len):
            res += word1[i]
            res += word2[i]
        
        if least_len < len(word1):
            res += word1[least_len:]
        else:
            res += word2[least_len:]
        
        return res
        