from typing import List 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimumSoFar = prices[0]
        maxProfit = 0

        for price in prices[1:]:
            profit = price - minimumSoFar
            if profit > maxProfit:
                maxProfit = profit
            if price < minimumSoFar:
                minimumSoFar = price

        return maxProfit

                