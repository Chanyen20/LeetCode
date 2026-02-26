class Solution:
    def isValid(self, s: str) -> bool:
        valid_mapping = {
            ")": "(", 
            "]": "[", 
            "}": "{"
        }
        stack = []

        for char in s:
            if char not in valid_mapping:
                stack.append(char)
            else:
                if not stack or valid_mapping[char] != stack.pop():
                    return False

        
        return not stack

        