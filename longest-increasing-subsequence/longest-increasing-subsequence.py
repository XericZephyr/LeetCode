

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        long_list = [0] * len(nums)
        long_list[-1] = 1
        for i in reversed(range(len(nums)-1)):
            max_len = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    max_len = max(max_len, long_list[j] + 1)
            long_list[i] = max_len
        return max(long_list)


if __name__ == '__main__':
    print Solution().lengthOfLIS([1,2,3])
    print Solution().lengthOfLIS([10,9,2,5,3,7,101,18])
    print Solution().lengthOfLIS([])
    print Solution().lengthOfLIS([1])
    print Solution().lengthOfLIS([2,1])
    print Solution().lengthOfLIS([1,3,6,7,9,4,10,5,6])