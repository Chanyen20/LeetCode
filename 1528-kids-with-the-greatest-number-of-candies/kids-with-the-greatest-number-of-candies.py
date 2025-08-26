class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # find the max candies in all kids they have
        max_candy = 0
        for i in range(len(candies)):
            max_candy = max(max_candy, candies[i])
        
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candy:
                candies[i] = True
            else:
                candies[i] = False
        return candies