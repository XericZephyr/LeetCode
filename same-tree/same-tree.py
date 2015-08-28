__author__ = 'clp'


from utils import TreeNode

class Solution(object):


    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        elif p.val == q.val:
            return True and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
