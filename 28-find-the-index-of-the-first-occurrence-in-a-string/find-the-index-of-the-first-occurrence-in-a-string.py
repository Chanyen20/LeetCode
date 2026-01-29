class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_size = len(needle)

        for i in range(len(haystack) - needle_size + 1):
            if haystack[i] == needle[0]:
                if haystack[i : i + needle_size] == needle:
                    return i
                else:
                    continue
        
        return -1
        