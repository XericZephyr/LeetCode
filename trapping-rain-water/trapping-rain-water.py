

# class Solution(object):
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         def start_idx(height):
#             if height[0] > height[1]:
#                 yield 0
#             for i in range(1, len(height)-1):
#                 if height[i] > height[i-1] and height[i] > height[i+1]:
#                     yield i
#             if height[len(height)-2] < height[len(height)-1]:
#                 yield len(height)-1
#
#         if len(height) < 3:
#             return 0
#         total_capacity = 0
#         # find first container
#         g = start_idx(height)
#         try:
#             start, end = g.next(), g.next()
#         except StopIteration:
#             return 0
#         while True:
#             try:
#                 H = height[start] if height[start] < height[end] else height[end]
#                 for i in range(start, end):
#                     if height[i] < H:
#                         total_capacity += (H - height[i])
#                 start, end = end, g.next()
#             except StopIteration:
#                 break
#         return total_capacity


# class Solution(object):
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         if len(height) < 3:
#             return 0
#         start, end = 0, 1
#         while end < len(height):
#             while height[start] < height[end]:
#                 end += 1


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        currentHeight = 0
        left, right = 0, len(height) - 1
        area = 0
        while left < right:
            if height[left] < height[right]:
                currentHeight = max(currentHeight, height[left])
                area += currentHeight - height[left]
                left += 1
            else:
                currentHeight = max(currentHeight, height[right])
                area += currentHeight - height[right]
                right -= 1
        return area

if __name__ == '__main__':
    print Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
    print Solution().trap([5,2,1,2,1,5])
    print Solution().trap([0,2,0])