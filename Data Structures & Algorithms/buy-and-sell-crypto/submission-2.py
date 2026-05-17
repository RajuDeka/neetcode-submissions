class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        max_profit = 0

        for i in prices:
            min_p = min(min_p,i)
            profit = i - min_p
            max_profit = max(profit,max_profit)
        return max_profit