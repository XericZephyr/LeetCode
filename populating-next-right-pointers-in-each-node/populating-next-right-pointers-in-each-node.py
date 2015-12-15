
from utils import TreeLinkNode

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        current_level = [root]
        next_level = []
        while current_level:
            for i, node in enumerate(current_level[:-1]):
                node.next = current_level[i+1]
            current_level[-1].next = None
            for node in current_level:
                next_level.extend([n for n in [node.left, node.right] if n])
            current_level = next_level
            next_level = []
        return

if __name__ == '__main__':
    root = TreeLinkNode(1)
    root.left = TreeLinkNode(2)
    root.right = TreeLinkNode(3)
    print root.next
    print root.left.next
    print root.right.next
    Solution().connect(root)
    print root.next
    print root.left.next.val
    print root.right.next
