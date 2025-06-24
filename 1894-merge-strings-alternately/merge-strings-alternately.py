# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         res = ''
#         for i in range(max(len(word1), len(word2))):
#             if i < len(word1):
#                 res = res + word1[i]
#             if i < len(word2):
#                 res = res + word2[i]

#         return res

# time complexity:  0 < O(n) n < len(word1), len(word2))
# space complexity: 0 < O(n) n < len(word1), len(word2))

# Python 中字串是 immutable 的，每次用 res + ... 其實都會產生新字串。如果你要處理很長的字串，建議這樣寫
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                res.append(word1[i])
            if i < len(word2):
                res.append(word2[i])
        return ''.join(res)


