class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        left = 0 
        for right in range(1,len(prices)):
            if prices[right] > prices[left]:
                ans += prices[right] - prices[left]
            left += 1
        return ans
        