__author__ = 'clp'

from utils import ListNode

class Solution(object):

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        def link_len(head):
            node = head
            l = 0
            while node:
                l += 1
                node = node.next
            return l

        def link_index(head, idx):
            node = head
            for i in range(idx):
                if node is None:
                    break
                node = node.next
            return node

        lA, lB = link_len(headA), link_len(headB)
        if lA > lB:
            hA, hB = link_index(headA, lA - lB), headB
        elif lA < lB:
            hA, hB = headA, link_index(headB, lB - lA)
        else:
            hA, hB = headA, headB

        nA, nB = hA, hB
        while nA and nB:
            if nA == nB:
                return nA
            nA = nA.next
            nB = nB.next
        return None


if __name__ == '__main__':
    headC = ListNode.build_linked_list([4,5,6])
    headA = ListNode(1)
    headA.next = ListNode(2)
    headA.next.next = headC
    headB = headC

    print Solution().getIntersectionNode(headA, headB)
    print Solution().getIntersectionNode(None, None)
    print Solution().getIntersectionNode(ListNode.build_linked_list([1,3,5,7,9,11,13,15,17,19,21]),
                                         ListNode.build_linked_list([2]))
