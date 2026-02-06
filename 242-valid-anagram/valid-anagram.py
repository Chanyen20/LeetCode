class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if the length is not the same, means they were not anagram
        if len(s) != len(t):
            return False
        
        seen_s = dict()
        seen_t = dict()

        for s_char, t_char in zip(s, t):
            if s_char not in seen_s:
                seen_s[s_char] = 0
            
            if t_char not in seen_t:
                seen_t[t_char] = 0
            
            seen_s[s_char] += 1
            seen_t[t_char] += 1
        
        return seen_s == seen_t

        