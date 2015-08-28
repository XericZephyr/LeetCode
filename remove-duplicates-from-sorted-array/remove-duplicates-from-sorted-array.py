__author__ = 'clp'


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if len(nums) <= 1:
            # return lenght of list for empty list or single element list
            return len(nums)
        nums.sort()
        index = 1
        while len(nums) > index:
            if nums[index] == nums[index - 1]:
                nums.pop(index)
            else:
                index += 1
        return len(nums)

if __name__ == "__main__":
    nums = [6, 6, 1, 1, 2, 5]
    print Solution().removeDuplicates(nums)
    print nums
