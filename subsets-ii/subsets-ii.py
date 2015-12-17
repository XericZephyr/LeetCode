

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums:
            return [[]]

        def sort_counter():
            d = {}
            for n in nums:
                d[n] = d.get(n, 0) + 1
            skey = sorted(d.keys())
            return skey, d

        skey, d = sort_counter()

        def ksubsets(k, start, end):
            if k == 0:
                return [[]]
            elif k == 1:
                return [[skey[i]] for i in range(start, end+1)]
            elif start == end:
                if d[skey[start]] >= k:
                    return [[skey[start]] * k]
                else:
                    return []
            else:
                ret = []
                pivot = skey[start]
                for j in range(1+min(d[pivot], k)):
                    ret += [[pivot] * j + l for l in ksubsets(k-j, start+1, end)]
                return ret

        return reduce(lambda x, y: x + y,
                      (ksubsets(i, 0, len(skey)-1) for i in range(len(nums)+1)), [])

if __name__ == '__main__':
    # print Solution().subsetsWithDup([1,2,2,4])
    # print Solution().subsetsWithDup([1,2,2])
    l = Solution().subsetsWithDup([1,2,2,3,3,4,4,4,6])
    print l
