


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        ret = [0]

        def place_queen(state, r):

            def is_valid(state, r, c):
                for prev_r, prev_c in enumerate(state[:r]):
                    if prev_c == c or (abs(prev_r-r) == abs(prev_c-c)):
                        return False
                return True

            if r == n:
                ret[0] += 1
            else:
                for c in range(n):
                    if is_valid(state, r, c):
                        state[r] = c
                        place_queen(state, r+1)
                        state[r] = -1

        place_queen([-1] * n, 0)
        return ret[0]


if __name__ == '__main__':
    for n in range(3, 9):
        print Solution().totalNQueens(n)
