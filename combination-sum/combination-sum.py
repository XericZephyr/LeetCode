

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        if not candidates or target < 1:
            return []
        candidates.sort()

        def op(C, T, start, end):
            if T == 0:
                return [[]]
            if start == end:
                if T % C[end] == 0:
                    return [[C[end]] * (T/C[end])]
                else:
                    return []
            ret = []
            pivot = C[start]
            for i in range(1+T/pivot):
                ret += [[pivot] * i + l for l in reversed(op(C, T - pivot*i, start+1, end))]
            ret.reverse()
            return ret

        return op(candidates, target, 0, len(candidates)-1)

if __name__ == '__main__':
    print Solution().combinationSum([2,3,6,7], 7)
    print Solution().combinationSum([2,3,6,7], 10)
    print Solution().combinationSum([2,3,6,7], 20)
    print Solution().combinationSum([2], 1)
