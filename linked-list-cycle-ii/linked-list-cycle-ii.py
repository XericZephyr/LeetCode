
from utils import ListNode

#
#   This is very tricky, see proof in Gossip.md
#

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow
        return None


if __name__ == '__main__':
    head = ListNode.build_linked_list([1,2,3,4,5])
    head.next.next.next.next.next = head.next.next
    print Solution().detectCycle(head).val
    print Solution().detectCycle(None)


