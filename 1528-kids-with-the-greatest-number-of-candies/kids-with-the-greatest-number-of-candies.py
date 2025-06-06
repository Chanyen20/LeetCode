class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies) 
        res = []

        for i in range(len(candies)):
            if candies[i] + extraCandies < max_candies:
                res.append(False)
            else:
                res.append(True)

        return res