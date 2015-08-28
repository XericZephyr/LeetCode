__author__ = 'clp'


from utils import TreeNode

#
#
#

# dead end
# class DeadSolution(object):
#
#
#     def isSymmetric(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         def is_palindrome(l):
#             # compare the tuple (left or right, val)
#             assert isinstance(l, list)
#             if len(l) % 2 and l[0][0] is not 0:
#                 return False
#             for i in range(int(len(l)/2)):
#                 if (l[i][0] == l[-(i+1)][0]) or not (l[i][1] == l[-(i+1)][1]):
#                     return False
#             return True
#
#         if root is None:
#             return True
#         current_level = [(0, root)]   # -1 for left, 0 for middle and 1 for right
#         next_level = []
#         while current_level:
#             level_value_list = []
#             for position, current_node in current_level:
#                 level_value_list.append((position, current_node.val))
#                 next_level.append((-1, current_node.left)) if current_node.left else None
#                 next_level.append((1, current_node.right)) if current_node.right else None
#             if not is_palindrome(level_value_list):
#                 return False
#             current_level = next_level
#             next_level = []
#         return True

class Solution(object):

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def compare(left, right):
            if left is None and right is None:
                return True
            elif left is None or right is None:
                return False
            else:
                return (left.val == right.val) and compare(left.left, right.right) and compare(left.right, right.left)

        return compare(root.left, root.right) if root else True

if __name__ == "__main__":
    print Solution().isSymmetric(TreeNode.build_by_level_order([1, 2, 2, 3, 4, 4, 3]))
    print Solution().isSymmetric(TreeNode.build_by_level_order([1, 2, '#']))
    print Solution().isSymmetric(TreeNode.build_by_level_order([1, 2, 2, '#', 3, '#', 3]))
    print Solution().isSymmetric(TreeNode.build_by_level_order([1]))
    print Solution().isSymmetric(TreeNode.build_by_level_order([6,82,82,'#',53,53,'#',-58,'#','#',-58,'#',-85,-85,'#',-9,'#','#',-9,'#',48,48,'#',33,'#','#',33,81,'#','#',81,5,'#','#',5,61,'#','#',61,'#',9,9,'#',91,'#','#',91,72,7,7,72,89,'#',94,'#','#',94,'#',89,-27,'#',-30,36,36,-30,'#',-27,50,36,'#',-80,34,'#','#',34,-80,'#',36,50,18,'#','#',91,77,'#','#',95,95,'#','#',77,91,'#','#',18,-19,65,'#',94,'#',-53,'#',-29,-29,'#',-53,'#',94,'#',65,-19,-62,-15,-35,'#','#',-19,43,'#',-21,'#','#',-21,'#',43,-19,'#','#',-35,-15,-62,86,'#','#',-70,'#',19,'#',55,-79,'#','#',-96,-96,'#','#',-79,55,'#',19,'#',-70,'#','#',86,49,'#',25,'#',-19,'#','#',8,30,'#',82,-47,-47,82,'#',30,8,'#','#',-19,'#',25,'#',49]))
    print Solution().isSymmetric(TreeNode.build_by_level_order([2,3,3,4,5,'#',4]))
    print Solution().isSymmetric(TreeNode.build_by_level_order([2,3,3,4,5,5,4,'#','#',8,9,'#','#',9,8]))
    # TreeNode.print_in_level_order(TreeNode.build_by_level_order([6,82,82,'#',53,53,'#',-58,'#','#',-58,'#',-85,-85,'#',-9,'#','#',-9,'#',48,48,'#',33,'#','#',33,81,'#','#',81,5,'#','#',5,61,'#','#',61,'#',9,9,'#',91,'#','#',91,72,7,7,72,89,'#',94,'#','#',94,'#',89,-27,'#',-30,36,36,-30,'#',-27,50,36,'#',-80,34,'#','#',34,-80,'#',36,50,18,'#','#',91,77,'#','#',95,95,'#','#',77,91,'#','#',18,-19,65,'#',94,'#',-53,'#',-29,-29,'#',-53,'#',94,'#',65,-19,-62,-15,-35,'#','#',-19,43,'#',-21,'#','#',-21,'#',43,-19,'#','#',-35,-15,-62,86,'#','#',-70,'#',19,'#',55,-79,'#','#',-96,-96,'#','#',-79,55,'#',19,'#',-70,'#','#',86,49,'#',25,'#',-19,'#','#',8,30,'#',82,-47,-47,82,'#',30,8,'#','#',-19,'#',25,'#',49]))

