
from utils import TreeNode

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        parent_stack = []
        node = root
        count = 0
        while parent_stack or node:
            if node:
                parent_stack.append(node)
                node = node.left
            else:
                node = parent_stack.pop()
                count += 1
                if count == k:
                    return node.val
                node = node.right

if __name__ == '__main__':
    print Solution().kthSmallest(TreeNode.build_by_level_order([2, 1, 3]), 2)
    print Solution().kthSmallest(TreeNode.build_by_level_order([2, 1, 3]), 4)
    print Solution().kthSmallest(None, 2)
    print Solution().kthSmallest(None, 4)
    print Solution().kthSmallest(None, 4)