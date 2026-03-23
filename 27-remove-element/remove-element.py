class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer = len(nums) - 1
        
        while pointer >= 0:
            if nums[pointer] == val:
                del nums[pointer]
            pointer -= 1
        
        return len(nums)
        

        