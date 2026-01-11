class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        result = []

        answer0 = []
        answer1 = []

        for num in nums1_set:
            if num not in nums2_set:
                answer0.append(num)

        for num in nums2_set:
            if num not in nums1_set:
                answer1.append(num)
        
        result.append(answer0)
        result.append(answer1)

        return result
        




        