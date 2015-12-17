__author__ = 'clp'

from utils import TreeNode

null = '#'

class Solution(object):

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def op(root):
            if root == None:
                return 0, True

            left_depth, left_balance = op(root.left)
            right_depth, right_balance = op(root.right)
            return max(left_depth, right_depth) + 1, \
                   (left_balance and right_balance and (-1 <= left_depth - right_depth <= 1))

        return op(root)[1]

if __name__ == '__main__':
    print Solution().isBalanced(TreeNode.build_by_level_order([1, 2, 3, 4, null, null, null, 5]))
    print Solution().isBalanced(TreeNode.build_by_level_order([1, 2, 3, 4, null, null, null]))


