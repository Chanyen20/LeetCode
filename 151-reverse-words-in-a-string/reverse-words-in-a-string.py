class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = list(s.split())

        return ' '.join(word_list[::-1])


        