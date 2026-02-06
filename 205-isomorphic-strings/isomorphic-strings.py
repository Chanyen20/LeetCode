class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        switch_to_t = dict()
        switch_to_s = dict()

        if len(s) != len(t):
            return False
        
        for s_char, t_char in zip(s, t):
            if s_char in switch_to_t and switch_to_t[s_char] != t_char:
                return False
            
            if t_char in switch_to_s and switch_to_s[t_char] != s_char:
                return False

            switch_to_t[s_char] = t_char
            switch_to_s[t_char] = s_char
            
        return True

        

