
from utils import TreeNode

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        current_level = [root]
        next_level = []
        result = []
        while current_level:
            result.append(current_level[-1].val)
            for node in current_level:
                next_level.extend([n for n in [node.left, node.right] if n is not None])
            current_level = next_level
            next_level = []
        return result

if __name__ == '__main__':
    print Solution().rightSideView(TreeNode.build_by_level_order([1, 2, 3, '#', 5, '#', 4]))
    print Solution().rightSideView(TreeNode.build_by_level_order([1]))
    print Solution().rightSideView(TreeNode.build_by_level_order(None))
