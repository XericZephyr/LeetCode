

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nonzero_idx = 0
        for current_idx in range(len(nums)):
            if nums[current_idx]:
                nums[nonzero_idx] = nums[current_idx]
                nonzero_idx += 1
            else:
                pass
        for zero_idx in range(nonzero_idx, len(nums)):
            nums[zero_idx] = 0


if __name__ == '__main__':
    nums = [1, 0, 2, 0, 4]
    Solution().moveZeroes(nums)
    print nums
    nums = [0, 1, 0, 3, 12, 0]
    Solution().moveZeroes(nums)
    print nums
