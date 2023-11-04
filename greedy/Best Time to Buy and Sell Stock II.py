from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        slow = 0
        fast = 1
        # base case
        if not prices:
            return res
        # general case
        while fast < len(prices):
            # check if condition holds
            if prices[fast] - prices[slow] > 0:
                res += prices[fast] - prices[slow]
            # now adjust the pointers
            slow += 1
            fast += 1
        return res
