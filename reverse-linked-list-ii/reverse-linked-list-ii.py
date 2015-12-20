
from utils import ListNode

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return None
        elif head.next is None:
            return head
        elif m == n:
            return head
        c = 1
        prev, current = None, head
        while current:
            if c == m:
                r_head_prev, r_head = prev, current
                prev, current = current, current.next
            elif m < c < n:
                next = current.next
                current.next = prev
                prev, current = current, next
            elif c == n:
                r_tail, r_tail_next = current, current.next
                current.next = prev
                prev, current = current, r_tail_next
            else:
                prev, current = current, current.next
            c += 1
        if r_head_prev:
            r_head_prev.next = r_tail
        r_head.next = r_tail_next

        return head if m > 1 else r_tail

if __name__ == '__main__':
    ListNode.print_linked_list(Solution().reverseBetween(ListNode.build_linked_list([1,2,3,4,5]), 2, 4))
    ListNode.print_linked_list(Solution().reverseBetween(ListNode.build_linked_list([1,2,3,4,5]), 1, 4))
    ListNode.print_linked_list(Solution().reverseBetween(ListNode.build_linked_list([1,2,3,4,5]), 1, 5))
    ListNode.print_linked_list(Solution().reverseBetween(ListNode.build_linked_list([1,2,3,4,5]), 2, 2))