



class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2147483647
        sign = 1 if (dividend > 0 and divisor > 0) or \
                    (dividend < 0 and divisor < 0) else -1
        dividend, divisor = abs(dividend), abs(divisor)
        if divisor == 0:
            raise Exception("divided by 0")
        ret = 0
        if dividend < divisor:
            ret = 0
        elif dividend == divisor:
            ret = 1
        elif divisor == 1:
            ret = dividend
        elif divisor == 2:
            ret = dividend >> 1
        else:
            while dividend > divisor:
                temp = divisor
                i = 0
                while temp < dividend:
                    temp <<= 1
                    i += 1
                dividend -= (temp >> 1)
                ret += (1 << (i-1))

        ret = ret if sign > 0 else -ret
        if ret >= MAX_INT:
            return MAX_INT
        elif ret < -MAX_INT-1:
            return -MAX_INT-1
        else:
            return ret

if __name__ == '__main__':
    # print Solution().divide(5,2)
    # print Solution().divide(500000000,35)
    print Solution().divide(-2147483648,1)


