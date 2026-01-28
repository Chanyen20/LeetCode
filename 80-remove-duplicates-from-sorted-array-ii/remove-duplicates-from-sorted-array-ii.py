class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicate_cnt = 1
        curr_pointer = 0   # slow pointer

        for i in range(1, len(nums)):
            if nums[i] == nums[curr_pointer] and duplicate_cnt == 2:
                continue

            if nums[i] == nums[curr_pointer] and duplicate_cnt < 2:
                duplicate_cnt += 1
                nums[curr_pointer + 1] = nums[i]
                curr_pointer += 1
            else:
                nums[curr_pointer + 1] = nums[i]
                curr_pointer += 1
                duplicate_cnt = 1
        
        return curr_pointer + 1



