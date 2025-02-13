class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] < buyPrice:
                buyPrice = prices[i]
            elif profit < prices[i] - buyPrice:
                profit = prices[i] - buyPrice
        return profit

            
