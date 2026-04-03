class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        res = [[] for _ in range(numRows)]

        pointer_row = 0
        forward = True

        for char in s:
            res[pointer_row].append(char)

            if forward:
                if pointer_row + 1 == numRows:
                    forward = False
                    pointer_row -= 1
                else:
                    pointer_row += 1
            else:
                if pointer_row - 1 == -1:
                    forward = True
                    pointer_row += 1
                else:
                    pointer_row -= 1
        
        for i in range(len(res)):
            res[i] = ''.join(res[i])
        
        return ''.join(res)
            
            



        