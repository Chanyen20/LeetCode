class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxValue = sum(nums[:k])
        recentWindows = maxValue
        left = 0 

        for right in range(k, len(nums)):
            recentWindows = recentWindows - nums[left] + nums[right]
            maxValue = max(maxValue, recentWindows) 
            left += 1
        return maxValue / k