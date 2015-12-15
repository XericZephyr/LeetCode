

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        residual_dict = {}
        for i, num in enumerate(nums):
            if num in residual_dict:
                return [residual_dict[num], i+1]
            else:
                residual_dict[target-num] = i+1
        return []

if __name__ == '__main__':
    print Solution().twoSum([2, 7, 11, 15], 9)