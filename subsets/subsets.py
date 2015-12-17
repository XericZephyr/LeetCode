

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        nums.sort()

        def ksubset(k, start, end):
            if k == 0:
                return [[]]
            elif k == 1:
                return [[nums[i]] for i in range(start, end+1)]
            elif k >= 2:
                ret = []
                for i in range(start, end):
                    pivot = nums[i]
                    ret += [[pivot] + l for l in ksubset(k-1, i+1, end)]
                return ret

        return reduce(lambda x, y: x + y,
                      (ksubset(i, 0, len(nums)-1) for i in range(len(nums)+1)), [])

if __name__ == '__main__':
    print Solution().subsets([1,2,3])
    print Solution().subsets([1,2,3,5,6])