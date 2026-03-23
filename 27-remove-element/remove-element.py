class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer = len(nums) - 1
        
        while pointer >= 0:
            if nums[pointer] == val:
                nums[pointer], nums[-1] = nums[-1], nums[pointer]
                del nums[-1]
            pointer -= 1
        
        return len(nums)
        

        