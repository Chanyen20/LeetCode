class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                first = num  # 更新最小值
            elif num <= second:
                second = num  # 找到比 first 大的第二小值
            else:
                # 找到比 second 還大的數，即存在 triplet
                return True

        return False



        