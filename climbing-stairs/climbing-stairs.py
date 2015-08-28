__author__ = 'clp'


#
#   Slower one, recursively
#
class SlowSolution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 1 + self.climbStairs(1)
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)

#
#   Faster one, close form solution,
#   calculate the how many 2 steps there can be and use combination mathematics
#   For n stairs, the total combination is
#   \sum\limits_{m=1}^{\lfloor n/2\rfloor} C^m_{n-m}
#
class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return reduce(lambda s, m: s + self.combination(n-m, m), range(1+int(n/2)), 0)

    def combination(self, n, k):
        # combination number for n choose k
        multiply_func = lambda x, y: x*y
        return reduce(multiply_func, range(n, n-k, -1), 1)/reduce(multiply_func, range(1, k+1), 1)

if __name__ == "__main__":
    print SlowSolution().climbStairs(3)
    print SlowSolution().climbStairs(4)
    # print Solution().climbStairs(50)
    # print FastSolution().combination(5, 3)
    # print FastSolution().combination(3, 1)
    # print FastSolution().combination(3, 0)
    print Solution().climbStairs(3)
    print Solution().climbStairs(4)
    print Solution().climbStairs(50)
    for x in range(1, 20):
        print "Validating x = %d..." % x
        assert Solution().climbStairs(x) == SlowSolution().climbStairs(x)