__author__ = 'clp'

from utils import TreeNode

class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        current_level = [root]
        next_level = []
        result = []
        while current_level:
            level_value_list = []
            for current_node in current_level:
                level_value_list.append(current_node.val)
                next_level.append(current_node.left) if current_node.left else None
                next_level.append(current_node.right) if current_node.right else None
            current_level = next_level
            next_level = []
            result.append(level_value_list)
        return result




if __name__ == '__main__':
    t = TreeNode.build_by_level_order([1,2,3,'#','#',4,'#','#',5])
    print Solution().levelOrder(t)
    TreeNode.print_in_level_order(t)
    t2 = TreeNode.build_by_level_order([3,9,20,'#','#',15,7])
    print Solution().levelOrder(t2)
    t3 = TreeNode.build_by_level_order([3])
    print Solution().levelOrder(t3)