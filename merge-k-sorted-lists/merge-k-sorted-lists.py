
from utils import ListNode

b = ListNode.build_linked_list

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from heapq import heapify, heappop, heappush
        h = [(l.val, l) for l in lists if l]
        heapify(h)
        new_head = current = None
        while len(h):
            val, node = heappop(h)
            if node.next:
                heappush(h, (node.next.val, node.next))
            if not new_head:
                current = new_head = node
            else:
                current.next = node
                current = node
                node.next = None
        return new_head


if __name__ == '__main__':
    ListNode.print_linked_list(Solution().mergeKLists([b([1,3,5,7,9]), b([2,4,6,8,10]), b([12,14,15,17,19])]))
    ListNode.print_linked_list(Solution().mergeKLists([b([1,3,5,7,9]), b([2,4,6,8,10]), b([])]))
    ListNode.print_linked_list(Solution().mergeKLists([b([]), b([])]))
    ListNode.print_linked_list(Solution().mergeKLists([]))


