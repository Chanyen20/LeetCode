class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = 0

        for i in range(len(candies)):
            max_candy = max(max_candy, candies[i])

        for i in range(len(candies)):
            if candies[i] + extraCandies < max_candy:
                candies[i] = False
            else:
                candies[i] = True
        return candies
        
        