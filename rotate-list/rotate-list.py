

from utils import ListNode

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        if k == 0:
            return head
        # count the length and get last_node
        length = 0
        current = head
        while current:
            length += 1
            if current.next is None:
                last_node = current
            current = current.next
        k = k % length
        if k == 0:
            return head
        idx = 0
        current = head
        while current:
            if idx == length - k - 1:
                target_prev, target_current = current, current.next
            current = current.next
            idx += 1
        new_head = target_current
        last_node.next = head
        target_prev.next = None
        return new_head

if __name__ == '__main__':
    ListNode.print_linked_list(Solution().rotateRight(ListNode.build_linked_list([1,2,3,4,5]), 2))
    ListNode.print_linked_list(Solution().rotateRight(ListNode.build_linked_list([1,2,3,4,5]), 3))
    ListNode.print_linked_list(Solution().rotateRight(ListNode.build_linked_list([1,2,3,4,5]), 4))
    ListNode.print_linked_list(Solution().rotateRight(ListNode.build_linked_list([1,2,3,4,5]), 5))
    ListNode.print_linked_list(Solution().rotateRight(ListNode.build_linked_list([1,2,3,4,5]), 5))
    ListNode.print_linked_list(Solution().rotateRight(ListNode.build_linked_list([1,2]), 2))
