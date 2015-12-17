

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bit_count = [0] * 32

        def count_bit(num, bit_count):
            for i in range(32):
                bit_count[i] += (num & 1)
                num >>= 1

        for num in nums:
            count_bit(num, bit_count)

        # recover
        ret = 0
        for i in reversed(range(1, 32)):
            ret |= (1 if bit_count[i] % 3 else 0)
            ret <<= 1
        ret |= (1 if bit_count[0] % 3 else 0)
        if ret & 0x80000000:
            ret = -(~ret & 0x7FFFFFFF) - 1
        return ret

if __name__ == '__main__':
    print Solution().singleNumber([1,1,1,2,2,2,3])
    print Solution().singleNumber([-1,-1,-1,-2,-2,-2,-3])