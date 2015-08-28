__author__ = 'clp'

class Solution(object):

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # zero pad the short number
        a, b = a.lstrip('0') or "0", b.lstrip('0') or "0"
        len_diff = abs(len(a) - len(b))
        a, b = (''.join(['0' for i in range(len_diff)]) + a, b) if len(a) < len(b) else \
            (a, ''.join(['0' for i in range(len_diff)]) + b)
        al, bl = list(a), list(b)
        res = ""
        overflow = 0
        while al and bl:
            a_bit, b_bit = int(al.pop()), int(bl.pop())
            r = a_bit + b_bit + overflow
            overflow = int(r/2)
            res = str(r%2) + res
        if overflow:
            res = '1' + res
        return res

if __name__ == "__main__":
    print Solution().addBinary("0", "0")
    print Solution().addBinary("11", "1")
    print Solution().addBinary("11", "11")
    print Solution().addBinary("11", "111")


