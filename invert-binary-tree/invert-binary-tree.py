__author__ = 'clp'

from utils import TreeNode

class Solution(object):

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def invert_tree(root):
            if root is None:
                return None
            root.left, root.right = root.right, root.left
            invert_tree(root.left)
            invert_tree(root.right)

        if root:
            invert_tree(root)
        return root

if __name__ == '__main__':
    TreeNode.print_in_level_order(Solution().invertTree(TreeNode.build_by_level_order([4, 2, 7, 1, '#',6,9])))
    TreeNode.print_in_level_order(Solution().invertTree(TreeNode.build_by_level_order([])))
