

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x ^ y, nums)

if __name__ == '__main__':

    print Solution().singleNumber([1, 1, 2, 2, 5])
    print Solution().singleNumber([1, 1, 2, 2, 7, 8, 5, 7, 5])