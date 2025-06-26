class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0 
        res = 0

        for i in range(len(gain)):

            res = max (res, curr + gain[i]) 
            curr += gain[i]

        return res

        