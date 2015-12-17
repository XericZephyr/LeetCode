

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def bit_alter(num, n):
            bit = 0x01 << (n-1)
            return num ^ bit if num & bit else num | bit

        def op(n, l):
            if n == 1:
                l.append(bit_alter(l[-1], 1))
                return
            op(n-1, l)
            l.append(bit_alter(l[-1], n))
            op(n-1, l)

        if n == 0:
            return [0]
        l = [0]
        op(n, l)
        return l

if __name__ == '__main__':
    print Solution().grayCode(2)
    print Solution().grayCode(1)
    print Solution().grayCode(0)
    print Solution().grayCode(3)
    print Solution().grayCode(4)