__author__ = 'clp'

from utils import ListNode

class Solution(object):

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head is not None and head.val == val:
            head = head.next
        if not head:
            return None
        current_node = head
        while current_node.next:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
        return head

if __name__ == '__main__':
    ListNode.print_linked_list(Solution().removeElements(ListNode.build_linked_list([1,2,3,4,5,6]),  6))
    ListNode.print_linked_list(Solution().removeElements(ListNode.build_linked_list([1,1,3,4,56]),  1))
    ListNode.print_linked_list(Solution().removeElements(ListNode.build_linked_list([2,1,3,4,4,4,4]),  4))
    ListNode.print_linked_list(Solution().removeElements(ListNode.build_linked_list([1]),  1))