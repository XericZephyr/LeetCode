__author__ = 'clp'

class Solution(object):

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def is_balanced(root):

            def depth(root):
                if root is None:
                    return -1
                elif root.left is None and root.right is None:
                    return 0
                left_depth = depth(root.left)+1
                right_depth = depth(root.right)+1
                if
                return max([left_depth, right_depth])


