

class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self._integral_image = []
        if not matrix:
            return
        def cumsum(nums):
            res = [0]
            for i in range(len(nums)):
                res.append(res[i] + nums[i])
            return res
        # build integral image
        self._integral_image.append([0] * (1+len(matrix[0])))
        for i in range(len(matrix)):
            c_matrix = cumsum(matrix[i])
            self._integral_image.append([c_matrix[j] + self._integral_image[i][j] for j in range(len(c_matrix))])

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return (self._integral_image[row2+1][col2+1] - self._integral_image[row1][col2+1]) - \
               (self._integral_image[row2+1][col1] - self._integral_image[row1][col1])

if __name__ == '__main__':
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    numMatrix = NumMatrix(matrix)
    print numMatrix._integral_image
    print numMatrix.sumRegion(2, 1, 4, 3)
    print numMatrix.sumRegion(1,1,2,2)
    print numMatrix.sumRegion(1,2,2,4)

