class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf') # 1
        max_profit = 0 # 5

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit

# time complexity: O(n)
# space complexity: O(1)

# [7,1,5,3,6,4]
#            |
        