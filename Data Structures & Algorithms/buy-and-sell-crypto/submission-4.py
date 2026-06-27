class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minL = prices[0]
        profit = 0

        for i in range (1, len(prices)):
            # i is the selling day, we can't sell before we buy hence we start a 1
            profit = max(profit, prices[i] - minL)
            minL = min(minL, prices[i])

        return profit