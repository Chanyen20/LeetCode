class Solution:
    def maxArea(self, height: List[int]) -> int:
        water_container = 0
        left_pointer, right_pointer = 0, len(height) - 1

        while left_pointer < right_pointer:
            bottleneck_height = min(height[left_pointer], height[right_pointer])
            water_container = max(water_container, (right_pointer - left_pointer) * bottleneck_height)

            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
                
        return water_container