


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for idx, num in enumerate(nums):
            if num >= target:
                return idx
            else:
                pass
        return len(nums)


#
#   Binary Search

# class Solution(object):
#     def searchInsert(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         def doSearchInsert(nums, target, start, end):
#             if start == end:
#                 if target == nums[start]:
#                     return start+1
#                 else:
#                     return -1
#             elif target < nums[start]:
#                 return -1
#             elif target > nums[end]:
#                 return end
#             else:
#                 pivot = int(start+end)/2
#                 return max((doSearchInsert(nums, target, start, pivot),
#                             doSearchInsert(nums, target, pivot+1, end)))
#         return doSearchInsert(nums, target, 0, len(nums)-1)


if __name__ == '__main__':
    print Solution().searchInsert([1, 3, 5, 6], 5)
    print Solution().searchInsert([1, 3, 5, 6], 2)
    print Solution().searchInsert([1, 3, 5, 6], 7)
    print Solution().searchInsert([1, 3, 5, 6], 0)
