




class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ret = []

        def place_n_row(state, r):

            def is_valid(state, r, c):
                for prev_r, prev_c in enumerate(state[:r]):
                    if prev_c == c or abs(prev_c-c) == abs(prev_r-r):
                        return False
                return True

            if r == n:
                tmp = [None] * n
                for i in state:
                    tmp[i] = '.' * state[i] + 'Q' + '.' * (n - state[i] - 1)
                ret.append(tmp)
            else:
                for c in range(n):
                    state[r] = c
                    if is_valid(state, r, c):
                        place_n_row(state, r+1)
                    state[r] = -1

        place_n_row([-1] * n, 0)
        return ret

if __name__ == '__main__':
    print Solution().solveNQueens(4)


