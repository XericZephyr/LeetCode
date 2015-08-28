__author__ = 'clp'

from utils import ListNode

class Solution(object):

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        def count_intersection(headA, headB):
            if headA == headB:
                if headA.next is None:
                    return 1
                else:
                    return 1 + count_intersection(headA.next, headB.next)
            elif headA.next is None:
                return count_intersection(headA, headB.next)
            elif headB.next is None:
                return count_intersection(headA.next, headB)
            else:
                return count_intersection(headA.next, headB.next)

        def get_intersection_head(headA, intersection_count):
            if intersection_count == 0:
                return None
