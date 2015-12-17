


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def op(num, k, start, end):
            if num <= 0:
                return []
            if k == 1:
                if start <= num <= end:
                    return [[num]]
                else:
                    return []
            elif k == 2:
                l = []
                for i in range(start, num/2+1):
                    j = num - i
                    if i < j <= end:
                        l.append([i, j])
                return l
            else:
                ret = []
                for s in range(start, end + 2 - k):
                    ret += [[s] + l for l in op(num-s, k-1, s+1, end) if l]
                return ret

        return op(n, k, 1, 9)

if __name__ == '__main__':
    print Solution().combinationSum3(3, 7)
    print Solution().combinationSum3(3, 9)
    print Solution().combinationSum3(3, 2)
    print Solution().combinationSum3(1, 6)
    print Solution().combinationSum3(1, 0)
    print Solution().combinationSum3(4, 20)
