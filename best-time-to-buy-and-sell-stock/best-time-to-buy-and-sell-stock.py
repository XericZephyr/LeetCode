

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sum, max = 0, 0
        for i in range(len(prices)-1):
            sum += prices[i+1] - prices[i]
            sum = sum if sum > 0 else 0
            max = max if max > sum else sum
        return max


if __name__ == '__main__':
    print Solution().maxProfit([1,2,3,4,5])
    print Solution().maxProfit([1,2,3,4,5])
    print Solution().maxProfit([])
    print Solution().maxProfit([2,1])
    print Solution().maxProfit([2,1, 4])