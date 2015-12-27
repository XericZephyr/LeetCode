

from utils import TreeNode

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def op(start, end):
            if start == end:
                return TreeNode(nums[start])
            elif end - start == 1:
                root = TreeNode(nums[start])
                root.right = TreeNode(nums[end])
                return root
            else:
                pivot = (start + end)/2
                root = TreeNode(nums[pivot])
                root.left = op(start, pivot-1)
                root.right = op(pivot+1, end)
                return root
        if len(nums) == 0:
            return None
        return op(0, len(nums)-1)


if __name__ == '__main__':
    TreeNode.print_in_level_order(Solution().sortedArrayToBST([1,2,3,4,5]))
    TreeNode.print_in_level_order(Solution().sortedArrayToBST([1,2,3,4,5,6]))
    TreeNode.print_in_level_order(Solution().sortedArrayToBST([1,2]))
    TreeNode.print_in_level_order(Solution().sortedArrayToBST([1]))
    TreeNode.print_in_level_order(Solution().sortedArrayToBST([]))
