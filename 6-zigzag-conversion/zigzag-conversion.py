class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
            
        word_row = [""] * numRows

        pointer = 0
        forward = True
        for i in range(len(s)):
            word_row[pointer] += s[i]

            if forward:
                pointer += 1
                if pointer == numRows - 1:
                    forward = False
            else:
                pointer -= 1
                if pointer == 0:
                    forward = True
        return ''.join(word_row)