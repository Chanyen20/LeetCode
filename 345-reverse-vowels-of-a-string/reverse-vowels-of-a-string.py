class Solution:
    def reverseVowels(self, s: str) -> str:
        # vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        # 用 set("aeiouAEIOU") 替代列表能讓時間複雜度從O(n)降到O(1)
        vowels = set("aeiouAEIOU")
        lst = list(s)

        left, right = 0, len(s) - 1

        while left < right:
            if lst[left] not in vowels:
                left += 1
            elif lst[right] not in vowels:
                right -= 1
            else:
                # both are vowels → swap and move inward
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1

        return "".join(lst)