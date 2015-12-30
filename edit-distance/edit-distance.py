


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        M, N = len(word1), len(word2)
        distance = [[None] * (1+N) for _ in range(1+M)]

        def _dp(r, c):
            if distance[r][c] is None:
                if r == 0:
                    distance[r][c] = c
                elif c == 0:
                    distance[r][c] = r
                elif word1[r-1] == word2[c-1]:
                    distance[r][c] = _dp(r-1, c-1)
                else:
                    distance[r][c] = 1+min((_dp(r-1, c), _dp(r, c-1), _dp(r-1, c-1)))

            return distance[r][c]

        return _dp(M, N)

if __name__ == '__main__':
    print Solution().minDistance("word1", "word2")
    print Solution().minDistance("wrad", "word")