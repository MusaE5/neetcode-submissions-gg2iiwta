class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0

        lowest_price = prices[0]
        max_profit = 0

        for i in range (len(prices)):
            lowest_price = min(lowest_price, prices[i])
            max_profit = max(max_profit, prices[i] - lowest_price)

        return max_profit    






        