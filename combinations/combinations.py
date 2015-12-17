

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def op(k, start, end):
            if k == 0:
                return [[]]
            elif k == 1:
                return [[i] for i in range(start, end+1)]
            elif k >= 2:
                ret = []
                for i in range(start, end):
                    ret += [[i] + l for l in op(k-1, i+1, end)]
                return ret

        if n == 0 and k != 0:
            return []
        return op(k, 1, n)

if __name__ == '__main__':
    print Solution().combine(4, 2)
    print Solution().combine(5, 2)