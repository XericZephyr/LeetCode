

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def rob_line(nums, start, end):
            odd_sum = nums[start]
            even_sum = 0
            for i in range(start+1, end+1):
                if (i - start) % 2:
                    even_sum = max(odd_sum, even_sum+nums[i])
                else:
                    odd_sum = max(even_sum, odd_sum+nums[i])
            return max(even_sum, odd_sum)

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return max(rob_line(nums, 0, len(nums)-2), rob_line(nums, 1, len(nums)-1))

if __name__ == '__main__':
    print Solution().rob([])
    print Solution().rob([1])
    print Solution().rob([1, 2])
    print Solution().rob([1, 2, 3, 4])
