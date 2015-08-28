__author__ = 'clp'


class Solution(object):

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(32):
            if n <= 0:
                break
            res += n % 2
            n /= 2
        return res

if __name__ == "__main__":
    print Solution().hammingWeight(11)
    print Solution().hammingWeight(760)
    print Solution().hammingWeight(0)
    print Solution().hammingWeight(-1)