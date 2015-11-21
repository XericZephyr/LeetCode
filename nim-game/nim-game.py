

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return bool(n % 4)


if __name__ == '__main__':
    print Solution().canWinNim(10)
    print Solution().canWinNim(12)
    print Solution().canWinNim(4)
    print Solution().canWinNim(8)
    print Solution().canWinNim(9)