class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_container = 0

        while left < right:
            curr_height = min(height[left], height[right])
            curr_width = right - left

            max_container = max(max_container, curr_height * curr_width)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_container

