__author__ = 'clp'

class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        elif x < 0:
            return False
        # calculate max bit
        max_bit = 1
        while x/max_bit > 0:
            max_bit *= 10
        max_bit /= 10
        l = max_bit
        r = 1
        while l >= r*10:
            l_bit = x/l % 10
            r_bit = x/r % 10
            if not (l_bit == r_bit):
                return False
            l /= 10
            r *= 10
        return True

if __name__ == "__main__":
    print Solution().isPalindrome(-0)
    print Solution().isPalindrome(-1)
    print Solution().isPalindrome(121)
    print Solution().isPalindrome(11)
    print Solution().isPalindrome(10)