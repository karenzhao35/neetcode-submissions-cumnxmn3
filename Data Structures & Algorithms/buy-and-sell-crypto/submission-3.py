class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_index = 0
        min_index = 0
        maxSoFar = 0 
        for index, price in enumerate(prices):
            if price < prices[min_index]:
                min_index = index
                max_index = index
            elif price > prices[max_index]: 
                max_index = index
                new_profit = prices[max_index] - prices[min_index]
                maxSoFar = new_profit if new_profit > maxSoFar else maxSoFar
            print(f"min{min_index} max{max_index} maxSoFar {maxSoFar}")
        return maxSoFar
