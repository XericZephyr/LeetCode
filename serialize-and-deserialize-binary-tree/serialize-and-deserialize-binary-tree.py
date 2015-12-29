

from utils import TreeNode

null = '#'


# class Codec:
#
#     def serialize(self, root):
#         """Encodes a tree to a single string.
#
#         :type root: TreeNode
#         :rtype: str
#         """
#         if root is None:
#             return ""
#         current_level = [root]
#         val_list = []
#         while current_level and reduce(lambda x, y: x or bool(y), current_level, False):
#             next_level = []
#             for node in current_level:
#                 if node:
#                     val_list.append(str(node.val))
#                     next_level += [node.left, node.right]
#                 else:
#                     val_list.append('null')
#                     next_level += [None, None]
#             current_level = next_level
#         return ','.join(val_list)
#
#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
#
#         :type data: str
#         :rtype: TreeNode
#         """
#         if len(data) == 0:
#             return None
#         val_list = data.split(',')
#         if val_list[0] == 'null':
#             return None
#         root = TreeNode(int(val_list[0]))
#         current_level = [root]
#         i = 1
#         while current_level and i < len(val_list):
#             next_level = []
#             for node in current_level:
#                 if node is None:
#                     next_level += [None, None]
#                     i += 2
#                     continue
#                 if i >= len(val_list):
#                     break
#                 node.left = None if val_list[i] == 'null' else TreeNode(int(val_list[i]))
#                 i += 1
#                 if i >= len(val_list):
#                     break
#                 node.right = None if val_list[i] == 'null' else TreeNode(int(val_list[i]))
#                 i += 1
#                 next_level += [node.left, node.right]
#             current_level = next_level
#         return root


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def tostr(node):
            return str(node.val) if node else '#'
        if not root:
            return '#'
        return ','.join([tostr(root), self.serialize(root.left), self.serialize(root.right)])

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        from collections import deque

        def do_deserialize(data_list):
            if data_list[0] == '#':
                data_list.popleft()
                return None
            else:
                node = TreeNode(data_list.popleft())
                node.left = do_deserialize(data_list)
                node.right = do_deserialize(data_list)
                return node

        if data:
            return do_deserialize(deque(data.split(',')))
        return None

if __name__ == '__main__':
    # print Codec().deserialize(Codec().serialize(TreeNode.build_by_level_order([1,2,3,4])))
    TreeNode.print_in_level_order(Codec().deserialize(Codec().serialize(TreeNode.build_by_level_order([1,2,3,4]))))
    TreeNode.print_in_level_order(Codec().deserialize(Codec().serialize(TreeNode.build_by_level_order([1,2,3,4,'#',5,6]))))
    TreeNode.print_in_level_order(Codec().deserialize(Codec().serialize(TreeNode.build_by_level_order([1]))))
    TreeNode.print_in_level_order(Codec().deserialize(Codec().serialize(TreeNode.build_by_level_order([]))))
    TreeNode.print_in_level_order(Codec().deserialize(Codec().serialize(TreeNode.build_by_level_order([5,2,3,null,null,2,4,3,1]))))
    TreeNode.print_in_level_order(Codec().deserialize(Codec().serialize(TreeNode.build_by_level_order([5,2,3,null,null,2,4,3,1]))))