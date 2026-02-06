class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = dict() #{value: index}
        n = len(nums)

        for i in range(n):
            if nums[i] in seen:
                index = seen[nums[i]]
                if abs(index - i) <= k:
                    return True   
            seen[nums[i]] = i
        
        return False


        