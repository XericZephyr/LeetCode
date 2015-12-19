


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        next_direction = {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}
        if not matrix:
            return []
        M, N = len(matrix), len(matrix[0])
        visit = [[0] * N for _ in range(M)]
        ret = []
        r, c = 0, 0
        dr, dc = 0, 1
        while True:
            ret.append(matrix[r][c])
            visit[r][c] = 1
            nr, nc = r + dr, c + dc
            if 0 <= nr < M and 0 <= nc < N and visit[nr][nc] == 0:
                r, c = nr, nc
            else:
                dr, dc = next_direction[(dr, dc)]
                nr, nc = r + dr, c + dc
                if not (0 <= nr < M and 0 <= nc < N and visit[nr][nc] == 0):
                    break
                else:
                    r, c = nr, nc
        return ret

if __name__ == '__main__':
    print Solution().spiralOrder([[ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]])


