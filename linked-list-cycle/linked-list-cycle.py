
from utils import ListNode

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        prev, current = head, head.next
        head.next = None
        while current:
            if current == head:
                return True
            next = current.next
            current.next = prev
            prev, current = current, next
        return False

if __name__ == '__main__':
    head = ListNode.build_linked_list([1, 2, 3, 4, 5])
    head.next.next.next.next = head.next.next
    print Solution().hasCycle(head)
    head2 = ListNode.build_linked_list([1, 2, 3, 4, 5])
    print Solution().hasCycle(head2)
    print Solution().hasCycle(None)