

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums)-3):
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[-3] + nums[-2] + nums[-1] < target:
                continue
            for j in range(i + 3, len(nums)):
                left = i + 1
                right = j - 1
                if nums[i] + nums[j-2] + nums[j-1] + nums[j] < target:
                    continue
                if nums[i] + nums[i+1] + nums[i+2] + nums[j] > target:
                    break
                while left < right:
                    s = nums[left] + nums[right] + nums[i] + nums[j]
                    if s == target:
                        ret = [nums[i], nums[left], nums[right], nums[j]]
                        if ret not in result:
                            result.append(ret)
                        left += 1
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1
        return result


if __name__ == "__main__":
    print Solution().fourSum([1, 0, -1, 0, -2, 2], 0)
    print Solution().fourSum([1, 0, -1, 0, 0, 0, 0, -2, 2], 0)
