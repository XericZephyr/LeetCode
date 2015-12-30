

from utils import TreeNode

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        current = (root, [], 0)
        stack = []
        ret = []
        while current or stack:
            if current:
                node, prev_path, cumsum = current
                if node is None:
                    current = None
                    continue
                prev_path += [node.val]
                cumsum += node.val
                if node.right is None and node.left is None and cumsum == sum:
                    ret.append(prev_path)
                    current = None
                    continue
                if node.right:
                    stack.append((node.right, prev_path[:], cumsum))
                current = (node.left, prev_path[:], cumsum)
            else:
                current = stack.pop()
        return ret


if __name__ == '__main__':
    null = '#'
    print Solution().pathSum(TreeNode.build_by_level_order([5,4,8,11,null,13,4,7,2,null,null,5,1]), 22)
    print Solution().pathSum(TreeNode.build_by_level_order([5]), 5)
    print Solution().pathSum(TreeNode.build_by_level_order([]), 5)
    print Solution().pathSum(TreeNode.build_by_level_order([]), 0)
    print Solution().pathSum(TreeNode.build_by_level_order([5,1,2]), 6)
    print Solution().pathSum(TreeNode.build_by_level_order([5,1,2]), 7)
    print Solution().pathSum(TreeNode.build_by_level_order([5,1,2]), 0)
    print Solution().pathSum(TreeNode.build_by_level_order([-2,null,3]), -2)




