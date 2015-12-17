

from utils import TreeNode

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        current_level = [(root, 0)]
        s = 0
        while current_level:
            next_level = []
            for node, val in current_level:
                pivot = val * 10 + node.val
                if node.left:
                    next_level.append((node.left, pivot))
                if node.right:
                    next_level.append((node.right, pivot))
                if node.left == node.right == None:
                    s += pivot
            current_level = next_level
        return s


if __name__ == '__main__':
    print Solution().sumNumbers(TreeNode.build_by_level_order([1,2,3]))
    print Solution().sumNumbers(TreeNode.build_by_level_order([1]))

