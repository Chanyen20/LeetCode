class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_length = len(needle)
        haystack_length = len(haystack)

        if haystack_length < needle_length:
            return -1

        for i in range(0, haystack_length - needle_length + 1):
            if haystack[i: i + needle_length] == needle:
                return i
        
        return -1

        