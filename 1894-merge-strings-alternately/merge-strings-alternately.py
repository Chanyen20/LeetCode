class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        length = max(len(word1), len(word2))

        for i in range(length):
            if i < len(word1):
                res = res + word1[i]
            
            if i < len(word2):
                res = res + word2[i]
        return res

# time complexity: O(n) n <= max(len(word1), len(word2))
# space complexity : O(n) n <= len(word1)+ len(word2))
            
        