
#
#   Quite close, TLE solution, we need to optimize the is_palindrome
#

class SolutionTLEDP(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        cut = [None] * len(s)
        P = [[None] * (1+len(s)) for _ in range(1+len(s))]
        cut[-1] = 0

        c = [0, 0]

        def is_palindrome(i, j):
            c[0] += 1
            if P[i][j] is None:
                for k in range(i, i+1+(j-i)/2):
                    if s[k] != s[j-1-(k-i)]:
                        P[i][j] = False
                        break
                if P[i][j] is None:
                    P[i][j] = True
            return P[i][j]

        def _preprocess():
            i = 0
            while i < len(s):
                j = i + 1
                while j < len(s) and s[j] == s[i]:
                    j += 1

                for p in range(i, j):
                    for q in range(p, j+1):
                        P[p][q] = True
                i = j


        def _dp(i):
            c[1] += 1
            if not cut[i]:
                if is_palindrome(i, len(s)):
                    cut[i] = 0
                else:
                    # find max palindrome
                    cut[i] = min([1+_dp(j) for j in reversed(range(i+1, len(s))) if is_palindrome(i, j)])

            return cut[i]

        if is_palindrome(0, len(s)):
            return 0
        else:
            _preprocess()
            ret = _dp(0)
            print c
            return ret


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        P = [[False] * len(s) for _ in range(len(s))]
        cut = [len(s)] * len(s)
        cut[0] = 0
        for j in range(len(s)):
            for i in range(j+1):
                if s[i] == s[j] and (i+1 > j-1 or P[i+1][j-1]):
                    P[i][j] = True
                    cut[j] = min(cut[j], 1+cut[i-1]) if i > 0 else 0
        return cut[-1]

if __name__ == '__main__':
    print Solution().minCut("aab")
    print Solution().minCut("a")
    print Solution().minCut("")
    print Solution().minCut("abadjajfkdalaaaaa")
    # print Solution().minCut("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    from time import time
    t1 = time()
    print Solution().minCut("a"*500+'bb'+'a'*400)
    print time()-t1
