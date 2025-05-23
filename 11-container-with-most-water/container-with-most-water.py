class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxContainer = 0
        left, right = 0, len(height) - 1

        while left < right:
            currnet_height = min(height[left], height[right])
            maxContainer = max(maxContainer, (right - left) * currnet_height)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxContainer
        