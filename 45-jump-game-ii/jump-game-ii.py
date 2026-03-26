class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
            
        jump = 0
        current_end = 0
        farest_jump = 0

        for i, num in enumerate(nums):
            farest_jump = max(farest_jump, i + num)

            if i == current_end:
                jump += 1
                current_end = farest_jump

                if current_end >= len(nums) - 1:
                    break
        
        return jump
        