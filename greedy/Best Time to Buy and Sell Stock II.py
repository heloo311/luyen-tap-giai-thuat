from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n= len(prices)
        have_stock = False
        current_calue = prices[0]
        maxx = current_calue
        for i in range(1,n-1):
            temp = prices[i]
            if min(temp,maxx) <


print()