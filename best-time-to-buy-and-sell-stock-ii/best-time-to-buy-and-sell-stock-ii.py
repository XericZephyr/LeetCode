
#
#   O(N) AC, 52 ms
#

class SolutionAC(object):
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


#
#   State Machine (AC, 56ms)
#

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        hold = -prices[0]
        rest = 0
        for i in range(1, len(prices)):
            hold, rest = max(hold, rest - prices[i]), max(rest, hold+prices[i])
        return rest


if __name__ == '__main__':
    print Solution().maxProfit([1,2,3,2,3,4,1])
    print Solution().maxProfit([12,3,2,15,24,54,3])