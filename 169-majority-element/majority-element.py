class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        tempt = None
        cnt = 0

        for num in nums:
            if cnt == 0:
                tempt = num
            
            cnt += 1 if num == tempt else -1
        

        return tempt
        