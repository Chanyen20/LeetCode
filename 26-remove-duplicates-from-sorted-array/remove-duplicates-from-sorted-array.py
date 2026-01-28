class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 0
    
        for i in range(1, len(nums)):
            if nums[pointer] != nums[i]:
                nums[pointer + 1] = nums[i]
                pointer += 1
        
        return pointer + 1
