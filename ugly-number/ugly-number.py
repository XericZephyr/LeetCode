__author__ = 'clp'

#
#   https://leetcode.com/problems/ugly-number/
#

class Solution:
    # @param {integer} num
    # @return {boolean}
    def isUgly(self, num):
        if num > 0:
            while num % 5 == 0:
                num /= 5
            while num % 3 == 0:
                num /= 3
            while num % 2 == 0:
                num /= 2
            if num == 1:
                return True
        return False

if __name__ == "__main__":
    print Solution().isUgly(-5)
    print Solution().isUgly(0)
    print Solution().isUgly(6)
    print Solution().isUgly(8)
    print Solution().isUgly(14)
