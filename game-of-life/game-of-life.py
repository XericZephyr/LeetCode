



class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def integral_image(board):
            M, N = len(board), len(board[0])
            integral = [[0] * (N+1) for _ in range(M+1)]
            for i in range(1, M+1):
                for j in range(1, N+1):
                    integral[i][j] = integral[i-1][j] + integral[i][j-1] - integral[i-1][j-1] + board[i-1][j-1]
            return integral

        if not board:
            return
        M, N = len(board), len(board[0])
        it = integral_image(board)
        for i in range(M):
            for j in range(N):
                tr, tc = max(0, i-1), max(0, j-1)
                br, bc = min(M, i+2), min(N, j+2)
                n = it[br][bc] + it[tr][tc] - it[br][tc] - it[tr][bc]
                if board[i][j]:
                    if n < 3 or n > 4:
                        board[i][j] = 0
                else:
                    if n == 3:
                        board[i][j] = 1
        return

if __name__ == '__main__':
    board = [[0, 1, 0], [1, 0, 1], [1, 1, 1]]
    Solution().gameOfLife(board)
    print board



