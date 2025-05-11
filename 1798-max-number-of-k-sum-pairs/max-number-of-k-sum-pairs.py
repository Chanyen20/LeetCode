class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        if nums is None:
            return 0

        nums.sort()    
        # ord_nums = sorted(nums)
        res = 0
        left_pointer, right_pointer = 0, len(nums) - 1

        while left_pointer < right_pointer:
            cal_num = nums[left_pointer] + nums[right_pointer]
            if cal_num == k:
                res += 1
                left_pointer += 1
                right_pointer -= 1
            elif cal_num < k:
                left_pointer += 1
            else:
                right_pointer -= 1

        return res
