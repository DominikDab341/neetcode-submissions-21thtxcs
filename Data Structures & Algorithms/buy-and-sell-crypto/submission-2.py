class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 0
        max_profit = 0
        for i in range(len(prices)):
            if prices[i]<prices[j]:
                j = i
            profit =  prices[i] - prices[j]
            if profit > max_profit:
                max_profit = profit

        return max_profit
            