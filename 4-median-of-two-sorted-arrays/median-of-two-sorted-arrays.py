class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mixList = []

        pointer1, pointer2 = 0, 0
        while pointer1 < len(nums1) and pointer2 < len(nums2):
            if nums1[pointer1] < nums2[pointer2]:
                mixList.append(nums1[pointer1])
                pointer1 += 1
            elif nums1[pointer1] > nums2[pointer2]:
                mixList.append(nums2[pointer2])
                pointer2 += 1
            else:
                mixList.append(nums1[pointer1])
                mixList.append(nums2[pointer2])
                pointer1 += 1
                pointer2 += 1
        
        mixList.extend(nums1[pointer1:])
        mixList.extend(nums2[pointer2:])

        if len(mixList) % 2 != 0:
            median = len(mixList) // 2
            return mixList[median] / 1
        else:
            median = (len(mixList) - 1) // 2
            return (mixList[median] + mixList[median + 1]) / 2

        