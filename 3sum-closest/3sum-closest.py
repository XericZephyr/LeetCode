

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def abs(num):
            return num if num >= 0 else -num
        nums.sort()
        min_target = None
        min_distance = max(abs(3*nums[-1]-target), abs(3*nums[0]-target))
        for center in range(1, len(nums)-1):
            left, right = 0, len(nums) - 1
            while left < center < right:
                s = nums[left] + nums[center] + nums[right]
                if s == target:
                    return target
                elif s < target:
                    left += 1
                else:
                    right -= 1
                if abs(s-target) <= min_distance:
                    min_target = s
                    min_distance = abs(s-target)
        return min_target

if __name__ == '__main__':
    print Solution().threeSumClosest([-1, 2, 1, -4], 1)
    print Solution().threeSumClosest([0, 0, 0], 1)
    print Solution().threeSumClosest([3, 3, 3], 1)

