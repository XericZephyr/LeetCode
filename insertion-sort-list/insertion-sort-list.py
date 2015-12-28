
from utils import ListNode

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        sorted_head, sorted_end = head, head
        current = head.next
        head.next = None
        while current:
            current_next = current.next
            if current.val < sorted_head.val:
                current.next = sorted_head
                sorted_head = current
            else:
                sorted_prev, sorted_current = sorted_head, sorted_head.next
                while sorted_current:
                    if sorted_current.val > current.val:
                        sorted_prev.next = current
                        current.next = sorted_current
                        break
                    sorted_prev, sorted_current = sorted_current, sorted_current.next
                if current.val >= sorted_end.val:
                    current.next = None
                    sorted_end.next = current
                    sorted_end = current

            current = current_next

        return sorted_head

if __name__ == '__main__':
    ListNode.print_linked_list(Solution().insertionSortList(ListNode.build_linked_list([5,1,4,3,2])))
    ListNode.print_linked_list(Solution().insertionSortList(ListNode.build_linked_list([1])))
    ListNode.print_linked_list(Solution().insertionSortList(ListNode.build_linked_list([])))
    ListNode.print_linked_list(Solution().insertionSortList(ListNode.build_linked_list([8,7])))
    ListNode.print_linked_list(Solution().insertionSortList(ListNode.build_linked_list([8,7,1])))
    ListNode.print_linked_list(Solution().insertionSortList(ListNode.build_linked_list([1])))
