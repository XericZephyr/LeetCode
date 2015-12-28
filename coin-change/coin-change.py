

#
#   This is a joke
#

class SolutionJoke(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if coins:
            coins.sort()
        if 0 == len(coins):
            return -1
        elif 1 == len(coins):
            if amount % coins[0] != 0:
                return -1
            else:
                return amount/coins[0]
        else:
            c = coins[-1]
            m = amount
            for i in range(amount/c+1):
                l = self.coinChange(coins[:-1], amount-c*i)
                if l == -1:
                    continue
                cc = i + l
                if cc < m:
                    m = cc
            return m


class Solution(object):
    def coinChange(self, coins, amount):
        INT_MAX = 0xFFFFFFFF
        if not coins:
            return -1
        if amount == 0:
            return 0
        coins.sort()
        k, N = len(coins), amount
        n_list = [INT_MAX] * max(amount, coins[-1])
        for c in coins:
            n_list[c-1] = 1
        for i in range(coins[0]-1, N):
            for c in coins:
                if i+c < N:
                    n_list[i+c] = min(n_list[i+c], n_list[i]+1)
        return n_list[amount-1] if n_list[amount-1] < INT_MAX else -1


if __name__ == '__main__':
    print Solution().coinChange([1,2,5], 11)
    print Solution().coinChange([2], 3)
    print Solution().coinChange([2], 1)
    print Solution().coinChange([470,35,120,81,121], 9825)
    print Solution().coinChange([1], 0)