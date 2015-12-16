

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        path_grid = [[0] * N for _ in range(M)]
        path_grid[0][0] = 1 if not obstacleGrid[0][0] else 0
        for i in range(1, M):
            path_grid[i][0] = path_grid[i-1][0] if not obstacleGrid[i][0] else 0
        for j in range(1, N):
            path_grid[0][j] = path_grid[0][j-1] if not obstacleGrid[0][j] else 0
        for i in range(1, M):
            for j in range(1, N):
                if obstacleGrid[i][j]:
                    path_grid[i][j] = 0
                else:
                    path_grid[i][j] = path_grid[i-1][j] + path_grid[i][j-1]
        return path_grid[-1][-1]

if __name__ == '__main__':
    # print Solution().uniquePathsWithObstacles([
    #     [0,0,0],
    #     [0,1,0],
    #     [0,0,0]
    # ])
    # print Solution().uniquePathsWithObstacles([
    #     [0,0,0,0],
    #     [0,1,0,0],
    #     [0,0,0,0],
    #     [0,0,0,0]
    # ])
    # print Solution().uniquePathsWithObstacles([
    #     [1]
    # ])
    # print Solution().uniquePathsWithObstacles([
    #     [1, 0],
    #     [0, 0]
    # ])
    #
    # print Solution().uniquePathsWithObstacles([
    #     [0, 1],
    #     [1, 0]
    # ])

    print Solution().uniquePathsWithObstacles([
        [0, 0],
        [1, 0]
    ])
