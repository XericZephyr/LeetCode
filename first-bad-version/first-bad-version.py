

def isBadVersion(version):
    if version >= 5:
        return True
    else:
        return False

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def doFirstBadVersion(start, end):
            pivot = int((start + end)/2)
            if isBadVersion(pivot):
                if not isBadVersion(pivot-1):
                    return pivot
                else:
                    return doFirstBadVersion(start, pivot-1)
            else:
                return doFirstBadVersion(pivot+1, end)

        if n < 1:
            return 0
        elif n == 1:
            return 1 if isBadVersion(1) else 0
        elif n > 1:
            return doFirstBadVersion(1, n)


if __name__ == '__main__':
    print Solution().firstBadVersion(10)
    print Solution().firstBadVersion(11)
    print Solution().firstBadVersion(12)
    print Solution().firstBadVersion(16)
    print Solution().firstBadVersion(4)