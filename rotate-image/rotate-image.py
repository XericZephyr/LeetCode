



class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        def do_rotate(matrix, start, end):
            if start >= end:
                return
            for i in range(end-start):
                matrix[start][start+i], matrix[start+i][end], \
                matrix[end][end-i], matrix[end-i][start] = \
                matrix[end-i][start], matrix[start][start+i], \
                matrix[start+i][end], matrix[end][end-i],
            do_rotate(matrix, start+1, end-1)

        if len(matrix):
            do_rotate(matrix, 0, len(matrix)-1)

if __name__ == '__main__':
    matrix = [[1,2], [3,4]]
    Solution().rotate(matrix)
    print matrix
    matrix = [[1,2,3], [4,5,6],[7,8,9]]
    Solution().rotate(matrix)
    print matrix

