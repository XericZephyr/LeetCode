

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache_list = [1, 1, 2]
        if n <= 2:
            return cache_list[n]
        for i in range(3, n+1):
            cache_list.append(sum([n1*n2 for n1, n2 in zip(cache_list, reversed(cache_list))]))
        return cache_list[n]

if __name__ == '__main__':
    print Solution().numTrees(3)
    print Solution().numTrees(4)
    print Solution().numTrees(25)
