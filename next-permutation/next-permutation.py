



class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # find the first nums[i] < nums[i-1] from the end
        begin = -1
        for i in reversed(range(len(nums)-1)):
            if nums[i] < nums[i+1]:
                begin = i
                break
        if begin >= 0:
            end = len(nums) - 1
            while nums[end] <= nums[begin]:
                end -= 1
            nums[begin], nums[end] = nums[end], nums[begin]
            end = len(nums) - 1
            for i in range((end-begin)/2):
                nums[begin+1+i], nums[end-i] = nums[end-i], nums[begin+i+1]
        else:
            for i in range(len(nums)/2):
                nums[i], nums[len(nums)-1-i] = nums[len(nums)-1-i], nums[i]
        return

if __name__ == '__main__':
    nums = [1,1,2]
    Solution().nextPermutation(nums)
    print nums
    nums = [1,5,1]
    Solution().nextPermutation(nums)
    print nums
    nums = [5,1,1]
    Solution().nextPermutation(nums)
    print nums
    nums = [1,1,5,1,1]
    Solution().nextPermutation(nums)
    print nums
    nums = [1,1,5,2,1]
    Solution().nextPermutation(nums)
    print nums
    nums = [1,2,3]
    print nums
    for _ in range(6):
        Solution().nextPermutation(nums)
        print nums
    nums = [1,1,2,3]
    print nums
    for _ in range(24):
        Solution().nextPermutation(nums)
        print nums
    # print Solution().nextPermutation([1,1,2])
