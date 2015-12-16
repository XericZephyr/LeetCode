

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        N = len(citations)
        left, right = 0, N
        while left < right - 1:
            mid = (left + right) / 2
            if citations[mid] < N - mid:
                left = mid
            else:
                right = mid
        return N - left if N - left <= citations[left] else N - right

if __name__ == '__main__':
    print Solution().hIndex([0, 1, 3, 5, 6])
    print Solution().hIndex([1,1,2,3,4,5,7])
    print Solution().hIndex([1,1,4])
    print Solution().hIndex([0])
    print Solution().hIndex([0, 0])
    print Solution().hIndex([1, 1])
    print Solution().hIndex([1])
    print Solution().hIndex([1,1,2])