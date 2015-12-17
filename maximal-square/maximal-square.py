


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def integral_image(matrix):
            M, N = len(matrix), len(matrix[0])
            integral = [[0] * (N+1) for _ in range(M+1)]
            for i in range(1, M+1):
                for j in range(1, N+1):
                    integral[i][j] = integral[i-1][j] + integral[i][j-1] - integral[i-1][j-1] + matrix[i-1][j-1]
            return integral

        if not matrix:
            return 0
        M, N = len(matrix), len(matrix[0])
        if not M or not N:
            return 0
        matrix = [[int(i) for i in list(line)] for line in matrix]
        it = integral_image(matrix)
        max_square = max(matrix[0] + [matrix[0][j] for j in range(N)])
        for i in range(1, M+1):
            for j in range(1, N+1):
                for n in range(1, 1+min(i, j)):
                    s = it[i][j] + it[i-n][j-n] - it[i-n][j] - it[i][j-n]
                    if s == n * n:
                        max_square = max(max_square, s)
                    else:
                        break
        return max_square


if __name__ == '__main__':
    print Solution().maximalSquare([
        "10100", "10111", "11111", "10010"
    ])
    print Solution().maximalSquare([
        "00", "00"
    ])
    print Solution().maximalSquare([
        "11", "11"
    ])

    # print Solution().maximalSquare([
    #     [1,0,1,0,0],
    #     [1,0,1,1,1],
    #     [1,1,1,1,1],
    #     [1,0,0,1,0]
    # ])

