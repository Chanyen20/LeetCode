class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
    

        return self.dealBackspace(s) == self.dealBackspace(t)
    
    def dealBackspace(self, string): 
        res_list = []
        
        for char in string: 
            if char != '#':
                res_list.append(char)
            else:
                if res_list:
                    res_list.pop()
        return res_list