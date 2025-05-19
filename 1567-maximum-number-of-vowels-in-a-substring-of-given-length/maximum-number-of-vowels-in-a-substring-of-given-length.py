class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a','e','i','o','u'] 
        maxNumVowel = 0
        left = 0

        for i in range(0, k):
            if s[i] in vowels:
                maxNumVowel += 1
        currentNum = maxNumVowel

        for right in range(k, len(s)):
            if not (s[left] in vowels) and s[right] in vowels:
                currentNum += 1
            elif s[left] in vowels and not (s[right] in vowels):
                currentNum -= 1
            
            maxNumVowel = max(maxNumVowel, currentNum)
            left += 1

        return maxNumVowel
        
        