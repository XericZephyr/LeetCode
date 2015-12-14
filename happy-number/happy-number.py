


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def happy(num):
            return sum([int(d)*int(d) for d in list(str(num))])

        num_list = []
        while n > 1 and n not in num_list:
            num_list.append(n)
            n = happy(n)
        return n == 1


if __name__ == '__main__':
    print Solution().isHappy(19)
    print Solution().isHappy(50)
    print Solution().isHappy(150)