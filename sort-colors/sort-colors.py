
class Solution(object):

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p_red_tail = -1
        p_blue_head = len(nums)
        i = 0
        while i < p_blue_head and p_red_tail < p_blue_head:
            # print nums
            if nums[i] == 0:
                p_red_tail += 1
                nums[i], nums[p_red_tail] = nums[p_red_tail], nums[i]
                i = p_red_tail + 1
            elif nums[i] == 2:
                p_blue_head -= 1
                nums[i], nums[p_blue_head] = nums[p_blue_head], nums[i]
            else:
                i += 1


if __name__ == '__main__':
    # nums = [1, 1, 0, 0, 2, 2]
    # Solution().sortColors(nums)
    # print nums
    nums = [1,1,1,0,0,2,2,1,2,0,2,1]
    Solution().sortColors(nums)
    print nums

    nums = [2, 0, 0]
    Solution().sortColors(nums)
    print nums

    nums = [1, 0]
    Solution().sortColors(nums)
    print nums

    nums = [2, 2]
    Solution().sortColors(nums)
    print nums

    nums = [1, 1]
    Solution().sortColors(nums)
    print nums

    nums = [0, 0]
    Solution().sortColors(nums)
    print nums


