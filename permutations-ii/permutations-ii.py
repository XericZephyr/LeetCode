


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1

        def _bfs(perm, rm_counter):
            new_perm = []
            for k, v in rm_counter.iteritems():
                if v > 0:
                    new_dict = dict(rm_counter)
                    new_dict[k] -= 1
                    new_perm += _bfs([i + [k] for i in perm], new_dict)
            return new_perm if new_perm else perm

        return _bfs([[]], counter) if nums else []

if __name__ == '__main__':
    print Solution().permuteUnique([1,1,2])
    print Solution().permuteUnique([1,1,1,2])
    print Solution().permuteUnique([])
    print Solution().permuteUnique([1])
    print Solution().permuteUnique([1] * 5 + [2] * 4)



