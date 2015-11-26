class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if 0 == len(grid) or grid is None:
            return 0
        m, n = len(grid), len(grid[0])
        distance_grid = [[0] * n for _ in range(m)]
        coordinate_list = [(0, 0)]
        new_coordinate_list = []
        while coordinate_list or new_coordinate_list:
            if not coordinate_list:
                coordinate_list = new_coordinate_list
                new_coordinate_list = []
            r, c = coordinate_list.pop()
            if r == c == 0:
                distance_grid[r][c] = grid[r][c]
            elif r == 0:
                distance_grid[r][c] = distance_grid[r][c-1] + grid[r][c]
            elif c == 0:
                distance_grid[r][c] = distance_grid[r-1][c] + grid[r][c]
            else:
                distance_grid[r][c] = min((distance_grid[r-1][c] + grid[r][c], distance_grid[r][c-1] + grid[r][c]))
            if 0 <= r+1 < m and 0 <= c < n and (r+1, c) not in new_coordinate_list:
                new_coordinate_list.append((r+1, c))
            if 0 <= r < m and 0 <= c+1 < n and (r, c+1) not in new_coordinate_list:
                new_coordinate_list.append((r, c+1))

        return distance_grid[m-1][n-1]

if __name__ == '__main__':
    print Solution().minPathSum([[1,2,3], [4,5,6], [7,8,9]])
    print Solution().minPathSum([[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],
                                 [9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],
                                 [8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],
                                 [6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],
                                 [7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],
                                 [9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],
                                 [1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],
                                 [3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],
                                 [1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],
                                 [5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],
                                 [2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],
                                 [0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]])



