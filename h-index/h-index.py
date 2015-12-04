

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        h_index = 0
        for i in reversed(citations):
            if h_index + 1 <= i:
                h_index += 1
            else:
                return h_index
        return h_index


if __name__ == '__main__':
    print Solution().hIndex([3,0,6,1,5])
    print Solution().hIndex([0,0,0])
    print Solution().hIndex([0,6,5])
    print Solution().hIndex([1])
    print Solution().hIndex([1, 1])
    print Solution().hIndex([])
