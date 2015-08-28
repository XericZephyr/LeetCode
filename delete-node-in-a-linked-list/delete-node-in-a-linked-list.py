__author__ = 'clp'

from utils import ListNode

class Solution(object):

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node is None:
            return
        current_node = node
        while current_node.next:
            current_node.val = current_node.next.val
            if current_node.next.next:
                current_node = current_node.next
            else:
                current_node.next = None

if __name__ == "__main__":
    l1 = ListNode.build_linked_list([1,2,3,4])
    l1_node_3 = l1.next.next
    Solution().deleteNode(l1_node_3)
    ListNode.print_linked_list(l1)