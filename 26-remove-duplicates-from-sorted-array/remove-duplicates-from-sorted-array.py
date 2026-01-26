class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        pointer = 0
        prev_val = None
    
        for i in range(len(nums)):
            if prev_val is None:
                prev_val = nums[i]
                continue
            
            if nums[i] != prev_val:
                prev_val = nums[i]
                nums[pointer + 1] = nums[i]
                pointer += 1
                
        return pointer + 1




        