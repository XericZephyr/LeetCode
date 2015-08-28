__author__ = 'clp'

from utils import ListNode

class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return None

        global new_head

        def reverse_list(node):
            global new_head
            if node.next is None:
                new_head = node
                return node
            next_node = reverse_list(node.next)
            next_node.next = node
            return node

        reverse_list(head)
        head.next = None
        return new_head


if __name__ == '__main__':
    l = ListNode.build_linked_list([])
    l = ListNode.build_linked_list([1])
    # l = ListNode.build_linked_list([1, 2, 3, 4, 5])
    ListNode.print_linked_list(Solution().reverseList(l))