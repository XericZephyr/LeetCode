


# class Solution(object):
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         tr, tc = 0, 0
#         br, bc = (len(matrix)-1, len(matrix[0])-1)
#         if target > matrix[br][bc] or target < matrix[tr][tc]:
#             return False
#         while tr < br-1 and tc < bc-1:
#             mr, mc = (tr + br)/2, (tc + bc)/2
#             if matrix[mr][mc] == target:
#                 return True
#             elif matrix[mr][mc] < target:
#                 tr, tc = mr+1, mc+1
#             else:
#                 br, bc = mr, mc
#         if matrix[tr][tc] > target:
#             tr, tc = tr-1, tc-1
#         if matrix[br][bc] < target:
#             br, bc = br+1, bc+1
#         for i in range(tr, br+1):
#             for j in range(tc, bc+1):
#                 if target == matrix[i][j]:
#                     return True
#         return False


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i, j = 0, len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False

if __name__ == '__main__':
    matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
    print Solution().searchMatrix(matrix, 4)
    print Solution().searchMatrix(matrix, -1)
    print Solution().searchMatrix(matrix, 50)
    print Solution().searchMatrix(matrix, 20)
    print Solution().searchMatrix(matrix, 5)
    print Solution().searchMatrix(matrix, 1)
    print Solution().searchMatrix(matrix, 26)
    print Solution().searchMatrix(matrix, 15)
    print Solution().searchMatrix(matrix, 17)