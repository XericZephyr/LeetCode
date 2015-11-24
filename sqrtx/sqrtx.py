

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x == 1:
            return 1
        y_n = float(x/2)
        while True:
            y_n_next = (y_n + float(x)/y_n)/2.
            if abs(y_n - y_n_next) < 1e-10:
                return int(y_n)
            else:
                y_n = y_n_next

if __name__ == '__main__':
    print Solution().mySqrt(0)
    print Solution().mySqrt(3)
    print Solution().mySqrt(9)
    print Solution().mySqrt(4)
    print Solution().mySqrt(19)
    print Solution().mySqrt(2147395599)
