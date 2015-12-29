


class Solution(object):

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        if not nums:
            return nums
        ans = [0] * (len(nums)-k+1)
        dp = deque()
        for i in range(len(nums)):
            while dp and nums[dp[-1]] < nums[i]:
                dp.pop()
            dp.append(i)
            if i - dp[0] + 1 > k:
                dp.popleft()
            if i >= k - 1:
                ans[i-k+1] = nums[dp[0]]
        return ans

if __name__ == '__main__':
    print Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)