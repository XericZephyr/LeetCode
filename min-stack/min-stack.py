__author__ = 'clp'

class MinStack(object):


    def __init__(self):
        """
        initialize your data structure here.
        """
        self._data_list = []
        self._min_index = 0

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self._data_list.append(x)
        self._min_index = self._min_index if x >= self._data_list[self._min_index] else len(self._data_list)-1


    def pop(self):
        """
        :rtype: nothing
        """


    def top(self):
        """
        :rtype: int
        """


    def getMin(self):
        """
        :rtype: int
        """