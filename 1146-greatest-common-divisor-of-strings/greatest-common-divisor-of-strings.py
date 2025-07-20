# import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        shortest_len = math.gcd(len(str1), len(str2))

        if str1[:shortest_len] == str2[:shortest_len] and str1 + str2 == str2 + str1:
            return str1[:shortest_len]
        else:
            return ""

# time: O(n)
# space: O(1)
        