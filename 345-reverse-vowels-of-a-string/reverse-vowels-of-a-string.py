class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        seen_stack = []
        res = []

        for char in s:
            if char in vowels:
                seen_stack.append(char)
        
        for char in s:
            if char in vowels:
                replace = seen_stack.pop()
                res.append(replace)
            else:
                res.append(char)
    
        return ''.join(res)

        
