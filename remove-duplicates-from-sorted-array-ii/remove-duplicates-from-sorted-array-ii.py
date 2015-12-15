

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)
        i = 2
        j = 2
        while i < len(nums):
            if nums[i] == nums[j-1] == nums[j-2]:
                i += 1
            else:
                nums[j] = nums[i]
                i += 1
                j += 1
        return j

if __name__ == '__main__':
    nums = [2, 2, 2, 3]
    print Solution().removeDuplicates(nums)
    print nums
    nums = [2, 2, 2]
    print Solution().removeDuplicates(nums)
    print nums

    nums = []
    print Solution().removeDuplicates(nums)
    print nums
