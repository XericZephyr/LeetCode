
class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self._current = 0
        self._nums = nums

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self._current < len(self._nums)

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        ret = self._nums[self._current]
        self._current += 1
        return ret


class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._iterator = iterator
        self._next = self._iterator.next() if iterator.hasNext() else None


    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self._next

    def next(self):
        """
        :rtype: int
        """
        n = self._next
        self._next = self._iterator.next() if self._iterator.hasNext() else None
        return n


    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self._next)


if __name__ == '__main__':
    iter = PeekingIterator(Iterator([1,2,3,4]))
    while iter.hasNext():
        val = iter.peek()   # Get the next element but not advance the iterator.
        print val, ' -> ',
        iter.next()         # Should return the same value as [val].