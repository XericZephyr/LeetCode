

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = set()
        res = 0
        for n in nums:
            h.add(n)
        for n in nums:
            if (n-1) not in h:
                val = n
                while val in h:
                    h.remove(val)
                    res = max(res, val-n+1)
                    val += 1
        return res


if __name__ == '__main__':
    print Solution().longestConsecutive([100, 200, 4, 3, 2, 1])
    print Solution().longestConsecutive([1,3,5,7])
    print Solution().longestConsecutive([])