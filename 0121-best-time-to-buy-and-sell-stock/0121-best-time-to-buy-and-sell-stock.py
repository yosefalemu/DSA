class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_buy = float('inf')
        profit = 0
        for price in prices:
            if price < current_buy:
                current_buy = price
            profit = max(profit,price - current_buy)
        return profit