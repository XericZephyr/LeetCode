

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        l = list(range(2, n))
        current_idx = 0
        while current_idx * current_idx < n - 2:
            num = l[current_idx]
            i = current_idx + num
            while i < len(l):
                l[i] = 0
                i += num
            current_idx += 1
            while current_idx * current_idx < n - 2 and l[current_idx] == 0:
                current_idx += 1
        return len([i for i in l if i > 0])


if __name__ == '__main__':
    # print Solution().countPrimes(499979)
    print Solution().countPrimes(3)
    print Solution().countPrimes(4)
    print Solution().countPrimes(499979)
