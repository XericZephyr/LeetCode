
from utils import BinaryIndexedTree

class NumArray(object):

    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self._tree = [0] * (1+len(nums))
        for i in range(1, 1+len(nums)):
            self._add_value(i, nums[i - 1])

    def _get_sum(self, idx):
        s = 0
        while idx > 0:
            s += self._tree[idx]
            idx -= (idx & -idx)
        return s

    def _get_value(self, idx):
        return self._get_sum(idx) - self._get_sum(idx - 1)

    def _add_value(self, idx, add_val):
        while idx < len(self._tree):
            self._tree[idx] += add_val
            idx += (idx & -idx)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self._add_value(i + 1, val - self._get_value(i + 1))

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._get_sum(j+1) - self._get_sum(i)


if __name__ == '__main__':
    # nums = [1,3,5]
    # tree = BinaryIndexedTree(nums)
    # for i in range(len(nums)):
    #     print tree[i]
    # print tree[:]
    # print tree[0:2]
    # print tree[1:2]
    # tree[1] = 2
    # for i in range(len(nums)):
    #     print tree[i]
    # print tree[:]

    numArray = NumArray([1,3,5])
    print numArray.sumRange(0, 2)
    print numArray.sumRange(2, 2)
    numArray.update(1, 2)
    print numArray.sumRange(0, 2)