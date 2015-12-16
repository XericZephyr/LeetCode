

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0
        if x == 1:
            return 1
        if n < 0:
            return 1./self.myPow(x, -n)
        elif n == 0:
            return 1
        elif n == 1:
            return x
        elif n == 2:
            return x*x
        elif n % 2:
            pow = self.myPow(x, n/2)
            return x * pow * pow
        else:
            pow = self.myPow(x, n/2)
            return pow * pow

if __name__ == '__main__':
    print Solution().myPow(5, 3)
    print Solution().myPow(2, 5)
    print Solution().myPow(2, 4)
    print Solution().myPow(2, -1)
    print Solution().myPow(2, -5)
    print Solution().myPow(0, 5000)
    print Solution().myPow(2, 1048)
    print Solution().myPow(1, 1048)