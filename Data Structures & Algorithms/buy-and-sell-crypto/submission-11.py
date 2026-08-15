class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuy = prices[0]

        for item in prices:
            minBuy = min(minBuy, item)
            maxProfit = max(maxProfit, item-minBuy)

        return maxProfit