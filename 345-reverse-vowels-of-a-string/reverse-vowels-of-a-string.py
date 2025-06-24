class Solution:
    def reverseVowels(self, s: str) -> str:
        res = list(s)
        left, right = 0, len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        while left < right:
            if res[left] in vowels:
                if res[right] in vowels:
                    res[left], res[right] = res[right], res[left]
                    left += 1
                    right -= 1
                
                else: 
                    right -= 1

            else:
                if res[right] in vowels:
                    left += 1
                
                else: 
                    left += 1
                    right -= 1
        
        return ''.join(res)
            
        