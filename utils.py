__author__ = 'clp'

from collections import Counter

'''
    Useful Data Structures and Utilities
'''

class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return self.val

    def __str__(self):
        return str(self.val)

    @classmethod
    def print_linked_list(cls, list_head, separator=" ->"):
        if not list_head:
            print None
            return
        n = list_head
        while n:
            print "%s" % str(n),
            if n.next:
                print "%s " % separator,
            n = n.next
        print ""

    @classmethod
    def build_linked_list(cls, element_list):
        if not element_list:
            return None
        n = list_head = cls(element_list[0])
        for x in element_list[1:]:
            n.next = cls(x)
            n = n.next
        return list_head


class TreeNode(object):

    '''
    Binary Tree Node class
    '''

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return self.val

    def __str__(self):
        return str(self.__repr__())

    @classmethod
    def build_by_level_order(cls, tree_list):
        # [1, 2, '#'] stands for 1 - left: 2, right: None
        if not tree_list or tree_list[0] == '#':
            return None
        root_node = cls(tree_list[0])
        list_pointer = 1
        current_level = [root_node]
        next_level = []
        while current_level and list_pointer < len(tree_list):
            for current_node in current_level:
                if tree_list[list_pointer] == '#':
                    n = None
                else:
                    n = cls(tree_list[list_pointer])
                    next_level.append(n)
                current_node.left = n
                list_pointer += 1
                if tree_list[list_pointer] == '#':
                    n = None
                else:
                    n = cls(tree_list[list_pointer])
                    next_level.append(n)
                current_node.right = n
                list_pointer += 1
            current_level = next_level
            next_level = []
        return root_node

    @classmethod
    def print_in_level_order(cls, root):
        if not root:
            print []
            return
        current_level = [root]
        next_level = []
        res = []
        while current_level:
            for current_node in current_level:
                if current_node:
                    res.append(current_node.val)
                    next_level.append(current_node.left if current_node.left else None)
                    next_level.append(current_node.right if current_node.right else None)
                else:
                    res.append('#')
            if reduce(lambda x, y: (y is None) and x, next_level, True):
                break
            current_level = next_level
            next_level = []
        print res


