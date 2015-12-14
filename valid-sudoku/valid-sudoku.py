

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        # check vertically
        for j in range(9):
            hash_table = [0] * 9
            for i in range(9):
                if not (board[i][j] == '.'):
                    num = int(board[i][j])
                    if hash_table[num - 1]:
                        return False
                    else:
                        hash_table[num-1] = 1
        # check horizontally
        for i in range(9):
            hash_table = [0] * 9
            for j in range(9):
                if not (board[i][j] == '.'):
                    num = int(board[i][j])
                    if hash_table[num - 1]:
                        return False
                    else:
                        hash_table[num-1] = 1
        # check each grid
        for i in range(9):
            hash_table = [0] * 9
            start_i, start_j = (i / 3) * 3, (i % 3) * 3
            for j in range(9):
                current_i, current_j = start_i + (j / 3), start_j + (j % 3)
                if not (board[current_i][current_j] == '.'):
                    num = int(board[current_i][current_j])
                    if hash_table[num-1]:
                        return False
                    else:
                        hash_table[num-1] = 1
        return True


if __name__ == '__main__':
    Solution().isValidSudoku(board=[".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])


