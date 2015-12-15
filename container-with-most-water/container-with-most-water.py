

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start, end = 0, len(height) - 1
        max_capacity = 0
        while start < end:
            H = min(height[start], height[end])
            W = end - start
            max_capacity = max(H*W, max_capacity)
            while start < end and height[start] <= H:
                start += 1
            while start < end and height[end] <= H:
                end -= 1
        return max_capacity

if __name__ == '__main__':
    print Solution().maxArea([1, 1])
    print Solution().maxArea([1, 2, 1])
    print Solution().maxArea([])