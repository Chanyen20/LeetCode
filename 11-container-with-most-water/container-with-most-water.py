class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        left, right = 0, len(height) - 1

        while left < right:
            width = right - left
            maxWater = max(maxWater, min(height[left], height[right]) * width)
            
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        
        return maxWater