class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]
        profit = 0
        for currPrice in prices:
            profit = max(profit, currPrice - buyPrice)
            buyPrice = min(buyPrice, currPrice)
        return profit

            
