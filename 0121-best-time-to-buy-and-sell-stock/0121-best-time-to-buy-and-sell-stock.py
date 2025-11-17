class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Take the first price as min_price
        min_price = prices[0]
        # Take the max profit as 0
        max_profit = 0
        # Iterate over the prices array
        for price in prices:
            # Determine what will be my profit if i sell the item today
            profit = price - min_price
            # Maximize the profit based on my current profit
            max_profit = max(max_profit, profit)
            # Take the currenet price as min if it is less than the min_price
            min_price = min(min_price, price)
        # Return the max_profit
        return max_profit
        