


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or target < nums[0] or target > nums[-1]:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        while left < right - 1:
            if nums[left] == nums[right] == target:
                break
            mid = (left + right) / 2
            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                for i in range(mid-1, left-1, -1):
                    if nums[i] != target:
                        left = i + 1
                        break
                for i in range(mid+1, right+1):
                    if nums[i] != target:
                        right = i - 1
                        break
                break
        if nums[left] == nums[right] == target:
            return [left, right]
        elif nums[left] == target:
            return [left, left]
        elif nums[right] == target:
            return [right, right]
        else:
            return [-1, -1]

if __name__ == '__main__':
    print Solution().searchRange([5,7,7,8,8,10], 8)
    print Solution().searchRange([5,7,7,8,8,10], 10)
    print Solution().searchRange([5,7,7,8,8,10], 5)
    print Solution().searchRange([1,1,1,1,1,1,1,2], 1)
    print Solution().searchRange([1,1,1,1,1,1,1,2], 2)
    print Solution().searchRange([1], 2)
    print Solution().searchRange([1], 1)