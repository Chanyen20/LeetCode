class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)

        for i in range(len(candies)):
            extra_candies = candies[i] + extraCandies
            if extra_candies >= max_candies:
                candies[i] = True
            else:
                candies[i] = False
        
        return candies
        