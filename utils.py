__author__ = 'clp'

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
                if list_pointer >= len(tree_list) or tree_list[list_pointer] == '#':
                    n = None
                else:
                    n = cls(tree_list[list_pointer])
                    next_level.append(n)
                current_node.left = n
                list_pointer += 1
                if list_pointer >= len(tree_list) or tree_list[list_pointer] == '#':
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



class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

    def __repr__(self):
        # visit = {}
        # stack = [self]
        # rep = []
        # while stack:
        #     current = stack.pop()
        #     visit[current.label] = True
        #     for n in current.neighbors:
        #         if n not in visit:
        #             stack.append(n)
        #         else:
        #             rep.append("%s#%s" % (str(current.label), str(n.label)))
        # return ', '.join(rep)
        return str(self.label)

    def __getitem__(self, item):
        for n in self.neighbors:
            if item == n.label:
                return n
        raise KeyError(item)


class BinaryIndexedTree(object):
    #
    #   Notice, idx is 1-based indexing
    #

    def __init__(self, init_list):
        self._tree = [0] * (1+len(init_list))
        for idx in range(1, 1+len(init_list)):
            self.add_value(idx, init_list[idx-1])

    def add_value(self, idx, val):
        while idx < len(self._tree):
            self._tree[idx] += val
            idx += (idx & -idx)

    def get_sum(self, idx):
        s = 0
        if idx == 0:
            return 0
        while idx > 0:
            s += self._tree[idx]
            idx -= (idx & -idx)
        return s

    def get_value(self, idx):
        return self.get_sum(idx) - self.get_sum(idx-1)

    def update(self, idx, val):
        # val is the add
        self.add_value(idx, val-self.get_value(idx))

    def __getitem__(self, item):
        #
        #   Here, we provide zero-based indexing in [] indexing
        #
        if isinstance(item, slice):
            start = item.start if item.start is not None else 0
            stop = item.stop+1 if item.stop is not None else len(self._tree)-1
            return self.get_sum(stop) - self.get_sum(start)
        elif isinstance(item, int):
            return self.get_value(item+1)
        raise KeyError(str(item))

    def __setitem__(self, key, value):
        if isinstance(key, int):
            self.update(key+1, value)
            return
        raise KeyError(str(key))

