class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        count = 1
        
        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                count += 1
            else:
                chars[left] = chars[i - 1]
                left += 1
                if count > 1:
                    for digit in str(count):
                        chars[left] = digit
                        left += 1
                count = 1
        
        # 收尾處理最後一組字元
        chars[left] = chars[-1]
        left += 1
        if count > 1:
            for digit in str(count):
                chars[left] = digit
                left += 1
        
        chars[left:] = []
        return len(chars)