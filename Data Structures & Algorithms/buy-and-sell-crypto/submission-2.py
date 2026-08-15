class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]

        n = len(prices)

        for p in range(n-1):
            maxProfit = max(maxProfit, prices[p+1] - minPrice)
            minPrice = min(minPrice, prices[p+1])
        
        return maxProfit

            