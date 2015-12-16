

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 1, len(nums)
        while low < high:
            mid = (low + high) / 2
            c = reduce(lambda x, y: x+1, (n for n in nums if n <= mid), 0)
            if c > mid:
                high = mid
            else:
                low = mid + 1
        return low

if __name__ == '__main__':
    print Solution().findDuplicate([1,2,3,4,4,6,7])
    print Solution().findDuplicate([1,2,3,4,5,5,5,5,6])
    print Solution().findDuplicate([1,1])