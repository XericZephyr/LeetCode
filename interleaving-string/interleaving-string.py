


# class Solution(object):
#     def isInterleave(self, s1, s2, s3):
#         """
#         :type s1: str
#         :type s2: str
#         :type s3: str
#         :rtype: bool
#         """
#         if len(s1) + len(s2) != len(s3):
#             return False
#
#         # DFS
#         stack = [(0, 0, 0)]
#         c = 0
#         max_stack_len = 0
#         while stack:
#             max_stack_len = max(max_stack_len, len(stack))
#             c += 1
#             i, j, k = stack.pop()
#             if k >= len(s3):
#                 print c
#                 print max_stack_len
#                 return True
#             if i < len(s1):
#                 if s1[i] == s3[k]:
#                     stack.append((i+1, j, k+1))
#             if j < len(s2):
#                 if s2[j] == s3[k]:
#                     stack.append((i, j+1, k+1))
#         print c
#         return False


# class Solution(object):
#     def isInterleave(self, s1, s2, s3):
#         """
#         :type s1: str
#         :type s2: str
#         :type s3: str
#         :rtype: bool
#         """
#         if len(s1) + len(s2) != len(s3):
#             return False
#
#         node = (0, 0, 0)
#         stack = []
#         c = 0
#         max_stack_len = 0
#         while node or stack:
#             max_stack_len = max(max_stack_len, len(stack))
#             c += 1
#             i, j, k = node
#             if k >= len(s3):
#                 print c
#                 print max_stack_len
#                 return True
#             node = ()
#             if j < len(s2) and s2[j] == s3[k]:
#                 stack.append((i, j+1, k+1))
#             if i < len(s1) and s1[i] == s3[k]:
#                 node = (i+1, j, k+1)
#             if not node:
#                 node = stack.pop()
#         print c
#         return False


#
#   Optimal Structure
#
#   i, j are 1-indexed
#   M[i][j] = /  True if i == j == 0
#             |  (s1[i] == s3[i] and M[i-1][j]) if j == 0
#             |  (s2[j] == s3[j] and M[i][j-1]) if i == 0
#             |  M[i-1][j] if s1[i] == s3[i+j-1], s2[j] != s3[i+j-1]  # because the s3 shift only from s1
#             |  M[i][j-1] if s2[j] == s3[i+j-1], s1[i] != s3[i+j-1]
#             |  M[i-1][j] or M[i][j-1] if s1[i] == s2[j] == s3[i+j-1]
#             \  False otherwise
#
#
#


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        if len(s1) + len(s2) != len(s3):
            return False
        if not len(s1):
            return s3 == s2
        if not len(s2):
            return s3 == s1

        s1_len, s2_len = len(s1), len(s2)
        M = [[None] * (1+s2_len) for _ in range(1+s1_len)]

        def _dfs(i, j):
            if M[i][j] is None:
                if i == j == 0:
                    M[i][j] = True
                elif i == 0:
                    M[i][j] = (s2[j-1] == s3[j-1]) and _dfs(0, j-1)
                elif j == 0:
                    M[i][j] = (s1[i-1] == s3[i-1]) and _dfs(i-1, 0)
                elif s1[i-1] == s2[j-1] == s3[i+j-1]:
                    M[i][j] = _dfs(i-1, j) or _dfs(i, j-1)
                elif s1[i-1] == s3[i+j-1]:
                    M[i][j] = _dfs(i-1, j)
                elif s2[j-1] == s3[i+j-1]:
                    M[i][j] = _dfs(i, j-1)
                else:
                    M[i][j] = False
            return M[i][j]

        return _dfs(len(s1), len(s2))

if __name__ == '__main__':
    from time import time
    # N = 500
    # t1 = time()
    # print Solution().isInterleave("ab"*N, "ab"*N, "ab"*(2*N))
    # print time()-t1
    t1 = time()
    print Solution().isInterleave("bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa",
                                  "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab",
                                  "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab")
    print time()-t1
    print Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac")
    print Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc")
    print Solution().isInterleave("baa", "aab", "babbab")
    print Solution().isInterleave(
        "baababbabbababbaaababbbbbbbbbbbaabaabaaaabaaabbaaabaaaababaabaaabaabbbbaabbaabaabbbbabbbababbaaaabab",
        "aababaaabbbababababaabbbababaababbababbbbabbbbbababbbabaaaaabaaabbabbaaabbababbaaaababaababbbbabbbbb",
        "babbabbabbababbaaababbbbaababbaabbbbabbbbbaaabbabaababaabaaabaabbbaaaabbabbaaaaabbabbaabaaaabbbbababbbababbabaabababbababaaaaaabbababaaabbaabbbbaaaaabbbaaabbbabbbbaaabaababbaabababbbbababbaaabbbabbbab")