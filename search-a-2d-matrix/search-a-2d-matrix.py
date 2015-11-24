
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for r in range(len(matrix)):
            if matrix[r][0] <= target <= matrix[r][-1]:
                for c in range(len(matrix[r])):
                    if matrix[r][c] == target:
                        return True
                return False
            elif target < matrix[r][0]:
                return False
        return False


if __name__ == '__main__':
    print Solution().searchMatrix([
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], 3)
    print Solution().searchMatrix([
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], 1)
    print Solution().searchMatrix([
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], 0)
    print Solution().searchMatrix([
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], 50)
    print Solution().searchMatrix([
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], 75)

