class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o','u', 'A', 'E', 'I', 'O','U']
        s_list = list(s)
        left_pointer, right_pointer = 0, len(s) - 1


        while left_pointer < right_pointer:
            if s_list[left_pointer] not in vowels:
                left_pointer += 1
            if s_list[right_pointer] not in vowels:
                right_pointer -= 1
            if s_list[left_pointer] in vowels and s_list[right_pointer] in vowels:
                s_list[left_pointer], s_list[right_pointer] = s_list[right_pointer], s_list[left_pointer]
                left_pointer += 1
                right_pointer -= 1
        return ''.join(s_list)
            


