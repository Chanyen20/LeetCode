class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # # edge case
        # if s == "":
        #     return True
        # if s or t is None:
        #     return False
        if not s:
            return True
        if len(s) > len(t):
            return False

        left_point = 0 

        for right_pointer in range(len(t)):
            if s[left_point] == t[right_pointer]:
                left_point += 1
            if left_point == len(s):
                return True

        return False
        
        