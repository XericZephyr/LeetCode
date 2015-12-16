


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right - 1:
            mid = (left + right)/2
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left if (left == len(nums) - 1) or (nums[left] > nums[right]) else right

if __name__ =='__main__':
    print Solution().findPeakElement([1,2,3,1])
    print Solution().findPeakElement([1,2,1])
    print Solution().findPeakElement([1,2,3])
    print Solution().findPeakElement([3,2,1])
    print Solution().findPeakElement([1,2,3,2,3,1])
