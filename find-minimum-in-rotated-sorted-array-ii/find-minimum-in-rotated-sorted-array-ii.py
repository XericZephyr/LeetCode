

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #
        #   What if we got [1 1 1 1 0 1 1] and [1 0 1 1 1 1 1]
        #
        left, right = 0, len(nums) - 1
        while left < right-1:
            mid = (left + right)/2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid
            else:
                right -= 1
        return min(nums[left], nums[right])

if __name__ == '__main__':
    print Solution().findMin([1,1,1,1,0,1,1])
    print Solution().findMin([1,0,1,1,1,1,1])