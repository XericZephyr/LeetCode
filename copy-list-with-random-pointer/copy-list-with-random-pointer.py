
from utils import RandomListNode

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None
        old2new_map = dict()
        new_head = RandomListNode(head.label)
        current = new_head
        old_next = head.next
        old2new_map[id(head)] = new_head
        while old_next:
            current.next = RandomListNode(old_next.label)
            old2new_map[id(old_next)] = current.next
            old_next = old_next.next
            current = current.next
        old_current, current = head, new_head
        while old_current and current:
            current.random = old2new_map[id(old_current.random)] if old_current.random else None
            old_current = old_current.next
            current = current.next
        return new_head


if __name__ == '__main__':
    head = RandomListNode(-1)
    head.next = RandomListNode(-1)
    head.random = head
    new_head = Solution().copyRandomList(head)
    print new_head.label, new_head.next.label