

class Solution(object):

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 0 == len(nums):
            return 0
        rob_list = [0] * len(nums)
        non_rob_list = [0] * len(nums)
        rob_list[0] = nums[0]
        for i in range(1, len(nums)):
            rob_list[i] = non_rob_list[i-1]+nums[i]
            non_rob_list[i] = max((rob_list[i-1], non_rob_list[i-1]))
        return max((rob_list[-1], non_rob_list[-1]))

if __name__ == '__main__':
    print Solution().rob([1, 2, 3, 2, 5])
    print Solution().rob([1, 1, 1, 1, 1])
    print Solution().rob([])