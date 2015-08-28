__author__ = 'clp'

from utils import ListNode

class Solution(object):

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        l1_node, l2_node = l1, l2
        l = dummy_new_head = ListNode(1)
        while l1_node and l2_node:
            if l1_node.val <= l2_node.val:
                l.next = ListNode(l1_node.val)
                l1_node = l1_node.next
            else:
                l.next = ListNode(l2_node.val)
                l2_node = l2_node.next
            l = l.next
        l.next = l1_node or l2_node
        return dummy_new_head.next

if __name__ == "__main__":
    ListNode.print_linked_list(ListNode.build_linked_list([1,2,3]))
    #print_ListNode(Solution().mergeTwoLists(None, None))
    #print_ListNode(Solution().mergeTwoLists(None, ListNode(1)))
    #print_ListNode(Solution().mergeTwoLists(build_ListNode([2]), build_ListNode([1])))
    #print_ListNode(Solution().mergeTwoLists(build_ListNode([1]), build_ListNode([2])))
    #print_ListNode(Solution().mergeTwoLists(build_ListNode([1,2,3]), build_ListNode([2, 5,7])))
    ListNode.print_linked_list(
        Solution().mergeTwoLists(
            ListNode.build_linked_list([1, 2, 3]),
            ListNode.build_linked_list([2, 5, 7])
        )
    )
