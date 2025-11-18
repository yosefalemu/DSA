class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        max_profit = 0
        for price in prices:
            profit = price - buy_price
            buy_price = min(buy_price, price)
            max_profit = max(max_profit, profit)
        return max_profit