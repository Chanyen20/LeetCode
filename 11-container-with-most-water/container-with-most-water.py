class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1
        
        while left < right:
            avaliable_height = min(height[left], height[right])
            max_area = max(max_area, avaliable_height * (right - left))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area