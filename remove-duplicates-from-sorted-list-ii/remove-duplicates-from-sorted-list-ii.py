

from utils import ListNode


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        hash_counter = {}
        current = head
        while current:
            k = current.val
            hash_counter[k] = hash_counter.get(k, 0) + 1
            current = current.next
        new_head = None
        prev, current = None, head
        while current:
            if hash_counter[current.val] >= 2:
                if prev:
                    prev.next = current.next
                prev, current = prev, current.next
            else:
                if not new_head:
                    new_head = current
                prev, current = current, current.next
        return new_head


if __name__ == '__main__':
    ListNode.print_linked_list(Solution().deleteDuplicates(ListNode.build_linked_list([1,1,2,3,1,1,2])))
    ListNode.print_linked_list(Solution().deleteDuplicates(ListNode.build_linked_list([1,1,2,3,1,1])))
    ListNode.print_linked_list(Solution().deleteDuplicates(ListNode.build_linked_list([1,2,3,3,4,4,5])))
    ListNode.print_linked_list(Solution().deleteDuplicates(ListNode.build_linked_list([1, 5])))
    ListNode.print_linked_list(Solution().deleteDuplicates(ListNode.build_linked_list([1])))
    ListNode.print_linked_list(Solution().deleteDuplicates(ListNode.build_linked_list([])))