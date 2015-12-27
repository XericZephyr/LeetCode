

from utils import TreeNode, ListNode

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None
        fast, prev, slow = head, None, head
        while fast and fast.next:
            fast = fast.next.next
            prev, slow = slow, slow.next
        root = TreeNode(slow.val)
        if prev:
            prev.next = None
        else:
            return root
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root


if __name__ == '__main__':
    TreeNode.print_in_level_order(Solution().sortedListToBST(ListNode.build_linked_list([1,2])))
    TreeNode.print_in_level_order(Solution().sortedListToBST(ListNode.build_linked_list([1])))
    TreeNode.print_in_level_order(Solution().sortedListToBST(ListNode.build_linked_list([1,2,3,4,5,6])))
    TreeNode.print_in_level_order(Solution().sortedListToBST(ListNode.build_linked_list([1,2,3,4,5])))
    TreeNode.print_in_level_order(Solution().sortedListToBST(ListNode.build_linked_list([])))
