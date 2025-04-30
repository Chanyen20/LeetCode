class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_not_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_not_zero], nums[i] = nums[i], nums[last_not_zero]
                last_not_zero += 1