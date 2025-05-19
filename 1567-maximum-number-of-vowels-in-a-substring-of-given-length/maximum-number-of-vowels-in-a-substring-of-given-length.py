class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        # 1. 统计前 k 个字符的元音数
        currentNum = sum(1 for ch in s[:k] if ch in vowels)
        maxNumVowel = currentNum
        
        # 2. 滑动窗口：每次减掉左端、加上右端
        for right in range(k, len(s)):
            if s[right] in vowels:
                currentNum += 1
            if s[right - k] in vowels:
                currentNum -= 1
            
            # 更新最大值
            if currentNum > maxNumVowel:
                maxNumVowel = currentNum
        
        return maxNumVowel
