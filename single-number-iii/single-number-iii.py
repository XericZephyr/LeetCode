

class Solution(object):
    #
    #   Referenced from https://leetcode.com/discuss/70790/easy-python-o-n-o-1-solution
    #
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        xor = reduce(lambda x, y: x ^ y, nums, 0)
        mask = 1
        while not (xor & mask):
            mask <<= 1
        a, b = 0, 0
        for num in nums:
            if num & mask:
                a ^= num
            else:
                b ^= num
        return [a, b]

if __name__ == '__main__':
    print Solution().singleNumber([1, 2, 1, 3, 2, 5])
    print Solution().singleNumber([3, 2, 1, 3, 2, 5])