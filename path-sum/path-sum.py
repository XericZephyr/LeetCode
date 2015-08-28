__author__ = 'clp'


from utils import TreeNode

class Solution(object):


    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        def path_sum(root, sum, accumulate_sum):
            assert root is not None
            accumulate_sum += root.val
            if root.left is None and root.right is None:
                return (accumulate_sum == sum)
            left_result = path_sum(root.left, sum, accumulate_sum) if root.left else False
            if left_result:
                return True
            right_result = path_sum(root.right, sum, accumulate_sum) if root.right else False
            return left_result or right_result

        return path_sum(root, sum, 0) if root else False


if __name__ == '__main__':
    t = TreeNode.build_by_level_order([5, 4, 8, 11, '#', 13, 4, 7, 2, '#', '#', '#', 1])
    print Solution().hasPathSum(t, 22)
    print Solution().hasPathSum(t, 15)
    print Solution().hasPathSum(t, 9)
    print Solution().hasPathSum(t, 13)
    print Solution().hasPathSum(t, 16)
    print Solution().hasPathSum(t, 26)
    print Solution().hasPathSum(t, 18)