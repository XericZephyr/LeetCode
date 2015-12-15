

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for center in range(1, len(nums)-1):
            left = 0
            right = len(nums) - 1
            while left < center < right:
                s = nums[left] + nums[center] + nums[right]
                if s < 0:
                    left += 1
                elif s == 0:
                    ret = [nums[left], nums[center], nums[right]]
                    if ret not in result:
                        result.append(ret)
                    left += 1
                    right -= 1
                else:
                    right -= 1
        return result


#
#   O(n^3) solution, doesn't work
#
#
# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         nums.sort()
#         result = []
#         for i in range(len(nums)-2):
#             if nums[i] + nums[i+1] + nums[i+2] > 0:
#                 break
#             if nums[i] + nums[-2] + nums[-1] < 0:
#                 continue
#             for j in range(i+2, len(nums)):
#                 if nums[i] + nums[i+1] + nums[j] > 0:
#                     break
#                 if nums[i] + nums[j-1] + nums[j] < 0:
#                     continue
#                 for center in range(i+1, j):
#                     # ret = [nums[i], nums[center], nums[j]]
#                     # s = sum(ret)
#                     s = nums[i] + nums[center] + nums[j]
#                     if s == 0:
#                         ret = [nums[i], nums[center], nums[j]]
#                         if ret not in result:
#                             result.append(ret)
#                     elif s > 0:
#                         break
#         return result


if __name__ == '__main__':
    print Solution().threeSum([-1, 0, 1, 2, -1, -4])
    print Solution().threeSum([8,-15,-2,-13,8,5,6,-3,-9,3,6,-6,8,14,-9,-8,-9,-6,-14,5,-7,3,-10,-14,-12,-11,12,-15,-1,12,8,-8,12,13,-13,-3,-5,0,10,2,-11,-7,3,4,-8,9,3,-10,11,5,10,11,-7,7,12,-12,3,1,11,9,-9,-4,9,-12,-6,11,-7,4,-4,-12,13,-8,-12,2,3,-13,-12,-8,14,14,12,9,10,12,-6,-1,8,4,8,4,-1,14,-15,-7,9,-14,11,9,5,14])