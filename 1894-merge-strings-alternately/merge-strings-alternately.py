class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for i in range (0, 2 * max(len(word1), len(word2))): 
            if (i % 2) == 0:
                if i // 2 < len(word1):
                    res += word1[i // 2]
            else:
                if i // 2 < len(word2):
                    res += word2[i // 2]
        return res
