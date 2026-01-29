class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        total_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
               total_profit +=  (prices[i] - min_price)
               min_price = prices[i]
        return total_profit

        