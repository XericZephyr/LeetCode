

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        elif n == 1:
            return [[1]]
        next_direction = {(0, 1): (1, 0),
                          (1, 0): (0, -1),
                          (0, -1): (-1, 0),
                          (-1, 0): (0, 1)}
        matrix = [[0] * n for _ in range(n)]
        r, c = 0, 0
        dr, dc = 0, 1
        num = 1
        while True:
            if not (matrix[r][c] == 0):
                break
            matrix[r][c] = num
            num += 1
            if 0 <= r + dr <= n - 1 and 0 <= c + dc <= n - 1 and \
                            matrix[r + dr][c + dc] == 0:
                r += dr
                c += dc
            else:
                dr, dc = next_direction[(dr, dc)]
                r += dr
                c += dc
        return matrix


if __name__ == '__main__':
    print Solution().generateMatrix(2)
    print Solution().generateMatrix(3)
    print Solution().generateMatrix(4)