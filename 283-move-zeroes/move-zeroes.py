class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        number_of_zero = nums.count(0)
        answer_list = []

        for i in range(len(nums)):
            if nums[i] != 0:
                answer_list.append(nums[i])
            
        answer_list.extend([0] * number_of_zero)

        for i in range(len(nums)):
            nums[i] = answer_list[i]

        