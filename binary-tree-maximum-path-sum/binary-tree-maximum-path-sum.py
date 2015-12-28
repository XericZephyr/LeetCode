
from utils import TreeNode

null = '#'

# class Solution(object):
#     def maxPathSum(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         parent_stack = []
#         current_node, current_sum = root, 0
#         max_sum = 0
#         while current_node or parent_stack:
#             if current_node:
#                 current_sum += current_node.val
#                 parent_stack.append((current_node, current_sum))
#                 current_node = current_node.left
#             else:
#                 current_node, current_sum = parent_stack.pop()
#                 if None == current_node.left == current_node.right:
#                     max_sum = max(max_sum, current_sum)
#                 current_node = current_node.right
#         return max_sum

#
#   Think {1, 2, 3}, How many possible path? , Think more generally?
#

class Solution(object):
    def maxPathSum(self, root):
        def dfs(node):
            l = r = 0
            ls = rs = None
            if node.left:
                l, ls = dfs(node.left)
                l = max(l, 0)
            if node.right:
                r, rs = dfs(node.right)
                r = max(r, 0)
            return max(node.val + max(l, r), node.val), max(node.val + l + r, ls, rs)

        if root:
            return dfs(root)[-1]
        return 0

if __name__ == '__main__':
    print Solution().maxPathSum(TreeNode.build_by_level_order([1,2,3]))
    print Solution().maxPathSum(TreeNode.build_by_level_order([1,2,3,null,null,4,5]))
    print Solution().maxPathSum(TreeNode.build_by_level_order([-1, -2, -3]))
    print Solution().maxPathSum(TreeNode.build_by_level_order([]))
    print Solution().maxPathSum(TreeNode.build_by_level_order([1]))