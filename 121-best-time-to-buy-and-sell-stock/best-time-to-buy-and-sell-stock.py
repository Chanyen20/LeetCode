class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        res = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                res = max(res, price - min_price)
        
        return res
        