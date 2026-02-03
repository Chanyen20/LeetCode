class Solution:
    def isPalindrome(self, s: str) -> bool:
        letter_list = []

        for char in s:
            if char.isalnum():

                letter_list.append(char.lower())
        
        return letter_list == letter_list[::-1]
        