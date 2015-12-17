


class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        for i in range(31):
            ret |= (n & 0b1)
            ret <<= 1
            n >>= 1
        ret |= (n & 0xb1)
        return ret

if __name__ == '__main__':
    print Solution().reverseBits(1)
    print Solution().reverseBits(0)
    print Solution().reverseBits(43261596)