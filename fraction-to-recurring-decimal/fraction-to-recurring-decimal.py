

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        def abs(num):
            return num if num > 0 else -num

        def fractionUnder1(numerator, denominator):
            if numerator == 0:
                return ""
            fraction = ""
            residual_dict = {}
            str_idx = 0
            start = 0
            while numerator > 0:
                if numerator not in residual_dict:
                    residual_dict[numerator] = str_idx
                    fraction += str(numerator * 10 / denominator)
                    numerator = numerator * 10 % denominator
                    str_idx += 1
                else:
                    start = residual_dict[numerator]
                    break
            if numerator > 0:
                return "%s(%s)" % (fraction[:start], fraction[start:])
            else:
                return fraction

        isNegative = (numerator * denominator < 0)
        numerator, denominator = abs(numerator), abs(denominator)
        integer = int(numerator)/int(denominator)
        remainder = int(numerator) % int(denominator)
        fraction = fractionUnder1(remainder, denominator)
        result = ("%d.%s" % (integer, fraction)) if len(fraction) else str(integer)
        return "-%s" % result if isNegative else result

if __name__ == '__main__':
    print Solution().fractionToDecimal(1, 2)
    print Solution().fractionToDecimal(2, 1)
    print Solution().fractionToDecimal(3, 2)
    print Solution().fractionToDecimal(2, 3)
    print Solution().fractionToDecimal(0, 3)
    print Solution().fractionToDecimal(1, 3)
    print Solution().fractionToDecimal(1, 6)
    print Solution().fractionToDecimal(-50, 8)
    print Solution().fractionToDecimal(-22, -2)