

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self._integral_list = [0]
        for num in nums:
            self._integral_list.append(self._integral_list[-1]+num)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._integral_list[j+1] - self._integral_list[i]

if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    numArray = NumArray(nums)
    print numArray.sumRange(0, 2)
    print numArray.sumRange(2, 5)
    print numArray.sumRange(0, 5)

