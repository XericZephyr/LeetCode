

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        elif 1 <= n <= 9:
            return 1
        elif n == 10:
            return 2
        else:
            thres = 10
            while n / thres >= 1:
                thres *= 10
            thres /= 10
            first_digit = n / thres
            if first_digit >= 2:
                return self.countDigitOne(2 * thres - 1) + \
                    (n - 2*thres)/thres * self.countDigitOne(thres-1) + \
                    self.countDigitOne(n % thres)
            elif first_digit == 1:
                return 1 + n - thres + self.countDigitOne(n - thres) + self.countDigitOne(thres-1)

if __name__ == '__main__':
    print Solution().countDigitOne(13)
    print Solution().countDigitOne(19)
    print Solution().countDigitOne(20)
    print Solution().countDigitOne(21)
    print Solution().countDigitOne(30)
    print Solution().countDigitOne(99)
    print Solution().countDigitOne(2192)
