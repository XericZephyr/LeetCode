


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[right]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[left]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                elif nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right -= 1
        return False

if __name__ == '__main__':
    # nums = [4,5,6,7,0,1,2]
    # for i in nums:
    #     print Solution().search(nums, i)
    nums = [4,7,0,1,2]
    for i in nums:
        print Solution().search(nums, i)
    nums = [1,2,4,5,0]
    for i in nums:
        print Solution().search(nums, i)
    nums = [0,1,2,3,4]
    for i in nums:
        print Solution().search(nums, i)
    nums = [4,1,2,3]
    for i in nums:
        print Solution().search(nums, i)
    nums = [1,1,1,1,0,1,1]
    for i in nums:
        print Solution().search(nums, i)
    nums = [1,0,1,1,1,1,1]
    for i in nums:
        print Solution().search(nums, i)
    nums = [1,1,1,0,1,1,1]
    for i in nums:
        print Solution().search(nums, i)
    nums = [1,1,1,0,0,1,1,1]
    for i in nums:
        print Solution().search(nums, i)
    nums = [1,1,1,2,2,0,0,1,1,1]
    for i in nums:
        print Solution().search(nums, i)
    print Solution().search([1,1,1,1,1,0,1], 2)
    print Solution().search([1,1,1,1,1,0,1], 3)
    print Solution().search([1,1,1,1,1,0,1], 0)

