__author__ = 'clp'


class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._data_list = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        tmp_list = []
        for i in range(len(self._data_list)):
            tmp_list.append(self._data_list.pop())
        self._data_list.append(x)
        for i in range(len(tmp_list)):
            self._data_list.append(tmp_list.pop())

    def pop(self):
        """
        :rtype: nothing
        """
        return self._data_list.pop()


    def peek(self):
        """
        :rtype: int
        """
        assert not self.empty(), "Stack empty"
        value = self._data_list.pop()
        self._data_list.append(value)
        return value

    def empty(self):
        """
        :rtype: bool
        """
        return len(self._data_list) == 0


if __name__ == "__main__":
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    print q.pop()
    print q.pop()
    print q.peek()
    print q.empty()
    print q.pop()