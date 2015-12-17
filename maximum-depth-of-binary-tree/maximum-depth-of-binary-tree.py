__author__ = 'clp'

from utils import TreeNode

class SolutionOLD(object):


    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def max_depth(root, level):
            if root is None:
                return -1
            else:
                return max([level, max_depth(root.left, level+1), max_depth(root.right, level+1)])

        return max_depth(root, 1) if root else 0


#
#   A clearer version
#

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


if __name__ == "__main__":
    print Solution().maxDepth(TreeNode.build_by_level_order([1, 2, 2, 3, 4, 4, 3]))
    print Solution().maxDepth(TreeNode.build_by_level_order([1, 2, '#']))
    print Solution().maxDepth(TreeNode.build_by_level_order([1, 2, 2, '#', 3, '#', 3]))
    print Solution().maxDepth(TreeNode.build_by_level_order([1]))
    print Solution().maxDepth(TreeNode.build_by_level_order([6,82,82,'#',53,53,'#',-58,'#','#',-58,'#',-85,-85,'#',-9,'#','#',-9,'#',48,48,'#',33,'#','#',33,81,'#','#',81,5,'#','#',5,61,'#','#',61,'#',9,9,'#',91,'#','#',91,72,7,7,72,89,'#',94,'#','#',94,'#',89,-27,'#',-30,36,36,-30,'#',-27,50,36,'#',-80,34,'#','#',34,-80,'#',36,50,18,'#','#',91,77,'#','#',95,95,'#','#',77,91,'#','#',18,-19,65,'#',94,'#',-53,'#',-29,-29,'#',-53,'#',94,'#',65,-19,-62,-15,-35,'#','#',-19,43,'#',-21,'#','#',-21,'#',43,-19,'#','#',-35,-15,-62,86,'#','#',-70,'#',19,'#',55,-79,'#','#',-96,-96,'#','#',-79,55,'#',19,'#',-70,'#','#',86,49,'#',25,'#',-19,'#','#',8,30,'#',82,-47,-47,82,'#',30,8,'#','#',-19,'#',25,'#',49]))
    print Solution().maxDepth(TreeNode.build_by_level_order([2,3,3,4,5,'#',4]))
    print Solution().maxDepth(TreeNode.build_by_level_order([2,3,3,4,5,5,4,'#','#',8,9,'#','#',9,8]))
    print Solution().maxDepth(TreeNode.build_by_level_order([]))