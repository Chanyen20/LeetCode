class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left_pointer = 0

        for num in nums:
            if num != 0:
                nums[left_pointer] = num
                left_pointer += 1
        
        for i in range(left_pointer, len(nums)):
            nums[i] = 0

        # time complexity: O(n) -> Only walked through the list once
        # space complexity: O(1) -> No extra list is used
        