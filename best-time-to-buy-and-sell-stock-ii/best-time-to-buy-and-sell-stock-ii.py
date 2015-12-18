

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i in range(len(prices)-1):
            dif = prices[i+1] - prices[i]
            max_profit += dif if dif > 0 else 0
        return max_profit