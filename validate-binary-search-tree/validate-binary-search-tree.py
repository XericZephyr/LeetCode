from utils import TreeNode


class Solution(object):

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def in_order_tree(node):
            if node.left:
                for x in in_order_tree(node.left):
                    yield x
            yield node.val
            if node.right:
                for x in in_order_tree(node.right):
                    yield x
        if not root:
            return True
        old_value = None
        print list(in_order_tree(root))
        for val in in_order_tree(root):
            if not old_value:
                old_value = val
                continue
            if val <= old_value:
                return False
            old_value = val
        return True

if __name__ == '__main__':
    # print Solution().isValidBST(TreeNode.build_by_level_order([1, '#', 2, 3, '#']))
    # print Solution().isValidBST(TreeNode.build_by_level_order([2, 1, 3]))
    # print Solution().isValidBST(TreeNode.build_by_level_order([]))
    # print Solution().isValidBST(TreeNode.build_by_level_order([2]))
    # print Solution().isValidBST(TreeNode.build_by_level_order([10, 5, 15, '#', '#', 6, 20]))
    # print Solution().isValidBST(TreeNode.build_by_level_order([1, 1, '#']))
    # print Solution().isValidBST(TreeNode.build_by_level_order([0]))
    print Solution().isValidBST(TreeNode.build_by_level_order([0, '#', -1]))
