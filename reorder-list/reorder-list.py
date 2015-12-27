
from utils import ListNode

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        # make sure the length of list is more than 3
        if not head or not head.next or not head.next.next:
            return
        # find mid
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev, current = slow.next, slow.next.next
        slow.next = None
        prev.next = None
        # reverse the list from the mid
        while current:
            next = current.next
            current.next = prev
            prev, current = current, next
        # interleave the two list
        current1, current2 = head, prev
        while current1 and current2:
            current1_next, current2_next = current1.next, current2.next
            current1.next, current2.next = current2, current1_next
            current1, current2 = current1_next, current2_next

if __name__ == '__main__':
    l1 = ListNode.build_linked_list([1,2,3])
    Solution().reorderList(l1)
    ListNode.print_linked_list(l1)
    l1 = ListNode.build_linked_list([1,2])
    Solution().reorderList(l1)
    ListNode.print_linked_list(l1)
    l1 = ListNode.build_linked_list([])
    Solution().reorderList(l1)
    ListNode.print_linked_list(l1)
    l1 = ListNode.build_linked_list([1])
    Solution().reorderList(l1)
    ListNode.print_linked_list(l1)
    l1 = ListNode.build_linked_list([1,2,3,4,5,6])
    Solution().reorderList(l1)
    ListNode.print_linked_list(l1)
    l1 = ListNode.build_linked_list([1,2,3,4,5,6,7])
    Solution().reorderList(l1)
    ListNode.print_linked_list(l1)



