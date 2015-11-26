

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        path_matrix = [[0]*n for _ in range(m)]
        level_list = [(0, 0)]
        new_level_list = []
        while level_list or new_level_list:
            if not level_list:
                level_list = new_level_list
                new_level_list = []
            r, c = level_list.pop()
            if r == c == 0:
                path_matrix[r][c] = 1
            elif r == 0:
                path_matrix[r][c] = path_matrix[r][c-1]
            elif c == 0:
                path_matrix[r][c] = path_matrix[r-1][c]
            else:
                path_matrix[r][c] = path_matrix[r-1][c] + path_matrix[r][c-1]
            if 0 <= r+1 < m and 0 <= c < n and (r+1, c) not in new_level_list:
                new_level_list.append((r+1, c))
            if 0 <= r < m and 0 <= c+1 < n and (r, c+1) not in new_level_list:
                new_level_list.append((r, c+1))
        return path_matrix[m-1][n-1]

if __name__ == '__main__':
    print Solution().uniquePaths(3, 4)
    print Solution().uniquePaths(2, 4)
    print Solution().uniquePaths(2, 3)
