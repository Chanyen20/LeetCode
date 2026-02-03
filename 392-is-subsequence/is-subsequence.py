class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        s_pointer = 0

        for t_char in t:
            if s[s_pointer] == t_char:
                s_pointer += 1
            
            if s_pointer == len(s):
                return True
        
        return False


        