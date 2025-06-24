from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        pointer = 0
        length = len(flowerbed)

        while pointer < length:
            if flowerbed[pointer] == 0:
                empty_left = (pointer == 0 or flowerbed[pointer - 1] == 0)
                empty_right = (pointer == length - 1 or flowerbed[pointer + 1] == 0)

                if empty_left and empty_right:
                    # flowerbed[pointer] = 1
                    n -= 1
                    if n == 0:
                        return True
                    pointer += 2
                    continue
            pointer += 1

        return n <= 0
