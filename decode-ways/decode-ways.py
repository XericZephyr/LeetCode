
#
#   Use BFS to count the leaf nodes
#
#
#   Take "1,2,3" as an example, we got tree {0, "12", "1", "3", '#', "2", "23", "3"}
#


#
#   Exponential, TLE
#
# class Solution(object):
#     def numDecodings(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if not len(s):
#             return 0
#         parent_stack = [0]
#         count = 0
#         while parent_stack:
#             current_node = parent_stack.pop()
#             if current_node == len(s) - 1:
#                 count += 1
#             elif current_node == len(s) - 2:
#                 if int(s[current_node:current_node+2]) <= 26:
#                     count += 2
#                 else:
#                     count += 1
#             else:
#                 parent_stack.append(current_node+1)
#                 if int(s[current_node:current_node+2]) <= 26:
#                     parent_stack.append(current_node+2)
#         return count

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1 if int(s) > 0 else 0
        plus2 = 1 if int(s[-1:]) > 0 else 0
        if int(s[-2]) > 0:
            plus1 = plus2 + (0 if int(s[-2:]) > 26 else 1)
        else:
            plus1 = 0
        for i in reversed(range(len(s)-2)):
            if int(s[i]) == 0:
                plus1, plus2 = 0, plus1
            else:
                plus1, plus2 = plus1 + (0 if int(s[i:i+2]) > 26 else plus2), plus1
        return plus1

if __name__ == '__main__':
    # print Solution().numDecodings("123")
    # print Solution().numDecodings("12")
    # print Solution().numDecodings("11")
    # print Solution().numDecodings("61")
    # print Solution().numDecodings("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948")
    print Solution().numDecodings("00")
    print Solution().numDecodings("300")
    print Solution().numDecodings("303")
    print Solution().numDecodings("0")
