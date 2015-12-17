

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def sort_counter(num_list):
            d = {}
            for n in num_list:
                d[n] = d.get(n, 0) + 1
            skey = d.keys()
            skey.sort()
            return skey, d

        if not candidates:
            return []
        skey, d = sort_counter(candidates)

        def op(T, start, end):
            if T == 0:
                return [[]]
            if start > end or T < 0:
                return []
            ret = []
            pivot = skey[start]
            for i in range(d[pivot]+1):
                ret += [[pivot] * i + l for l in op(T-pivot*i, start+1, end)]
            return ret

        return op(target, 0, len(skey)-1)

if __name__ == '__main__':
    print Solution().combinationSum2([10,1,2,7,6,1,5], 8)