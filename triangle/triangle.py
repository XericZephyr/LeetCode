
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        total_row = len(triangle)
        distance_list = [triangle[0]]
        for i in range(1, total_row):
            distance_list.append([0]*len(triangle[i]))
            distance_list[i][0] = triangle[i][0] + distance_list[i-1][0]
            distance_list[i][-1] = triangle[i][-1] + distance_list[i-1][-1]
            for j in range(1, len(distance_list[i])-1):
                distance_list[i][j] = min((triangle[i][j]+distance_list[i-1][j],
                                           triangle[i][j]+distance_list[i-1][j-1]))
        return min(distance_list[-1])

if __name__ == '__main__':
    print Solution().minimumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ])
