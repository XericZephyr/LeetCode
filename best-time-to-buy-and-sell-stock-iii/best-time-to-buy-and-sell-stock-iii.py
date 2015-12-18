


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        INT_MIN = -0xFFFFFFFF
        hold_1st = INT_MIN
        rest_1st = 0
        hold_2nd = INT_MIN
        rest_2nd = 0
        for i in range(len(prices)):
            hold_1st, rest_1st, hold_2nd, rest_2nd = \
                max(-prices[i], hold_1st), \
                max(rest_1st, hold_1st+prices[i]), \
                max(hold_2nd, rest_1st-prices[i]), \
                max(rest_2nd, hold_2nd+prices[i])
        return max(rest_2nd, rest_1st)


if __name__ == '__main__':
    print Solution().maxProfit([1, 2, 3, 0, 2])
    print Solution().maxProfit([1, 2, 3, 0, 2])