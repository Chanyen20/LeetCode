class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_len = 0
        anchor = 0

        for i in range(len(nums)):

            if i > 0 and nums[i - 1] >= nums[i]:
                anchor = i
            max_len = max(max_len, i - anchor + 1)

        return max_len