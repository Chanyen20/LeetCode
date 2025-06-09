class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        pointer = 0
        while pointer < len(flowerbed):
            if flowerbed[pointer] == 0:
                empty_left = (pointer == 0) or (flowerbed[pointer - 1] == 0)
                empty_right = (pointer == len(flowerbed) - 1) or (flowerbed[pointer + 1] == 0)
                if empty_left and empty_right:
                    flowerbed[pointer] = 1
                    n -= 1
                    pointer += 2  # 跳過下一格，不能連種
                    continue
            pointer += 1
        return n <= 0
        