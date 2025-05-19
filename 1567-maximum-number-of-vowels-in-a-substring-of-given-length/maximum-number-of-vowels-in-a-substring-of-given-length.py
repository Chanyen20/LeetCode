class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a','e','i','o','u'] 
        maxNumVowel = 0

        currentNum = sum(1 for ch in s[:k] if ch in vowels)
        maxNumVowel = currentNum

        for right in range(k, len(s)):
            if s[right] in vowels:
                currentNum += 1
            if s[right - k] in vowels:
                currentNum -= 1

            maxNumVowel = max(maxNumVowel, currentNum)

        return maxNumVowel
        
        