class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_step = 0

        # [3,2,1,0,4]
        #  0,1,2,3,4
        # [3,3,3,3,8]

        for i in range(n):
            if max_step < i:
                return False

            max_step = max(max_step, nums[i] + i)

            if max_step >= n - 1:
                return True
        
        return False


