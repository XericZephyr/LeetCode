


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        factor2roman = {100: ['C', 'D', 'M'],
                    10:  ['X', 'L', 'C'],
                    1:   ['I', 'V', 'X']}
        ret = ""
        ret += "M" * (num/1000)
        num %= 1000
        factor = 100
        while num > 0:
            b = num/factor
            if 1 <= b <= 3:
                ret += factor2roman[factor][0] * b
            elif b == 4:
                ret += factor2roman[factor][0] + factor2roman[factor][1]
            elif 5 <= b <= 8:
                ret += factor2roman[factor][1] + factor2roman[factor][0] * (b-5)
            elif b == 9:
                ret += factor2roman[factor][0] + factor2roman[factor][2]
            num %= factor
            factor /= 10
        return ret

if __name__ == '__main__':
    for i in range(1, 10):
        print Solution().intToRoman(i)
    print Solution().intToRoman(19)
    print Solution().intToRoman(29)
    print Solution().intToRoman(99)
    print Solution().intToRoman(3999)
