#Question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        cp = prices[0]
        for x in range(1,len(prices)):
            if prices[x] - cp > p:
                p = prices[x]-cp
            elif prices[x] < cp:
                cp = prices[x]
        return p