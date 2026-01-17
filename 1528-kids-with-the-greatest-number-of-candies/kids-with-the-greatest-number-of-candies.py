class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest_num_candies = max(candies)
        res = []

        for kid_candies in candies:
            if kid_candies + extraCandies >= greatest_num_candies:
                res.append(True)
            else:
                res.append(False)
        
        return res


        