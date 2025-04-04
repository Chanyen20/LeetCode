class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        number_of_zero = nums.count(0)

        # only retain none zero
        nums[:] = [num for num in nums if num != 0]

        nums.extend([0] * number_of_zero)
        