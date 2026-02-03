class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums) - 1
        res = set()

        for i in range(len(nums)):
            left = i + 1
            right = n
            target = nums[i] * -1

            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    pair = (nums[i], nums[left], nums[right])
                    res.add(pair)
                    left += 1
                    right -= 1

        
        return [list(t) for t in res]


        