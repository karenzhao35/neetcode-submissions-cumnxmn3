class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_index, min_index, maxSoFar = 0, 0, 0
        for index, price in enumerate(prices):
            if price < prices[min_index]: min_index, max_index = index, index
            elif price > prices[max_index]: max_index, maxSoFar = index, max(maxSoFar, prices[index] - prices[min_index])
        return maxSoFar