class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        pointer = 0
        
        while pointer < len(flowerbed):
            if flowerbed[pointer] == 0:
                left_empty = (pointer == 0 or flowerbed[pointer - 1] == 0)
                right_empty = (pointer == len(flowerbed) - 1 or flowerbed[pointer + 1] == 0)
                
                if left_empty and right_empty:
                    pointer += 2
                    n -= 1
                else:
                    pointer += 1
            else:
                pointer += 1
        
        return n <= 0

        
        