

from utils import ListNode

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None
        f_head, f_end, b_head, b_end = None, None, None, None
        current = head
        while current:
            if current.val < x:
                if not f_head:
                    f_head = current
                    f_end = f_head
                else:
                    f_end.next = current
                    f_end = f_end.next
            else:
                if not b_head:
                    b_head = current
                    b_end = b_head
                else:
                    b_end.next = current
                    b_end = b_end.next
            current = current.next
        if f_head:
            f_end.next = b_head
        if b_end:
            b_end.next = None
        return f_head if f_head else b_head

if __name__ == '__main__':
    ListNode.print_linked_list(Solution().partition(ListNode.build_linked_list([1, 4, 3, 2, 5, 2]), 3))
    ListNode.print_linked_list(Solution().partition(ListNode.build_linked_list([1, 4, 3, 2, 5, 2]), 6))
    ListNode.print_linked_list(Solution().partition(ListNode.build_linked_list([1, 4, 3, 2, 5, 2]), 1))
    ListNode.print_linked_list(Solution().partition(ListNode.build_linked_list([1, 4, 3, 2, 5, 2]), 2))
    ListNode.print_linked_list(Solution().partition(ListNode.build_linked_list([1]), 2))
    ListNode.print_linked_list(Solution().partition(None, 2))
