__author__ = 'clp'

class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        CONVERSION_DICT = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        n_list = [CONVERSION_DICT[s_bit] for s_bit in list(s)]
        num = 0
        while n_list:
            n = n_list.pop()
            num += n
            while n_list and n_list[-1] < n:
                num -= n_list.pop()
        return num

if __name__ == "__main__":
    print Solution().romanToInt("I")
    print Solution().romanToInt("V")
    print Solution().romanToInt("MCMLVI")
    print Solution().romanToInt("MCMXC")
    print Solution().romanToInt("MCMLIV")
    print Solution().romanToInt("XIIII")
    print Solution().romanToInt("XIV")


